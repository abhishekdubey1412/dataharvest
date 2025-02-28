from bs4 import BeautifulSoup
from core.models.raw_data import create_raw_data

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
    def get_cleaned_soup(soup):
        tags_to_remove = [
            "header", "footer", "script", "style", "noscript", "nav", "iframe", "table",
            "br", "hr", "input", "svg", "aside", "button", "link", "meta", "picture", 
            "source", "object", "embed", "param", "canvas", "map", "area", "img", "i"
        ]

        for tags in tags_to_remove:
            for tag in soup.find_all(tags):
                tag.decompose()
        
        for pagination in soup.find_all(class_=lambda x: x is not None and isinstance(x, str) and "pagination" in x.lower()):
            pagination.decompose()

        for tag in soup.find_all(True):
            if tag.text.strip() == "" or tag.text.strip() ==  None:
                tag.decompose()
        
        for tag in soup.find_all(True):
            for attribute in ['onload', 'onclick', 'style']:
                del tag[attribute]

        return soup

    @staticmethod
    def get_cleaned_data(soup):
        """Recursively extract nested tags into key-value pairs, handling special <a> links."""
        data = {}
        if not soup:
            return data
        
        for child in soup.find_all(recursive=False):
            child_key = child.name
            
            if child_key == "a" and child.has_attr("href"):
                href = child["href"]
                text = child.get_text(strip=True)
                if href.startswith(("mailto:", "tel:", "ph:")):
                    value = {"text": text, "href": href}
                else:
                    value = text
            elif not child.find():  # Leaf node (no nested tags)
                value = child.get_text(strip=True)
            else:
                value = DataExtracted.get_cleaned_data(child)

            if child_key in data:
                if isinstance(data[child_key], list):
                    data[child_key].append(value)
                else:
                    data[child_key] = [data[child_key], value]
            else:
                data[child_key] = value if value else None

        # Filter out None values
        return {k: v for k, v in data.items() if v is not None}
    
    @staticmethod
    def extract_data(driver):
        soup = BeautifulSoup(driver.page_source, "html.parser")
        tables_data = DataExtracted.get_tables_data(soup)
        cleaned_soup = DataExtracted.get_cleaned_soup(soup.find("body"))
        get_cleaned_data = DataExtracted.get_cleaned_data(cleaned_soup)
        create_raw_data(url=driver.current_url, data={"tables": tables_data, "get_cleaned_data": get_cleaned_data})