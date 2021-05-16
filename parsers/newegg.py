def get_price(res_obj):
    selector = '.price-current'
    price = res_obj.html.find(selector, first=True)
    return price.text

def is_in_stock(res_obj):
    selector = '#app > div.page-content > div.page-section > div > div > div.row-side > div.product-buy-box > div.product-flag > div > div > span'
    stock = res_obj.html.find(selector, first=True)

    if stock == None: 
        return True

    if stock.text == 'OUT OF STOCK':
        return False
        
    return True

def parse(res_obj):
    information = {
        'price': get_price(res_obj),
        'in_stock': is_in_stock(res_obj),
        'retailer': 'newegg'
    }
    return information
