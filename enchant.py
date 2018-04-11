import enchant
import itertools
c=0
dict = enchant.Dict("en_US")
letters = input()
wosp = open("withoutspace.txt",'w')
w1sp = open("withonespace.txt", 'w')
w2sp = open("withtwospace.txt", 'w')

# Without Space
permut = list(itertools.permutations(letters))
for i in range(0,len(permut)) :
    if dict.check(''.join(permut[i])) == True :
        wosp.write(str(''.join(permut[i]))+'\n')
wosp.close()
# With space
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
        if dict.check(j) == True :
            c+=1
    if c==2:
        w1sp.write(str(strings[0]+' '+strings[1])+'\n')
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
        if dict.check(j) == True :
            c+=1
    if c==3:
        w2sp.write(str(strings[0]+' '+strings[1]+' '+strings[2])+'\n')
w2sp.close()

