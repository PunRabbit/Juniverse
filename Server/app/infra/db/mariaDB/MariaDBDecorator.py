def check_connection(func):
    """
    Rapping for Check Connection when Target Get Lost Connection.
    :param func:
    :return: func
    """
    def wrapper(*args, **kwargs):
        if args[0].connection is None:
            args[0].create_connection()
            result = func(*args, **kwargs)
            return result
        else:
            result = func(*args, **kwargs)
            return result
    return wrapper

