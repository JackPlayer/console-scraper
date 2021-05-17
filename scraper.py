import parsers
import urls
import interface

from requests_html import HTMLSession

RESPONSE_TIMEOUT = 20
RESPONSE_SLEEP = 10

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
    response.html.render(timeout=RESPONSE_TIMEOUT, sleep=RESPONSE_SLEEP)
    info = parser.parse(response)
    return info


def get_info_all_retailers(url_dict, console_type):
    console_dict = url_dict[console_type]
    session = HTMLSession()
    info_list = []
    for retailer in console_dict:
        try:
            info = get_info_from_parser(session, retailer, url=console_dict[retailer])
            if info == -1:
                continue        
            info_list.append(info)
        except:
            continue
    return info_list

def get_info_all_consoles(url_dict):
    for console in url_dict:
        info_list = get_info_all_retailers(url_dict, console)
        interface.ui.print_table(console, info_list)
        
def main():
    URLS = urls.parse_urls.get_urls('./urls/data/')
    get_info_all_consoles(URLS)

if __name__ == "__main__":
   main()