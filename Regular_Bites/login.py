from functools import wraps

known_users = ['bob', 'julian', 'mike', 'carmen', 'sue']
loggedin_users = ['mike', 'sue']


def login_required(func):
    @wraps(func)
    def iam_awrapper(user, *args, **kwargs):
        """ Wrapper Function """
        if user not in known_users:
            return "please create an account"
        elif user not in loggedin_users:
            return "please login"
        else:
            return func(user, *args, **kwargs)

    return iam_awrapper


@login_required
def welcome(user):
    '''Return a welcome message if logged in'''
    return f'welcome back {user}'


print(welcome('sue'))
print(welcome.__doc__)
