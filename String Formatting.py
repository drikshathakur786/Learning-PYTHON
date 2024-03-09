# Suppose you have the following two words
# You want the output to be chble taair. 
word1 ='table'
word2 ='chair'
w1 = word2[:2] + word1[2:]
w2 = word1[:2] + word2[2:]
word1=w1
word2=w2
print(word1, word2)

# Multi line string
text="""Shiv Kumar Batalvi, a luminary in the realm of Punjabi literature, captivated hearts with his profound poetry that resonated with raw emotions and poignant imagery. Born on July 23, 1936, in Punjab, Batala, his life was a tapestry of passion, pain, and poetic brilliance. From a tender age, Batalvi displayed an innate talent for verse, crafting verses that transcended mere words, delving deep into the human soul. His poetic journey burgeoned during his tumultuous teenage years, marked by unrequited love, societal upheavals, and personal struggles, which served as a wellspring of inspiration for his poetry. Batalvi's poetry was a melange of romance, despair, and existential ponderings, reflecting the human condition with unparalleled authenticity. His magnum opus, "Loona," a poetic saga of tragic love, catapulted him to literary stardom, earning him acclaim far beyond the boundaries of Punjab. Despite his meteoric rise, Batalvi's personal life was fraught with turmoil, grappling with mental health issues and the tumult of relationships. Yet, his poetic prowess remained undiminished, serving as both catharsis and solace amidst the tempests of life. Tragically, Shiv Kumar Batalvi's journey was cut short on May 6, 1973, leaving behind a legacy that continues to inspire generations of poets and enthusiasts alike. His verses, imbued with the fragrance of Punjab and the echoes of human experiences, endure as timeless masterpieces, immortalizing the enigmatic poet who bared his soul through his words."""
print(text)

# String formatting: formats the specified values and insert them inside the string's placeholder
name ='Muskan'
age=23

#line='Hello my name is',name,'and my age is',age
#print(line)

#line='My name is name and my age is age'.format()

line= f'My name is {name} and my age is {age}'
print(line)
print(type(line))

#print('Hello my name is',name,'and my age is',age)

#output= hello my name is Muskan and my age is 23