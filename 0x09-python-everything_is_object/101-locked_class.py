class LockedClass:
    """
    This class defines a locked class that restricts the creation of instance attributes,
    except for 'first_name'
    """
    __slots__ = ("first_name",)