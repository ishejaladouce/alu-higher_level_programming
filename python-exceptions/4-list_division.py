#!/usr/bin/python3
"""4-list_division
Divide elements of two lists index by index with safe error handling.
"""


def list_division(my_list_1, my_list_2, list_length):
    """Divide items of two lists up to list_length and return results list.

    Prints:
        - wrong type       if an element is not int or float
        - division by 0    if denominator is zero
        - out of range     if an index is missing in either list
    """
    result = []
    for i in range(list_length):
        try:
            num1 = my_list_1[i]
            num2 = my_list_2[i]

            if not isinstance(num1, (int, float)) \
                    or not isinstance(num2, (int, float)):
                raise TypeError

            division = num1 / num2
        except TypeError:
            print("wrong type")
            division = 0
        except ZeroDivisionError:
            print("division by 0")
            division = 0
        except IndexError:
            print("out of range")
            division = 0
        finally:
            result.append(division)
    return result
