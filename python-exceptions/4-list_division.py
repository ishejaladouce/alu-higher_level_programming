#!/usr/bin/python3
"""4-list_division
Divide elements of two lists with exception handling and finally block.
"""


def list_division(my_list_1, my_list_2, list_length):
    """Divide elements element-wise, handling exceptions with try/except/finally."""
    result = []
    for i in range(list_length):
        try:
            val1 = my_list_1[i]
            val2 = my_list_2[i]

            if not (isinstance(val1, (int, float)) and isinstance(val2, (int, float))):
                raise TypeError("wrong type")

            division = val1 / val2
        except IndexError:
            print("out of range")
            division = 0
        except ZeroDivisionError:
            print("division by 0")
            division = 0
        except TypeError:
            print("wrong type")
            division = 0
        finally:
            result.append(division)
    return result
