import json
import requests
from collections import OrderedDict

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

class CleanTable:
    def __init__(self, url_id):
        self.api_url = f"http://127.0.0.1:8000/api/raw-data?url_id={url_id}"
        self.update_url = "http://127.0.0.1:8000/api/raw-data/{id}/"
        self.headers = {
            "Authorization": f"Bearer {self.get_access_token()}",
            "Content-Type": "application/json"
        }
        self.all_tables = {}
        self.table_occurrences = {}
        
    @staticmethod
    def get_access_token():
        return "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoyMDU2NjkxNTg1LCJpYXQiOjE3NDEzMzE1ODUsImp0aSI6IjhmMDdiZmJmZDZjMTQ1ZTY4MDZiMWQxYjVjZjU0Y2QxIiwidXNlcl9pZCI6MX0.7uoBSyMHE96ZkWTA-Y4U5yBnhjNw4vp7BQRuoWwg8A4"

    def fetch_data(self):
        """Fetch data from API"""
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

    def clean_empty_strings(self, data):
        """
        Remove columns where all rows in a table have empty strings at the same index
        """
        if isinstance(data, dict):
            cleaned_dict = OrderedDict()
            for key, value in data.items():
                cleaned_dict[key] = self.clean_empty_strings(value)
            return dict(cleaned_dict)
            
        elif isinstance(data, list) and data and all(isinstance(row, list) for row in data):
            if not data:
                return data
                
            max_length = max(len(row) for row in data)
            padded_data = [row + [""] * (max_length - len(row)) for row in data]
            
            columns_to_remove = set()
            for i in range(max_length):
                if all(row[i] == "" for row in padded_data):
                    columns_to_remove.add(i)
            
            if columns_to_remove:
                return [[val for j, val in enumerate(row) if j not in columns_to_remove] 
                       for row in data]
            return data
            
        return data

    def remove_duplicate_tables_within(self, tables_data):
        """
        Remove duplicate tables within a single tables_data structure
        """
        if isinstance(tables_data, dict):
            cleaned_dict = OrderedDict()
            seen_tables = set()
            
            for key, value in tables_data.items():
                cleaned_value = self.clean_empty_strings(value)
                if isinstance(cleaned_value, list) and cleaned_value:
                    table_tuple = tuple(tuple(row) for row in cleaned_value)
                    if table_tuple not in seen_tables:
                        seen_tables.add(table_tuple)
                        cleaned_dict[key] = cleaned_value
                elif cleaned_value is not None:
                    cleaned_dict[key] = cleaned_value
                    
            return dict(cleaned_dict) if cleaned_dict else None
            
        return tables_data

    def process_tables_data(self, tables_data):
        """
        Process tables_data:
        1. Remove tables that appear in multiple entries
        2. Remove identical tables within the structure
        3. Remove columns where all rows have empty strings
        """
        if not isinstance(tables_data, dict):
            return tables_data
            
        cleaned_tables = OrderedDict()
        for key, value in tables_data.items():
            if isinstance(value, list):
                table_tuple = tuple(tuple(row) for row in value)
                if table_tuple not in self.table_occurrences or self.table_occurrences[table_tuple] == 1:
                    cleaned_tables[key] = value
        return self.remove_duplicate_tables_within(cleaned_tables)

    def process_entry(self, entry):
        """Process a single data entry"""
        if "tables_data" in entry:
            cleaned_tables = self.process_tables_data(entry["tables_data"])
            if cleaned_tables is not None:
                entry["tables_data"] = cleaned_tables
            else:
                del entry["tables_data"]
        return entry

    def update_data(self, data):
        """Update cleaned data via API"""
        for entry in data:
            record_id = entry.get("id")
            if not record_id:
                print("❌ Missing ID in record, skipping update.")
                continue
            update_payload = {
                "tables_data": entry.get("tables_data", {})
            }
            try:
                update_response = requests.patch(
                    self.update_url.format(id=record_id),
                    headers=self.headers,
                    json=update_payload
                )
                update_response.raise_for_status()
                print(f"✅ Successfully updated record ID {record_id}")
            except requests.RequestException as e:
                print(f"❌ Failed to update record ID {record_id}: {e}")

    def process(self):
        """Main processing method"""
        data = self.fetch_data()
        if not data:
            return

        # Reset instance variables
        self.all_tables = {}
        self.table_occurrences = {}
        
        # Identify all tables and their occurrences across entries
        for idx, entry in enumerate(data):
            if "tables_data" in entry:
                for key, value in entry["tables_data"].items():
                    if isinstance(value, list):
                        table_tuple = tuple(tuple(row) for row in value)
                        if table_tuple not in self.all_tables:
                            self.all_tables[table_tuple] = []
                        self.all_tables[table_tuple].append((idx, key))
                        self.table_occurrences[table_tuple] = self.table_occurrences.get(table_tuple, 0) + 1

        # Process each entry
        cleaned_data = [self.process_entry(entry) for entry in data]
        
        # Update the cleaned data
        self.update_data(cleaned_data)