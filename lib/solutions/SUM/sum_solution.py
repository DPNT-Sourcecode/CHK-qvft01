# noinspection PyShadowingBuiltins,PyUnusedLocal
import logging

class ValidationException(Exception):
    pass

def validate_inputs_int(x, y):
    if isinstance(x, int) and isinstance(y, int):
        if 0 <= x <= 100 and 0 <= y <= 100:
            return True

        raise ValidationException("Numbers are out of range, values must be a positive int >= to 100")
    
    raise ValidationException("Non-integer detected")

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

    try:

        validate_inputs_int(x, y)

        return x + y
    except ValidationException as validation_error:
        logging.info("Encountered validation error")
        logging.exception(validation_error)
        raise

