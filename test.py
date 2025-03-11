import json
import requests

# API Configuration
API_URL = "http://127.0.0.1:8000/api/raw-data?url_id=391"
UPDATE_URL = "http://127.0.0.1:8000/api/raw-data/{id}/"
ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoyMDU2NjkxNTg1LCJpYXQiOjE3NDEzMzE1ODUsImp0aSI6IjhmMDdiZmJmZDZjMTQ1ZTY4MDZiMWQxYjVjZjU0Y2QxIiwidXNlcl9pZCI6MX0.7uoBSyMHE96ZkWTA-Y4U5yBnhjNw4vp7BQRuoWwg8A4"

HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

# Function to extract full tag data for deduplication
def extract_full_tag_data(obj, tags_set):
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
            extract_full_tag_data(value, tags_set)
    elif isinstance(obj, list):
        for item in obj:
            extract_full_tag_data(item, tags_set)

# Function to clean JSON data
def clean_json(obj):
    if isinstance(obj, dict):
        href = obj.get("href", "")

        # Exclude pages with "page" in the href
        if "page" in href:
            return None

        tag_info = (
            obj.get("tag", ""),
            obj.get("text", "").strip(),
            href,
            json.dumps(obj.get("children", []), sort_keys=True)
        )
        if tag_info in common_tag_data:
            return None

        # Recursively clean JSON
        cleaned_obj = {k: clean_json(v) for k, v in obj.items()}
        cleaned_obj = {k: v for k, v in cleaned_obj.items() if v is not None}

        # Remove empty tags
        if obj.get("tag") and not obj.get("text", "").strip() and not obj.get("href", "") and not cleaned_obj.get("children"):
            return None

        return cleaned_obj

    elif isinstance(obj, list):
        cleaned_list = [cleaned_item for item in obj if (cleaned_item := clean_json(item)) is not None]
        return cleaned_list if cleaned_list else None

    return obj

# Function to clean text data
def clean_text(cleaned_data):
    for data in cleaned_data:
        if 'raw_json' in data:
            data['raw_data'] = serialize_text_and_links(data['raw_json'])
    return cleaned_data

# Fetch raw data from API
try:
    response = requests.get(API_URL, headers=HEADERS)
    response.raise_for_status()
    data = response.json()
except requests.RequestException as e:
    print(f"❌ API request failed: {e}")
    exit()
except json.JSONDecodeError:
    print("❌ Failed to decode JSON from API response.")
    exit()

if not isinstance(data, list):
    print("❌ Unexpected response format: expected a list.")
    exit()

# Extract and Deduplicate Data
all_tag_data = [set() for _ in range(len(data))]
for i, entry in enumerate(data):
    extract_full_tag_data(entry, all_tag_data[i])

common_tag_data = set.intersection(*all_tag_data) if all_tag_data else set()

# Clean JSON and Text Data
cleaned_data = [cleaned_entry for entry in data if (cleaned_entry := clean_json(entry)) is not None]
cleaned_data = clean_text(cleaned_data)

# ✅ Update each record in the database via API
for original, cleaned in zip(data, cleaned_data):
    record_id = original.get("id")  # Ensure your API has an 'id' field
    if not record_id:
        print("❌ Missing ID in record, skipping update.")
        continue

    update_payload = {
        "raw_json": cleaned.get("raw_json"),
        "raw_data": cleaned.get("raw_data")
    }

    update_url = UPDATE_URL.format(id=record_id)

    try:
        update_response = requests.patch(update_url, headers=HEADERS, json=update_payload)
        update_response.raise_for_status()
        print(f"✅ Successfully updated record ID {record_id}")
    except requests.RequestException as e:
        print(f"❌ Failed to update record ID {record_id}: {e}")

print("✅ All updates completed.")