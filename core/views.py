import pandas as pd
from django.contrib import messages
from api.models.url_data import UrlData
from api.models.domain_data import DomainData
from django.shortcuts import render, redirect
from api.utils import is_valid_url, process_next_url

def home_view(request):
    """Handles website scraping requests and file uploads."""
    if request.method == "POST":
        website_url = request.POST.get("url")
        pagination_enabled = request.POST.get("pagination") == "on"
        uploaded_file = request.FILES.get("excel_file")
        urls_to_process = []

        if website_url:
            website_url = website_url.strip()
            if not is_valid_url(website_url):
                messages.error(request, "Invalid URL! URLs ending with restricted file extensions are not allowed.")
                return redirect("home")

            url_obj, created = UrlData.objects.get_or_create(
                url=website_url,
                defaults={"pagination_enabled": pagination_enabled, "scraping_status": "pending"}
            )

            if not created:
                messages.info(request, f"{website_url} already exists.")
            else:
                urls_to_process.append(website_url)

        elif uploaded_file:
            if not uploaded_file.name.endswith((".xls", ".xlsx")):
                messages.error(request, "Invalid file type! Please upload an Excel file (.xls, .xlsx).")
                return redirect("home")

            try:
                df = pd.read_excel(uploaded_file)

                if "urls" not in df.columns:
                    messages.error(request, "Invalid file format! Column 'urls' not found.")
                    return redirect("home")

                urls = df["urls"].dropna().unique()
                added_count = 0

                for url in urls:
                    url = url.strip()
                    if is_valid_url(url):
                        _, created = UrlData.objects.get_or_create(
                            url=url,
                            defaults={"pagination_enabled": pagination_enabled, "scraping_status": "pending"}
                        )
                        if created:
                            added_count += 1
                            urls_to_process.append(url)

                messages.success(request, f"{added_count} valid URLs uploaded successfully!")

            except Exception as e:
                messages.error(request, f"Error processing file: {str(e)}")
                return redirect("home")

        if urls_to_process:
            process_next_url()

        return redirect("home")

    websites_data = UrlData.objects.all()
    domain_data = DomainData.objects.all()

    return render(request, "index.html", {"websites_data": websites_data, "domain_data": domain_data})