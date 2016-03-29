"""
Collection of common functions to be used throughout the project.
"""


def correct_type(obj, obj_type):
    """Raises TypeError if object is not type of object_type

    :param obj: object to be checked
    :param obj_type: object that instance will be checked against
    :return: None
    """
    if not isinstance(obj, obj_type):
        raise TypeError("Expected {0}, got {1} of type {2}"
                        .format(obj_type, obj, type(obj)))
