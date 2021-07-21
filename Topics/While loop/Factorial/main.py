number = int(input())
factorial = 1
while 1 <= number <= 100:
    factorial *= number
    number -= 1
print(factorial)
