#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def natural(n):
   i = 2
   result = []
   while i * i <= n:
       while n % i == 0:
           result.append(i)
           n = n // i
       i = i + 1
   if n > 1:
       result.append(n)
   return result
n = int(input())
print(natural(n))