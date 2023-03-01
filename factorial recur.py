def factorial(n):
    if n==1:
        return 1
    else:
        x=n*factorial(n-1)
        return x
x=factorial(5)
print(x)