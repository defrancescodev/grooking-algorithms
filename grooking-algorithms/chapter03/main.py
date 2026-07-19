def regressive_count(i):
    print(i)
    if i <= 1:
        return
    regressive_count(i - 1)

def factorial(i):
    if i <= 1:
        return 1
    return i * factorial(i - 1)

regressive_count(10)
print(factorial(5))