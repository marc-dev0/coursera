for i in [5, 4, 3, 2, 1]:
    print(i)
print('hola')

friends = ['Joseph', 'Juan', 'Marc']
for friend in friends:
    print('Feliz navidad cachudo ' + friend)

sork = 0
print('before', sork)
for thing in [9, 41, 12, 3, 74, 15]:
    sork = sork + 1
    print(sork, thing)
print('After', sork)

for letter in 'banana':
    print(letter)

s = 'X-DSPAM-Confidence: 0.7556'
print(s[20:4])

fruit = 'banana'
var = 'n' in fruit
print (var)

if fruit == 'banana':
    print ('All right', 'bananas')

greet = 'Hello bob'
zap = greet.lower()
print(type(zap))
print(zap)
print(dir(zap))

print('Hi There'.lower())
print('Hi There'.upper())
pos = fruit.find('na')
print (pos)

greet = '    Hello bob   '
#strip = trim() java c#
print(greet.lstrip())
print(greet.rstrip())
print(greet.strip())

line = 'Please have a nice day'
print(line.startswith('Please'))
print(line.endswith('day'))
