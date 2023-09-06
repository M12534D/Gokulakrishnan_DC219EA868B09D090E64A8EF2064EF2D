# 1.1 Implement a recursive function to calculate the factorial of a given number.
def factorial(n):
  if n == 1 or n == 0:
    return 1
  else:
    return n * factorial(n - 1)


num = int(input("Entet the number : "))
print('The factorial of {} is {}'.format(num, factorial(num)))