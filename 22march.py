name = ['Manpreet','Mohan','Harpreet','Ballu','Diksha','Kriti']
marks = [67,89,32,56,88,99]

# Make dictinoary 
#d = {
#    'Manpreet':67,
#    'Mohan':89
#}

student={}
for i in range(len(name)):
    student[name[i]]= marks[i]
print(student)

# Get the key corresponding to the minimum value from the following dictionary
sampleDict = {
    'Physics':82,
    'Math':65,
    'History':75
}
min1= min(sampleDict, key=sampleDict.get)
print(min1)
# Expected output: Math