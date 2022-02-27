

# noinspection PyUnusedLocal
# skus = unicode string

from ast import Load
from itertools import groupby

class LoadingFactors:
    def __init__(self):
        self.discount_list = {
            '3A': {
                'discount': 20,
                'shared_products': None,
            },
            '5A': {
                'discount': 50,
                'shared_products': None,
            },
            '2B': {
                'rule': 2,
                'discount': 15,
                'shared_products': None,
            }
        }

    def process_A_discounts(self, product, product_list=None):
        quantity = product['quantity']

        if quantity % 3 == 0 and quantity < 5:
            loop_range = int(quantity / 3)

            for _ in range(loop_range):
                # do another
                get_discount_for_product = self.discount_list['3A']
                discount_to_apply = (product['price'] - get_discount_for_product['discount'])
                product['total_price'] += discount_to_apply
            return

        if (quantity - 5) % 3 == 0 and quantity > 5:
            loop_range = int(quantity / 3)

            get_discount_for_product = self.discount_list['3A']
            discount_to_apply = (product['price'] - get_discount_for_product['discount'])
            product['total_price'] += discount_to_apply
            return
            

        if quantity % 5 == 0:
            loop_range = int(quantity / 5)

            get_discount_for_product = self.discount_list['5A']
            discount_to_apply = get_discount_for_product['discount']
            product['total_price'] = 0
            new_total = product['price'] * quantity
            product['total_price'] = (new_total - (discount_to_apply * loop_range))
            return

        product['total_price'] += product['price'] * 1

    def process_B_discounts(self, product, product_list=None):
        if product['quantity'] == 2:
            get_discount_for_product = self.discount_list['2B']
            discount_to_apply = get_discount_for_product['discount']
            product['total_price'] = 0
            new_total = product['price'] * 2
            product['total_price'] = (new_total - discount_to_apply)
            return

        product['total_price'] += product['price']

    def process_C_discounts(self, product, product_list=None):
        product['total_price'] += product['price']

    def process_D_discounts(self, product, product_list=None):
        product['total_price'] += product['price']

    def process_E_discounts(self, product, product_list):
        if product['quantity'] == 2:
            if product_list['B']['quantity'] >= 1:
                product_list['B']['total_price'] -= product_list['B']['price']
            
            product['total_price'] += product['price']
            return

        product['total_price'] += product['price']


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
        loading_factors = LoadingFactors()
        self.products = {
            'A': {
                'price': 50,
                'quantity': 0,
                'total_price': 0,
                'loading_factor': loading_factors.process_A_discounts
            },
            'B': {
                'price': 30,
                'quantity': 0,
                'total_price': 0,
                'loading_factor': loading_factors.process_B_discounts
            },
            'C': {
                'price': 20,
                'quantity': 0,
                'total_price': 0,
                'loading_factor': loading_factors.process_C_discounts
            },
            'D': {
                'price': 15,
                'quantity': 0,
                'total_price': 0,
                'loading_factor': loading_factors.process_D_discounts
            },
            'E': {
                'price': 40,
                'quantity': 0,
                'total_price': 0,
                'loading_factor': loading_factors.process_E_discounts
            }
        }

        self.total = 0

        self.shopping_cart = {}

    def add_item(self, item: str):
        product = self.products[item]
        product['quantity'] += 1

        self.shopping_cart.update({ item: product })

        product['loading_factor'](product, self.products)
    

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

        
        for product in allowed_input_values:
            cart.total += cart.products[product]['total_price']

        return cart.total
    except (Exception, InvalidInputException) as e:
        return -1


