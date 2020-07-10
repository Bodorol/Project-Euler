def isPrime(num):
    if (num % 2 == 0 and num != 2 or num == 1):
        return False
    for i in range(3, (num+1)//2, 2):
        if (num % i == 0):
         return False
    return True;

count = 1
i = 1
while (count < 10001):
    if (isPrime(i)):
        count += 1
        print("Num:", i, "| Is Prime:", isPrime(i), "| Count:", count)
    i += 2
