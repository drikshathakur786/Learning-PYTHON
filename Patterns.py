# Patterns

'''
*
**
***
****
*****
'''

# Using for loop
for i in range(1,6):
    for j in range(i):
        print("*",end='')
    print()


# Modify and print:
'''
1
22
333
4444
55555
'''
for i in range(1,6):
    for j in range(i):
        print(i, end='')
# If want to print 0. Then replace i by i-1
    print()

'''
    *
   **
  ***
 ****
*****
'''

for i in range(1,6):
     for j in range(5-i):
         print(' ',end='')
     for j in range(i):
         print('*',end='')
     print()

'''
    *
   ***
  *****
 *******
*********
'''

for i in range(1,6):
     for j in range(5-i):
         print(' ',end='')
     for j in range(i):
# add a space after *
         print('* ',end='')
     print()

# Practice:
'''
    ******
   ******
  ******
 ******
******
'''
n = 5

for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for k in range(n):
        print("*", end="")
    print()

