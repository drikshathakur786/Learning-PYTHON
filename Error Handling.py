# Example
#num1 = 10
#num2 = 30
#result = num1 + num2
#print(result)

# if we write: num2 = "30" then ERROR
try:
    num1 = 10
    num2 = 30
# if num2='30' then output will be Kuch bura ho gya
    result = num1 + num2
    print(result)
except:
    print('Kuch bura ho gya')

# Zero division error
# Type Error
# Value Error
# Syntax Error
    
num3 = 10
num4 = 0
result = num3/num4

except ZeroDivisionError:
print('You are dividing a number with 0')

except TypeError:
print('You can not Divide a Text with Number')

except:
print('Something bad happened')

# if your code works then only else block works
else:
print('I am in else block')





