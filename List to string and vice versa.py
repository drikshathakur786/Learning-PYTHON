hashtags = '#popular#instagram#trending#follow#love#viral#like#instagood#explorepage#photography#explore#likeforlikes#followforfollowback#music#fashion#instadaily#famous#photooftheday#tiktok#likes#picoftheday#memes#beautiful#model#cute#followme#style#beauty#funny#photo'

lst = hashtags.split('#')
print(lst)

# by default spaces pe split kr deta hai
hashtags= ['instagram','trending','follow','love']
lst='#'.join(hashtags)
print(lst)
# by default spaces pe split kr deta hai
lst= hashtags.split()

# 2 strings ko apas mai # k sath jodna hai
lst='#'.join(hashtags)
print(lst)

# convert list into string and string into list
lst='# Driksha #'.join(hashtags)
print(lst)

