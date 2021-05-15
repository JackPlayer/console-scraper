def is_in_stock(res_obj):
    selector = '#dwfrm_product_addtocart_d0cokuznmets > fieldset > div.availability > p.availability.primary-msg.alert-msg'
    stock = res_obj.find(selector, first=True).text
    if stock == 'Out of Stock':
        return False
    return True

def get_price(res_obj):
    selector = '#pdpMain > div > div.product-container > div.product-details > div.product-pricing > h3'
    return res_obj.find(selector, first=True).text

def parse(res_obj):
    information = {
        'price': get_price(res_obj),
        'in_stock': is_in_stock(res_obj),
        'retailer': 'londondrugs'
    }
    return information