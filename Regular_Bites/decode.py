import base64
import csv
from typing import List  # will remove with 3.9


def get_credit_cards(data: bytes) -> List[str]:
    """Decode the base64 encoded data which gives you a csv
    of "first_name,last_name,credit_card", from which you have
    to extract the credit card numbers.
    """
    details = base64.b64decode(data).decode()
    return [row["credit_card"] for row in csv.DictReader(details.splitlines())]


csv2 = b"""
Zmlyc3RfbmFtZSxsYXN0X25hbWUsY3JlZGl0X2NhcmQKTWVsaXNlbmRhLENyb3NmaWVsZC
wzNTg0MTY2NjgwNjE3MjAzCkxpYW5hLFNlbnRlbiw2NzYyMDgzNDMwNjM3MjU2NwpEZWVy
ZHJlLE1hdGNoYW0sMzU0ODI2OTgzOTkwNDUzMwpDYXNzZXksQmxleW1hbiwzNzQ2MjI3MD
Y3OTU3OTUKRG9kaSxMZXlkb24sMzU3NTkwNDg5MzQyMjc5MgpDb25ub3IsQmVybmFyZG90
dGksMzUyODYwMjY2NDk0NDkxNQpMZXdpc3MsQnJhbnNieSw1MTAwMTM4NTUzNDQ2OTQ1Ck
p1bmllLFRhbXNldHQsMzU3MDUwNDQwNDkzMzMwNgpDb3JpbGxhLEhvZiwzMDI4NzM1NDg2
NTcyNApCb2JiaSxGZnJlbmNoLDM1NjYxMTA3Njc2NTcxNTUK
"""

print(get_credit_cards(csv2))
