import csv
import json
from groq import Groq
from io import StringIO
from django.views import View
from django.conf import settings
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class DeepSeekExtractor:
    def __init__(self):
        self.api_key = settings.GROQ_API_KEY
        self.client = Groq(api_key=self.api_key)

    def query_model(self, json_input):
        """Send JSON input to DeepSeek and get raw CSV output."""
        prompt = (
            'Extract structured data of staff (persons, members, or employees) from the given JSON and return ONLY raw CSV data '
            'with the following columns: "Name", "Email", "Phone", "Designation", and "Social Link" (only relevant social media links, if available).\n\n'
            
            'Output must follow strict CSV formatting:\n'
            '- Double quotes around all values.\n'
            '- Proper escaping of double quotes within values.\n'
            
            'Email Validation:\n'
            '- Ensure "Email" follows a proper email format (e.g., "example@domain.tld").\n'
            '- A valid email must contain "@" and a domain (any type, such as ".com", ".org", ".net", ".edu", ".gov", ".co.uk", ".io", etc.).\n'
            '- If "Email" is missing or invalid, leave it empty ("").\n'
            
            'Phone Validation:\n'
            '- Ensure "Phone" contains only valid phone numbers, formatted correctly.\n'
            '- Remove any non-numeric characters except "+" at the beginning for international numbers.\n'
            '- Acceptable formats include:\n'
            '  - "+1 1234567890" (International format with country code)\n'
            '  - "123-456-7890" or "(123) 456-7890" (Common US formats, should be normalized)\n'
            '- If "Phone" is missing or invalid, leave it empty ("").\n'
            
            'Social Link Validation:\n'
            '- Extract only valid social media profile links from platforms such as LinkedIn, Twitter (X), Facebook, Instagram, or other professional networking sites.\n'
            '- Ensure the link starts with "http://" or "https://".\n'
            '- Do not include general website links, only direct profile URLs.\n'
            '- If no valid social media link is found, leave it empty ("").\n'
            
            'Deduplication Rules:\n'
            '- Remove duplicate entries based on "Email" and "Name". If "Email" is empty, use "Name" + "Phone" for deduplication.\n'
            
            'Additional Rules:\n'
            '- If no valid staff data is found, return "None".\n'
            '- NO additional explanations, text, or formatting—ONLY raw CSV output.\n\n'
            
            'Example:\n'
            '"Name","Email","Phone","Designation","Social Link"\n'
            '"Lakeesha Brown","","","Vice President and Chief Human Resources Officer",""\n'
            '"Gopal Yadav","gopal.y@gmail.com","+91 7376096573","Software Engineer","https://www.linkedin.com/in/gopal-y-959451208/"\n\n'
            
            f'JSON Input:\n{json.dumps(json_input, indent=2)}'
        )

        try:
            response = self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "You are an AI that extracts data and returns ONLY raw CSV."},
                    {"role": "user", "content": prompt}
                ],
                model="deepseek-r1-distill-llama-70b",
                temperature=1,
                max_tokens=6000
            )

            if not response or not response.choices:
                return None

            return response.choices[0].message.content.strip()

        except Exception as e:
            return None

def csv_to_json(csv_data):
    """Convert CSV string to JSON format."""
    if csv_data == "None" or not csv_data:
        return []
    
    csv_file = StringIO(csv_data)
    csv_reader = csv.DictReader(csv_file)
    
    json_data = []
    for row in csv_reader:
        json_data.append({
            "name": row.get("Name", ""),
            "email": row.get("Email", ""),
            "phone": row.get("Phone", ""),
            "designation": row.get("Designation", ""),
            "social_link": row.get("Social Link", "")
        })
    
    return json_data

def extract_think_to_header(text):
    try:
        after_think = ""
        if "</think>" in text:
            find_think = text.find("</think>")
            after_think = text[find_think+len("</think>")::]
        else:
            after_think = text

        if '```' in after_think:
            after_think = after_think.split('```')[1]
            if "csv" in after_think:
                after_think = after_think.split('csv')[1]
                
        header_start = after_think.strip().find("Name")

        if header_start != -1:
            return after_think[header_start::].strip()
        return None
    except IndexError:
        return None

@method_decorator(csrf_exempt, name='dispatch')
class ExtractDataView(View):
    def post(self, request):
        try:
            json_input = json.loads(request.body)
            extractor = DeepSeekExtractor()
            csv_output = extractor.query_model(json_input)
            print(f"befor {csv_output}")
            csv_output = extract_think_to_header(csv_output)
            print(f"after {csv_output}")
            if csv_output is not None:
                json_output = csv_to_json(csv_output)
                return JsonResponse({"data": json_output}, status=200)
            else:
                return JsonResponse({"error": "Failed to process data"}, status=500)
                
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON input"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)