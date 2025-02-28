from bs4 import BeautifulSoup

def get_tables_data(soup):
    tables_data = {}
    tables = soup.find_all("table")

    social_platforms = ["facebook.com", "twitter.com", "linkedin.com", "instagram.com", "t.me", "youtube.com"]

    for index, table in enumerate(tables, start=1):
        table_data = []
        rows = table.find_all("tr")

        for row in rows:
            cells = row.find_all("td")
            row_data = []
            
            for cell in cells:
                text = cell.get_text(strip=True)
                
                link = cell.find("a", href=True)
                if link:
                    href = link["href"]
                    if href.startswith(("mailto:", "tel:", "ph:")):
                        text = href
                    elif any(platform in href for platform in social_platforms):
                        text = href
                
                row_data.append(text)

            if row_data:
                table_data.append(row_data)

        if table_data:
            tables_data[f"table{index}"] = table_data

    return tables_data

def get_cleaned_soup(soup):
    tags_to_remove = [
        "header", "footer", "script", "style", "noscript", "nav", "iframe", "table", 
        "br", "hr", "input", "svg", "aside", "button", "link", "meta", "picture", 
        "source", "object", "embed", "param", "canvas", "map", "area"
    ]

    for tags in tags_to_remove:
        for tag in soup.find_all(tags):
            tag.decompose()
    
    for pagination in soup.find_all(class_=lambda x: x is not None and isinstance(x, str) and "pagination" in x.lower()):
        pagination.decompose()

    for tag in soup.find_all(True):
        if tag.text.strip() == "" or tag.text.strip() ==  None:
            tag.decompose()
    
    return soup