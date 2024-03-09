age = int(input("Enter your age:"))

# double == for comparing two things

#if age>18:
#    print('You can vote')
# no need to apply any condition for else

#if age>18:
#    print('You can vote')
#else:
#    print('You can not vote')

# Correct this code as for age 25 output is coming Teen
if age>7:
    print('Teen')
elif age<7:
    print('Child')
elif age>18:
    print('Young')
else:
    print('You are alien') 

# Modified code:
if age > 18:
    print('Young')
elif age >= 13:
    print('Teen')
elif age < 7:
    print('Child')
else:
    print('You are an alien')

# Python operators:
# + Addition
print(50+50)
# - Subtraction
print(50-50)
# * Multiplication
print(50*50)
# / Divide
print(50/50)
# % Modulus (Remainder value)
print(50%50)
# ** Exponentiation (For power)
print(50**2)
# // Float division (Decimal value)
print(50//50)







