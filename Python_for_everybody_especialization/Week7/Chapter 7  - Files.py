fhand = open('mbox.txt')
print(fhand)
count = 0
for cheese in fhand:
    count = count + 1
print('Line count', count)

fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20])

fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print ('There were', count, 'subject lines in', fname)

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print ('There were', count, 'subject lines in', fname)