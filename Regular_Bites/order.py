import bisect


class OrderedList:

    def __init__(self):
        self._numbers = []

    def add(self, num):
        bisect.insort(self._numbers, num)

    def __str__(self):
        return ', '.join(str(num) for num in self._numbers)


order = OrderedList()
order.add(10)
print(order)  # __str__ already provided
order.add(9)
print(order)
order.add(16)
print(order)
order.add(2)
print(order)
order.add(7)
order.add(1)
order.add(5)
print(order)
