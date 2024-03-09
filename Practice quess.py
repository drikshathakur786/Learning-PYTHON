# PROGRAM 1: Write a program to find vowels and consonants
x = input('Enter:')
vowels= ['a','e','i','o','u','A','E','I','O','U']  
if x in vowels: 
    print("Vowel") 
else:
    print("Consonant") 

# When u enter a word the output should not be consonant show error and print pls enter a char
# if entered 2 show output pls enter a valid char only

# PROGRAM 2: Write a python program to check if a word is palindrome or not 
x = input("Enter: ")
if x==x[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

# PROGRAM 3: Input name and Bp of employee:
# calculate gross pay and net pay
# grosspay = bp+da+hra-pf
# pf =12% of bp
#  (To calculate percentage of any number:
#    Ex if bp is 200 then 12% of bp will be: 200*12/100)
# Hra is 20% of bp but maximum can be 2000 only
# da is 20% of bp for bp<3lac
# otherwise
# da is 30% of bp
# netpay= grosspay-pf
name= input("Enter employee name: ")
bp= float(input("Enter basic pay of employee:"))
pf= 0.12*bp
if bp<300000:
    da= 0.2*bp
else:
    da= 0.3*bp
hra= min(0.2*bp,2000)
grosspay= bp+da+hra-pf
netpay= grosspay-pf
print("Employee Name:",name)
print("Basic Pay:",bp)
print("DA:",da)
print("HRA:",hra)
print("PF:",pf)
print("Gross Pay:",grosspay)
print("Net Pay:",netpay)


