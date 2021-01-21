def fizzbuzz(num):
    lst = []
    if num % 3 == 0:
        lst.append('Fizz')
    if num % 5 == 0:
        lst.append('Buzz')
    return ' '.join(lst) or num


lst = []
for x in range(1, 101):
    lst.append(fizzbuzz(x))
print(lst)
