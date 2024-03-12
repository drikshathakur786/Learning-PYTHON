# If number divisible by 3 dont print that number instead print FIZZ
# If divisible by 5 print BUZZ
# If by both 3 and 5 print FIZZBUZZ
# If none condition then print number only
# Using while loop

n = 1

while n<=50: 
    if n%3==0 and n%5==0:
        print("FIZZBUZZ")
    elif n%3==0:
        print("FIZZ")
    elif n%5==0:
        print("BUZZ")
    else:
        print(n)
    n = n+1
