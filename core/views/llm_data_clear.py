import json
from django.http import JsonResponse
from django.views import View
from groq import Groq
from django.conf import settings

class DeepSeekExtractor:
    def __init__(self):
        self.api_key = settings.GROQ_API_KEY
        self.client = Groq(api_key=self.api_key)

    def query_model(self, json_input):
        """Send JSON input to DeepSeek and get raw CSV output."""
        prompt = (
            "Extract structured data from the following JSON and return ONLY raw CSV data with columns: "
            "Name, Email, Phone, Title, and Social Link (if available). Ensure no duplicates. "
            "Do NOT include explanations, just output the CSV.\n\n"
            f"JSON Input:\n{json.dumps(json_input, indent=2)}"
        )

        try:
            response = self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "You are an AI that extracts data and returns ONLY raw CSV."},
                    {"role": "user", "content": prompt}
                ],
                model="llama-3.3-70b-versatile",
                temperature=1,
                max_tokens=2048
            )

            if not response or not response.choices:
                return None

            return response.choices[0].message.content.strip()

        except Exception as e:
            return None

        return None

class ExtractDataView(View):
    def post(self, request):
        try:
            json_input = json.loads(request.body)
            extractor = DeepSeekExtractor()
            csv_output = extractor.query_model(json_input)

            if csv_output:
                return JsonResponse({"csv_data": csv_output}, status=200)
            else:
                return JsonResponse({"error": "Failed to process data"}, status=500)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON input"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)