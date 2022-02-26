

# noinspection PyUnusedLocal
# skus = unicode string

STOCK_LIST_BY_SKUS = (
        ('A', 50, '3A for 130'),
        ('B', 30, '2B for 45'),
        ('C', 20, None),
        ('D', 15, None)
    )
    

def checkout(skus):
    skus_to_list = skus.split(',')
    t = STOCK_LIST_BY_SKUS

    for sku in skus_to_list:
        item_price = [item for item in t]
    breakpoint()
    raise NotImplementedError()


