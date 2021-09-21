from textwrap import wrap
from itertools import zip_longest
COL_WIDTH = 20


def text_to_columns(text):
    """Split text (input arg) to columns, the amount of double
       newlines (\n\n) in text determines the amount of columns.
       Return a string with the column output like:
       line1\nline2\nline3\n ... etc ...
       See also the tests for more info."""
    paragraphs = text.split("\n\n")
    content = []
    for paragraph in paragraphs:
        content.append(wrap(paragraph, width=COL_WIDTH))
    lines = list(zip_longest(*content, fillvalue=''))
    lst = [' '.join(line) for line in lines]
    return "\n".join(lst)
