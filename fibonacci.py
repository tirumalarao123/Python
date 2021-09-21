def fibo(n):
    if (n<=1):
        return n
    else:
        return (fib0(n-1)+fib0(n-2))

n=int(input("Enter no of terms"))
if n<0:
    print("Enter positive number")
else:
    print("Fibonacci sequence")
    for i in range(n):
         print (fibo(i))
