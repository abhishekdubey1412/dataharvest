import json
import requests
from bs4 import BeautifulSoup
from api.models.raw_data import RawData
from api.models.scraped_data import ScrapedData

def call_extract_data_api(json_input):
    url = 'http://127.0.0.1:8000/staff-ai-extract/'
    try:
        response = requests.post(url, json=json_input)

        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Error: {response.status_code}, {response.text}"}

    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

def process_raw_data(raw_data):
    """Call API to extract structured data from raw data and save it."""
    filter_json_data = call_extract_data_api({"raw_data": raw_data.raw_data})

    if "data" in filter_json_data:
        for item in filter_json_data["data"]:
            ScrapedData.objects.create(
                url_id=raw_data.url_id,
                raw_id=raw_data,
                name=item.get("name"),
                email=item.get("email"),
                phone=item.get("phone"),
                designation=item.get("designation"),
                social_link=item.get("social_link"),
                created_at=raw_data.scraped_at
            )
    else:
        print("No data found or API error.")

EXCLUDED_TAGS = {
    "header", "footer", "script", "style", "noscript", "nav", "iframe", 
    "input", "svg", "aside", "button", "link", "meta", "picture", 
    "source", "object", "embed", "param", "canvas", "map", "area", "figure",
    "img", "br", "hr", "i", "table"
}

class HtmlExtractor:
    def __init__(self, html):
        self.html = html
        self.extracted_data = []

    def extract_and_save_data(self):
        """Extracts structured data from HTML and stores it in `self.extracted_data`."""
        soup = BeautifulSoup(self.html, "html.parser")
        
        for tag in soup.find_all(EXCLUDED_TAGS):
            tag.decompose()

        def get_direct_text(tag):
            """Extracts direct text content from an HTML tag."""
            return tag.get_text(strip=True) if tag.string else ""

        def build_json(tag, parent_path=""):
            """Recursively constructs a structured JSON representation."""
            if not tag.name:
                return None

            if tag.name == "a" and not tag.has_attr("href"):
                return None
            
            if tag.name == "p" and 2 < len(tag.get_text(strip=True)) > 80:
                return None
        
            current_path = f"{parent_path}.{tag.name}" if parent_path else tag.name
            
            children = [
                build_json(child, current_path) for child in tag.find_all(recursive=False)
            ]
            children = [child for child in children if child]
            
            if len(children) == 1:
                return children[0]
            
            if tag.name == "div" and any(isinstance(child, dict) and child.get("tag", "").endswith("div") for child in children):
                return children
            
            node = {"tag": current_path}
            
            if tag.name == "a" and tag.has_attr("href") and tag["href"] != "#":
                node["href"] = tag["href"]
            else:
                text = get_direct_text(tag)
                if text and 3 <= len(text) <= 90:
                    node["text"] = text
            
            if children:
                node["children"] = children
            
            if not node.get("text") and not node.get("href") and not node.get("children"):
                return None
            
            if "children" in node and len(node) == 1:
                return node["children"]
            
            return node

        self.extracted_data = build_json(soup.body) if soup.body else []
        return self.extracted_data if isinstance(self.extracted_data, list) else [self.extracted_data]

    def serialize_text_and_links(self):
        """Serializes extracted text and links into a structured format."""
        tag_data = []

        def extract_tags(node):
            if isinstance(node, dict):
                if "text" in node:
                    tag_data.append(node["text"])
                if "href" in node:
                    tag_data.append(node["href"])
                
                if "children" in node:
                    for child in node["children"]:
                        extract_tags(child)

            elif isinstance(node, list):
                for item in node:
                    extract_tags(item)

        extract_tags(self.extracted_data)
        return "\n".join(tag_data)

class DataExtracted:
    @staticmethod
    def get_tables_data(soup):
        tables_data = {}
        tables = soup.find_all("table")

        social_platforms = ["facebook.com", "twitter.com", "linkedin.com", "instagram.com", "t.me", "youtube.com", "x.com"]

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
                            text = href.split(":")[1]
                        elif any(platform in href for platform in social_platforms):
                            text = href
                    
                    row_data.append(text)

                if row_data:
                    table_data.append(row_data)

            if table_data:
                if all(len(row) == len(table_data[0]) for row in table_data):
                    tables_data[f"table{index}"] = table_data
                else:
                    table_data.pop(0)
                    if table_data:
                        tables_data[f"table{index}"] = table_data

        return tables_data
 
    @staticmethod
    def extract_data(driver, url_id):
        soup = BeautifulSoup(driver.page_source, "html.parser")
        tables_data = DataExtracted.get_tables_data(soup)
        extractor = HtmlExtractor(driver.page_source)
        extracted_data = extractor.extract_and_save_data()
        processed_data = extractor.serialize_text_and_links()

        raw_data = RawData.objects.create(
            url_id=url_id,
            tables_data=tables_data,
            raw_data=processed_data,
            raw_json=extracted_data
        )

        return raw_data