

# noinspection PyUnusedLocal
# skus = unicode string

STOCK_LIST_BY_SKUS = (
        ('A', 50, '3A for 130'),
        ('B', 30, '2B for 45'),
        ('C', 20, None),
        ('D', 15, None)
    )
    

def checkout(skus):
    price = 0
    skus_to_list = skus.split(',')

    for sku in skus_to_list:
        for stock_item in STOCK_LIST_BY_SKUS:
            label = stock_item[0]
            price += 
            breakpoint()
    raise NotImplementedError()



