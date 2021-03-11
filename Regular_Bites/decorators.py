from functools import wraps


def make_html(element):
    def real_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return f'<{element}>{func(*args, **kwargs)}</{element}>'
        return wrapper
    return real_decorator


@make_html('p')
@make_html('strong')
def get_text(text='I code with PyBites'):
    return text


print(get_text())
