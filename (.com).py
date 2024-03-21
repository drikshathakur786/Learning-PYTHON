students = [
    [85, 90, 78, 88, 92, 'Alice'],
    [79, 82, 88, 91, 87, 'Bob'],
    [92, 88, 85, 90, 86, 'Charlie'],
    [80, 84, 87, 89, 82, 'David'],
    [86, 87, 89, 92, 85, 'Eva'],
    [88, 90, 84, 92, 87, 'Fiona']
]

# Calculate percentage for each student and store in temp list
temp=[]
for i in range(6):
    marks= students[i][:-1]
    m1 = marks[0]
    m2 = marks[1]
    m3 = marks[2]
    m4 = marks[3]
    m5 = marks[4]
    name = students[i][-1]
    total = m1 + m2 + m3 + m4 + m5
    percentage = total/500*100
    temp.append([int(percentage),name])

print(temp)
[[86, 'Alice'], [85, 'Bob'], [88, 'Charlie'], [84, 'David'], [87, 'Eva'], [88, 'Fiona']]


# Print each number from the list lst
lst = [34, 4, 34567, 2, 34, 23]
for i in lst:
    print(i)

# Using the above method for percentage code:
for student in students:
    marks= student[:-1]
    total= sum(marks)
    percentage= total / 500*100
    name= student[-1]
    print(name,int(percentage))

# Print domain extension of each website in the list websites    
websites = ['www.netmax.com', 'www.gov.in', 'www.stackoverflow.com', 'www.google.co.uk','www.youtube.com']

for website in websites:
    domainext = website[-4:] 
    print(website + "-" + domainext)


