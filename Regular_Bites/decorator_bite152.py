from functools import wraps

DEFAULT_TEXT = ('Subscribe to our blog (sidebar) to periodically get '
                'new PyBites Code Challenges (PCCs) in your inbox')
DOT = '.'


def strip_range(start, end):
    if start < 0:
        start = 0
    if end < 0:
        end = 0

    def real_decorator(func):
        @wraps(func)
        def wrapper(text):
            cut = text[start:end]
            dot = DOT * len(cut)
            text = text.replace(cut, dot)
            return func(text)
        return wrapper
    return real_decorator


@strip_range(0, -1)
def get_text(text):
    return text


print(get_text('Welcome to PyBites'))
