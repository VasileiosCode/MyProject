# Topic 3 Collection (Data Types) Delete every 3rd character

print('In the given string, delete all the characters whose positions are divisible by and print the results.(The initial element has a position 0.')
print('for example: input abracadabra output bracaaba')
print('\n')

s = input ()

result = ''

for i in range(0,len(s)):
    if i % 3 != 0: result += s[i]

print(result)



print('\n')

word = input('Please enter the word: ')

empty_str = ''

for x in range(0,len(word)):
    if x % 3 != 0:
        empty_str += s[x]

print(empty_str)
