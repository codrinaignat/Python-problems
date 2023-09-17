basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket) #prints 'True'

print('crabgrass' in basket) #prints 'False'

a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a-b)
print(a|b)
print(a&b)
print(a^b)