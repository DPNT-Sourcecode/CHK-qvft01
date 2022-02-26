

# noinspection PyUnusedLocal
# skus = unicode string

from itertools import groupby

class ShoppingCart:

    """
    Shopping cart class for handling interactions for exercise

    Arguments:
    ---------

    None

    Methods
    -------

    add_item(item: str): None    
    """

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

    def add_item(self, item: str):
        product = self.products[item]
        product['quantity'] += 1

        self.shopping_cart.update({ item: product })

        self._apply_discount(product, item)

    
    def _apply_discount(self, product, item):
        get_discount_for_product = self.discount_list.get(item, None)

        if get_discount_for_product:
            if product['quantity'] % get_discount_for_product['rule'] == 0:
                percentage = get_discount_for_product['discount_percent']
                
                if percentage:
                    discount = int((product['price'] * percentage) / 100)
                    self.total += discount

            else:
                self.total += product['price'] * 1
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






