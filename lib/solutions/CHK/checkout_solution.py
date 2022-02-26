

# noinspection PyUnusedLocal
# skus = unicode string

from itertools import groupby

class LoadingFactors:
    def __init__(self):
        self.discount_list = {
            '3A': {
                'discount_percent': 60,
                'shared_products': None,
            },
            '5A': {
                'discount_percent': 25,
                'shared_products': None,
            },
            '2B': {
                'rule': 2,
                'discount_percent': 50,
                'shared_products': None,
            },
            '2E': {
                'rule': 2,
                'discount_percent': None,
                'shared_products': {
                    'B': {
                        'action': '1 free'
                    }
                }
            }
        }

    def process_A_discounts(self, product, product_list=None):
        if product['quantity'] == 3:
            get_discount_for_product = g


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
                'discounted_items': 0,
            },
            'B': {
                'price': 30,
                'quantity': 0,
                'discounted_items': 0,
            },
            'C': {
                'price': 20,
                'quantity': 0,
                'discounted_items': 0,
            },
            'D': {
                'price': 15,
                'quantity': 0,
                'discounted_items': 0,
            },
            'E': {
                'price': 40,
                'quantity': 0,
                'discounted_items': 0,
            }
        }

        self.total = 0

        self.shopping_cart = {}

    def add_item(self, item: str):
        product = self.products[item]
        product['quantity'] += 1

        self.shopping_cart.update({ item: product })

        self._apply_discount(product, item)

    
    def _apply_discount(self, product: object, item: str) -> None:
        discounted_count = product['discounted_items']
        breakpoint()
        get_discount_for_product = self.discount_list.get(f'{discounted_count}{item}', None)

        if get_discount_for_product:
            if product['quantity'] % get_discount_for_product['rule'] == 0:
                percentage = get_discount_for_product['discount_percent']
                shared_products = get_discount_for_product['shared_products']
                
                if percentage:
                    discount = int((product['price'] * percentage) / 100)
                    self.total += discount

                if shared_products:
                    self._apply_shared_discount(product, shared_products)

                product.update({ **product, 'discounted_items': 0 })

            else:
                self.total += product['price'] * 1
                product.update({ **product, 'discounted_items': discounted_count + 1 })
        else:
            self.total += product['price'] * 1
            product.update({ **product, 'discounted_items': discounted_count + 1 })

    def _apply_shared_discount(self, product, shared_products):
        shared_products_keys = shared_products.keys()
        for shared_item in shared_products_keys:
            try:
                target_shared_product = self.shopping_cart[shared_item]
                if shared_products[shared_item]['action'] == '1 free':
                    self.total += product['price']
                    self.total -= target_shared_product['price']
            except KeyError:
                self.total += product['price']



    

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
        return -1


