def fib_num(n):
   if n<=0:
      print("Fibonacci can't be computed")
   elif n==1:
      return 0
   elif n==2:
      return 1
   else:
      return fib_num(n-1)+fib_num(n-2)
