def get_users(passwd: str) -> dict:
    """Split password output by newline,
      extract user and name (1st and 5th columns),
      strip trailing commas from name,
      replace multiple commas in name with a single space
      return dict of keys = user, values = name.
    """
    details = passwd.strip()
    lst = details.split("\n")
    user_details = dict()
    for item in lst:
        seq = item.split('/')
        user_ext = seq[0]
        user, *_, name, rest = user_ext.split(':')
        name = ' '.join(list(filter(None, name.split(','))))
        if not name:
            name = 'unknown'
        user_details.setdefault(user, name)
    return user_details
