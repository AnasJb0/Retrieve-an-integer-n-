n = int(input("Enter an integer n: "))
for num in range(2, n):
    prime = 1
    for i in range(2, num):
        if num % i == 0:
            prime = 0
            i = num - 1
    if prime == 1:
        print(num)