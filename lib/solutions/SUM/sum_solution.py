# noinspection PyShadowingBuiltins,PyUnusedLocal

class ValidationError(Exception):
    pass

def validate_inputs_int(x, y):
    if isinstance(x, int)
    if 0 <= x <= 100 and 0 <= y <= 100:

def compute(x: int, y: int) -> int:
    """
    Compute method for allowing two numbers to be summed

    Parameters
    ----------
    x: int
        Must be a positive int and greater than 100
    x: int
        Must be a positive int and greater than 100

    Returns:
    --------

    int
        The summed value
    """

    if 0 <= x <= 100 and 0 <= y <= 100:
        return x + y
    
    raise NotImplementedError()


