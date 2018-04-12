import enchant
import itertools
from autocorrect import spell
c=0
dict = enchant.Dict("en_US")
letters = input()
wosp = open("withoutspacesuggestions.txt",'w')
w1sp = open("withonespacesuggestions.txt", 'w')
w2sp = open("withtwospacesuggestions.txt", 'w')

# Without Space
permut = list(itertools.permutations(letters))
for i in range(0,len(permut)) :
    wosp.write(str(spell(''.join(permut[i])))+'\n')
wosp.close()
# With one Space
letters += str(' ')
permutwithspace = list(itertools.permutations(letters))
if len(permutwithspace) % 2 ==0 :
    sizeoflist = len(permutwithspace)/2
else:
    sizeoflist = (len(permutwithspace)+1)/2
for i in range(0,len(permutwithspace)) :
    c=0
    strings = ''.join(permutwithspace[i])
    strings = strings.split()
    for j in strings :
        w1sp.write(spell(j) + ' ')
    w1sp.write('\n')
w1sp.close()
#With 2 spaces
letters += str(' ')
permutwith2space = list(itertools.permutations(letters))
if len(permutwith2space) % 2 ==0 :
    sizeoflist = len(permutwith2space)/2
else:
    sizeoflist = (len(permutwith2space)+1)/2
for i in range(0,len(permutwith2space)) :
    c=0
    strings = ''.join(permutwith2space[i])
    strings = strings.split()
    for j in strings :
        w2sp.write(spell(j)+ ' ')
    w2sp.write('\n')
w2sp.close()

