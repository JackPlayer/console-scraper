"""
Parser for newegg product pages
"""

def get_price(res_obj):
    """Gets the price of an item from the newegg website 

    Args:
        res_obj: requests_html response object of a newegg product page

    Returns:
        string: The price of the product
    """
    selector = '.price-current'
    price = res_obj.html.find(selector, first=True)
    return price.text

def is_in_stock(res_obj):
    """Checks if a product is in stock 

    Args:
        res_obj: requests_html response object of a newegg product page

    Returns:
        bool: Is the product in stock
    """
    selector = '#app > div.page-content > div.page-section > div > div > div.row-side > div.product-buy-box > div.product-flag > div > div > span'
    stock = res_obj.html.find(selector, first=True)

    if stock == None: 
        return True

    if stock.text == 'OUT OF STOCK':
        return False
        
    return True

def parse(res_obj):
    """Parses a newegg product page into information dictionary

    Args:
        res_obj: requests_html response object of a newegg product page

    Returns:
        dict: With price, stock status and the retailer
    """
    information = {
        'price': get_price(res_obj),
        'in_stock': is_in_stock(res_obj),
        'retailer': 'newegg'
    }
    return information
