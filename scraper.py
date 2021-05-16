import parsers
import urls

from requests_html import HTMLSession

def match_retailer_parser(retailer):
    if retailer == 'bestbuy':
        return parsers.bestbuy
    if retailer == 'newegg':
        return parsers.newegg
    if retailer == 'canadacomputers':
        return parsers.canadacomputers
    return -1

def get_info_from_parser(session, retailer, url):
    parser = match_retailer_parser(retailer)
    if (parser == -1):
        return
    response = session.get(url)
    response.html.render(timeout=25, sleep=10)
    info = parser.parse(response)
    return info


def get_info_all_retailers(url_dict, console_type):
    console_dict = url_dict[console_type]
    session = HTMLSession()
    info_list = []
    for retailer in console_dict:
        info = get_info_from_parser(session, retailer, url=console_dict[retailer])
        if info == -1:
            continue        
        info_list.append(info)
    return info_list

def main():
    URLS = urls.parse_urls.get_urls('./urls/data/')
    info_list = get_info_all_retailers(URLS, 'XBOX_SERIES_X_URLS')

    print(info_list)
if __name__ == "__main__":
   main()