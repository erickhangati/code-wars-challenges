"""
ATMs allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.
"""


def validate_pin(pin):
    """
    Check if pin is 4 or 6 digits
    :param pin: type - str
    :return: type - boolean
    """
    return len(pin) == 4 or len(pin) == 6 if pin.isdigit() else False


result = validate_pin("1234")
print(result)
