def is_in_stock(res_obj):
    selector = '#dwfrm_product_addtocart_d0cokuznmets > fieldset > div.availability > p.availability.primary-msg.alert-msg'
    stock = res_obj.html.find(selector, first=True).text
    print(stock)
    print("The stock is: " + stock)
    if stock == 'Out of Stock':
        return False
    return True

def get_price(res_obj):
    selector = '#pdpMain > div > div.product-container > div.product-details > div.product-pricing > h3'
    price = res_obj.text
    print("The price is: " + price)
    return 

def parse(res_obj):
    information = {
        'price': get_price(res_obj),
        'in_stock': is_in_stock(res_obj),
        'retailer': 'londondrugs'
    }
    return information