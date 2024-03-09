name = 'driksha thakur'
print(name)

# for modification of string we have several methods:
# Method 1: Capitalize and .upper
y=name.capitalize()
print(y)

u=name.title()
print(u)

# if use .upper it will convert the whole string to capital

# Method 2: Casefold and .lower
x =name.casefold()
print(x)

# Method 3: count()
y=name.count('a')
print(y)

# Method 4: find() and index()
z= name.find('h')
print(z)

# can find a whole word too
t = name.find('thakur')
print(t)

# suppose u have some mistake in your name and now you want to replace it
# Method 5: replace()
o= name.replace('d','f')
o= name.title()
print(o)

# Method 6: .expandtabs()
i= name.expandtabs(8)
print(i)

# and many more
