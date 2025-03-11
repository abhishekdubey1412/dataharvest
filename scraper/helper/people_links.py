from bs4 import BeautifulSoup
from collections import Counter
from urllib.parse import urlparse, urljoin

class PeopleLinkScraper:
    PEOPLE_KEYWORDS = {
        'team', 'teams', 'leadership', 'staff', 'employee', 'employees',
        'people', 'personnel', 'member', 'members', 'group', 'crew',
        'management', 'director', 'executive', 'contact', 'leaders'
    }

    def __init__(self, driver):
        self.driver = driver
        self.url = driver.current_url
        self.html = driver.page_source
        self.base_domain = urlparse(self.url).netloc
        self.filtered_links = set()
        self.repeated_paths = []

    def extract_and_filter_links(self):
        """Extract and filter links based on people-related keywords and domain matching."""
        print("\n🔍 Extracting and filtering links from the page source....")
        
        soup = BeautifulSoup(self.html, "html.parser")
        all_links = {
            urljoin(self.url, a["href"].strip()) for a in soup.find_all("a", href=True)
        }

        domain_links = {
            link for link in all_links
            if urlparse(link).netloc == self.base_domain and "page" not in urlparse(link).query
        }

        self.filtered_links = {
            link for link in domain_links if any(keyword in link.lower() for keyword in self.PEOPLE_KEYWORDS)
        }

        print(f"\n🔹 Total Links Found: {len(all_links)}")
        print(f"🔹 Links Matching Base Domain ({self.base_domain}): {len(domain_links)} (Excluding pagination links)")
        print(f"🔹 People-related Links: {len(self.filtered_links)}")

        print("\n🟢 Filtered People-related Links:")
        for link in self.filtered_links:
            print(f"   - {link}")
        
        return self.filtered_links

    def get_repeated_base_paths(self):
        """Find commonly occurring base paths to prioritize relevant pages."""
        path_counts = Counter()
        
        for url in self.filtered_links:
            parsed = urlparse(url)
            path_parts = parsed.path.rstrip('/').split('/')
            
            if len(path_parts) > 1:
                base_path = f'{parsed.scheme}://{parsed.netloc}' + '/'.join(path_parts[:-1]) + '/'
                path_counts[base_path] += 1

        self.repeated_paths = [path for path, count in path_counts.items() if count > 1] or list(self.filtered_links)
        return self.repeated_paths
    
    def process(self):
        """Run all steps of the scraping process."""
        self.extract_and_filter_links()
        repeated_paths = self.get_repeated_base_paths()
        
        print("\n🟠 Repeated Base Paths (Common URL Structures):")
        if repeated_paths:
            for path in repeated_paths:
                print(f"   - {path}")
        else:
            print("   ❌ No repeated base paths found.")
        
        return list(repeated_paths)