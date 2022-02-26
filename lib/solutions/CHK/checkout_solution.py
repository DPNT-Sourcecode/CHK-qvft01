

# noinspection PyUnusedLocal
# skus = unicode string

from itertools import groupby

from enum import Enum

class Offers(Enum):
    BUY_3A_FOR_130 = '3A for 130',
    BUY_2A_FOR_45 = '2B for 45',



STOCK_LIST_BY_SKUS = (
        ('A', 50, '3A for 130'),
        ('B', 30, '2B for 45'),
        ('C', 20, None),
        ('D', 15, None)
    )

def get_discount_factor(discount_type: str):
    if discount_type == Offers.BUY_3A_FOR_130.value[0]:
        # Hard coded for now
        return 3, 30
    
    if discount_type == Offers.BUY_2A_FOR_45.value[0]:
        return 2, 15

    return None, 0


def apply_discount_factor(stock_item: STOCK_LIST_BY_SKUS, index: int):
    discount_factor, discounted_price = get_discount_factor(stock_item[2])
    counter = index + 1

    if discount_factor:
        if counter % discount_factor == 0:
            return discounted_price
        else:
            return stock_item[1]
    else:
        return stock_item[1]

def validate_input(skus):
    for sku in skus:
        for _, sku_code in enumerate(list(sku)):
            if sku_code not in ['A', 'B', 'C', 'D']:
                raise Exception("Invalid input detected")
    
    return True







class ShoppingCart:

    def __init__(self):
        self.products = {
            'A': {
                'price': 50,
                'quantity': 0,
            },
            'B': {
                'price': 30,
                'quantity': 0,
            },
            'C': {
                'price': 20,
                'quantity': 0,
            },
            'D': {
                'price': 15,
                'quantity': 0,
            }
        }

        self.discount_list = {
            'A': {
                'rule': 3,
                'discount_percent': 60,
            },
            'B': {
                'rule': 2,
                'discount_percent': 50,
            }
        }

        self.total = 0

        self.shopping_cart = {}

    def add_item(self, item):
        product = self.products[item]
        product['quantity'] += 1

        self.shopping_cart.update({ item: product })

        self._apply_discount(product, item)

    
    def _apply_discount(self, product, item):
        get_discount_for_product = self.discount_list[item]
        if product['quantity'] % get_discount_for_product['rule'] == 0:
            percentage = get_discount_for_product['discount_percent']
            
            if percentage:
                discount = int((product['price'] * percentage) / 100)
                self.total += discount

        else:
            self.total += product['price'] * 1

    

class InvalidInputException(Exception):
    pass

    

def checkout(skus: str):
    """
    Parameters
    ----------

    skus: str
        String containing list of sku's

    
    Returns
    -------

    int
        Returns int price
    """

    try:
        cart = ShoppingCart()
        allowed_input_values = ["".join(key) for key in cart.products.keys()]

        if not all(allowed_string in allowed_input_values for allowed_string in skus):
            raise InvalidInputException("Invalid input provided")    
        
        incoming_skus = ["".join(group) for _, group in groupby(sorted(skus))]    

        for sublist in incoming_skus:
            for _, item in enumerate(sublist):
                cart.add_item(item)

        return cart.total
    except (Exception, InvalidInputException) as e:
        breakpoint()
        return -1





