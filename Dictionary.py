population = {343433,434343,343434,6565665,4564456}

# Data stored in Key value 
# Key and value both are combindely 1

population = {
    'IND':345649936920,
    'CHINA':62057290426,
    'UK':666299250206,
    'USA':5205492962,
#You can store a dict inside a dict
    'Hello':{
        'get':'dfddhjs'
    }
}
# print(population['Hello']['get'])

print(population['USA'])

# Main 3 methods:
print(population.keys())
print(population.values())
print(population.items())

# HW ques
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
# print this hello

print(d['k1'][2]['k2'][1]['tough'][2][0])

