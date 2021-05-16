def is_in_stock(res_obj):
    selector = '#pi-form > div.col-12.py-2 > div.pi-prod-availability > span:nth-child(2)'
    stock = res_obj.html.find(selector, first=True).text

    if stock == 'Not Available Online':
        return False
    return True

def get_price(res_obj):
    selector = 'body > div.page-product_info.container.pt-2.overflow-hidden > div:nth-child(1) > div > div:nth-child(3) > div:nth-child(2) > div.row.mt-2 > div:nth-child(2) > div.col-auto.col-md-12.order-2.order-md-1 > span > strong'
    price = res_obj.html.find(selector, first=True)
    
    return price.text

def parse(res_obj):
    information = {
        'price': get_price(res_obj),
        'in_stock': is_in_stock(res_obj),
        'retailer': 'canadacomputers'
    }
    return information