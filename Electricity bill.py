# Generate electricity bill according to following instructions
# 350 units
# output bill should be Rs.2000
# first 100 units free no charge
# second 100 units Rs 5/unit
# third 100 or above Rs 10/unit

units = int(input('Enter units:'))
if units<=100:
    bill= 0 
elif units<=200:
    bill= (units-100)*5
else:
    bill= 100*5+(units-200)*10 
print("Electricity bill:",bill)


