import parsers
import urls

from requests_html import HTMLSession

def main():
    URLS = urls.parse_urls.get_urls('./urls/data/')
    session = HTMLSession()
    response = session.get(URLS['XBOX_SERIES_S_URLS']['newegg'])
    response.html.render(timeout=20, sleep=7)

    info = parsers.newegg.parse(response)
    print(info)
if __name__ == "__main__":
   main()