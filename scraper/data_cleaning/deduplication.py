import json
import requests

class DataCleaner:
    def __init__(self, url_id):
        self.api_url = f"http://127.0.0.1:8000/api/raw-data?url_id={url_id}"
        self.update_url = "http://127.0.0.1:8000/api/raw-data/{id}/"
        self.headers = {
            "Authorization": f"Bearer {self.get_access_token()}",
            "Content-Type": "application/json"
        }
        self.common_tag_data = set()

    @staticmethod
    def get_access_token():
        return "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoyMDU2NjkxNTg1LCJpYXQiOjE3NDEzMzE1ODUsImp0aSI6IjhmMDdiZmJmZDZjMTQ1ZTY4MDZiMWQxYjVjZjU0Y2QxIiwidXNlcl9pZCI6MX0.7uoBSyMHE96ZkWTA-Y4U5yBnhjNw4vp7BQRuoWwg8A4"

    def fetch_data(self):
        try:
            response = requests.get(self.api_url, headers=self.headers)
            response.raise_for_status()
            data = response.json()
            if not isinstance(data, list):
                print("❌ Unexpected response format: expected a list.")
                return []
            return data
        except requests.RequestException as e:
            print(f"❌ API request failed: {e}")
            return []
        except json.JSONDecodeError:
            print("❌ Failed to decode JSON from API response.")
            return []

    def extract_full_tag_data(self, obj, tags_set):
        if isinstance(obj, dict) and "tag" in obj:
            tag_info = (
                obj["tag"],
                obj.get("text", "").strip(),
                obj.get("href", ""),
                json.dumps(obj.get("children", []), sort_keys=True)
            )
            tags_set.add(tag_info)
        
        if isinstance(obj, dict):
            for value in obj.values():
                self.extract_full_tag_data(value, tags_set)
        elif isinstance(obj, list):
            for item in obj:
                self.extract_full_tag_data(item, tags_set)

    def clean_json(self, obj):
        if isinstance(obj, dict):
            href = obj.get("href", "")
            if "page" in href or (self.common_tag_data and (obj.get("tag"), obj.get("text", "").strip(), href, json.dumps(obj.get("children", []), sort_keys=True)) in self.common_tag_data):
                return None
            cleaned_obj = {k: self.clean_json(v) for k, v in obj.items()}
            cleaned_obj = {k: v for k, v in cleaned_obj.items() if v is not None}
            return cleaned_obj if cleaned_obj else None
        elif isinstance(obj, list):
            cleaned_list = [cleaned_item for item in obj if (cleaned_item := self.clean_json(item)) is not None]
            return cleaned_list if cleaned_list else None
        return obj

    def serialize_text_and_links(self, data) -> str:
        tag_data = []
        def extract_tags(node):
            if isinstance(node, dict):
                tag_data.extend([node[key] for key in ("text", "href") if key in node])
                if "children" in node:
                    for child in node["children"]:
                        extract_tags(child)
            elif isinstance(node, list):
                for item in node:
                    extract_tags(item)
        extract_tags(data)
        return "\n".join(tag_data)

    def clean_text(self, cleaned_data):
        for data in cleaned_data:
            if 'raw_json' in data:
                data['raw_data'] = self.serialize_text_and_links(data['raw_json'])
        return cleaned_data

    def update_data(self, data):
        for original, cleaned in zip(data, self.clean_text(data)):
            record_id = original.get("id")
            if not record_id:
                print("❌ Missing ID in record, skipping update.")
                continue
            update_payload = {
                "raw_json": cleaned.get("raw_json"),
                "raw_data": cleaned.get("raw_data")
            }
            try:
                update_response = requests.patch(self.update_url.format(id=record_id), headers=self.headers, json=update_payload)
                update_response.raise_for_status()
                print(f"✅ Successfully updated record ID {record_id}")
            except requests.RequestException as e:
                print(f"❌ Failed to update record ID {record_id}: {e}")

    def process(self):
        data = self.fetch_data()
        if not data:
            return
        all_tag_data = [set() for _ in range(len(data))]
        for i, entry in enumerate(data):
            self.extract_full_tag_data(entry, all_tag_data[i])
        self.common_tag_data = set.intersection(*all_tag_data) if all_tag_data else set()
        cleaned_data = [cleaned_entry for entry in data if (cleaned_entry := self.clean_json(entry)) is not None]
        self.update_data(cleaned_data)
    