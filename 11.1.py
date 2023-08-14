fs = []

def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num

def factorial_list(n):
    c = 1
    for i in range (1, n+1):
        c *= i
        fs.append(c)


num = int(input("Введите число: "))
num = factorial(num)
print(num)
factorial_list(num)
fs.sort(reverse=True)
print(fs)       
        
