# You have a nested list
#marks = {
#    [85, 90, 78, 88, 92, 'Alice'],
#    [79, 82, 88, 91, 87, 'Bob'],
#    [92, 88, 85, 90, 86, 'Charlie'],
#    [80, 84, 87, 89, 82, 'David'],
#    [86, 87, 89, 92, 85, 'Eva'],
#    [88, 90, 84, 92, 87, 'Fiona']
#}

# instead of numbers calculated percentage and print it with name

# Output list should be like 
    
# Output = {
#    [92,'Alice'],
#    [78,'Bob'],
#    [82,'Charlie'],
#    [87,'David'],
#    [93,'Eva'],
#    [97,'Fiona']
#}

marks = [
    [85, 90, 78, 88, 92, 'Alice'],
    [79, 82, 88, 91, 87, 'Bob'],
    [92, 88, 85, 90, 86, 'Charlie'],
    [80, 84, 87, 89, 82, 'David'],
    [86, 87, 89, 92, 85, 'Eva'],
    [88, 90, 84, 92, 87, 'Fiona']
]

output = []
for student_marks in marks:
    percentage = sum(student_marks[:-1]) / len(student_marks[:-1])
    output.append([round(percentage), student_marks[-1]])  

print("Output list:")
print(output)

#for i in range(6):
#    print(marks)
