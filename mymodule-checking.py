# After import write the module name means the .py file name that has some function in it
import mymodule
# When using a function from a module, use the syntax: module_name.function_name.
mymodule.greeting("Driksha")


import mymodule
a = mymodule.person1["age"]
print(a)

# Renaming/Giving a nickname to the module
import mymodule as mx
a = mx.person1["age"]
print(a)

# Python also has many built in modules
