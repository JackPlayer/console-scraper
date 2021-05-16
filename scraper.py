import parsers
import urls

from requests_html import HTMLSession

# TODO: Implement this function
def get_page_content(session, url):
    response = session.get(url)
    return response

# TODO: Implement this function
def get_info(content, parser):
    pass

def main():
    URLS = urls.parse_urls.get_urls('./urls/data/')
    
    session = HTMLSession()
    response = session.get(URLS['XBOX_SERIES_S_URLS'][1]['url'])
    available = response.html.find('html', first=True).text
    print(available)
if __name__ == "__main__":
   main()