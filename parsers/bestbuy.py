"""
Parser for bestbuy product pages
"""

def get_price(res_obj):
    """Gets the price of an item from the bestbuy website 

    Args:
        res_obj: requests_html response object of a bestbuy product page

    Returns:
        string: The price of the product
    """
    selector = '#root > div > div.x-page-content.container_3Sp8P > div.x-product-detail-page > div.row_1mOdd > div.col-xs-12_198le.col-sm-6_1okfB.col-md-4_3LwCi.collapseColContainer_2eCPT > div.pricingContainer_9GyCd > div > span > div'
    price = res_obj.html.find(selector, first=True)
    return price.text

def is_in_stock(res_obj):
    """Checks if a product is in stock 

    Args:
        res_obj: requests_html response object of a bestbuy product page

    Returns:
        bool: Is the product in stock
    """
    selector = '#root > div > div.x-page-content.container_3Sp8P > div.x-product-detail-page > div.row_1mOdd > div.col-xs-12_198le.col-sm-6_1okfB.col-md-4_3LwCi.collapseColContainer_2eCPT > div:nth-child(6) > div > div > div > p > span'
    stock = res_obj.html.find(selector, first=True)

    if stock.text == 'Coming soon' or stock.text == 'Sold out online':
        return False
    return True

def format_price(raw_price):
    """Formats the price to account for bestbuy's raw price format

    Args:
        raw_price(string): Bestbuy's price format (ex: $5999 is $59.99)

    Returns:
        string: The formatted price
    """
    formatted_price = raw_price[:len(raw_price) - 2] + "." + raw_price[len(raw_price) - 2:]
    return formatted_price

def parse(res_obj):
    """Parses a bestbuy product page into information dictionary

    Args:
        res_obj: requests_html response object of a bestbuy product page

    Returns:
        dict: With price, stock status and the retailer
    """
    information = {
        'price': format_price(get_price(res_obj)),
        'in_stock': is_in_stock(res_obj),
        'retailer': 'bestbuy'
    }
    return information
