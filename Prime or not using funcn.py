# Checking prime or not using function
def prime(num):
    if num==2:
        return True
    for i in range(2,num):
        if num%i==0:
            return False
    return True
num = int(input('Enter a number:'))
print(prime(num))



