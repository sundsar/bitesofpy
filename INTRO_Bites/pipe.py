message = """Hello world!
We hope that you are learning a lot of Python.
Have fun with our Bites of Py.
Keep calm and code in Python!
Become a PyBites ninja!"""

def split_in_columns(message=message):
    wordlst = message.split('\n')
    pipe = '|'
    result = pipe.join(wordlst)
    return result

print(split_in_columns())
