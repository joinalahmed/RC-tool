import itertools
import pyexcel as pe

outs=open('output.txt', 'w')
a = 2 ** 4

total=list()

test_sets=[tuple(map(int,str('0101'))),tuple(map(int,str('0011')))]



def truth_push(input_result):
    newstring = str(input_result[0])
    for ch in range(1,len(input_result)):
        newstring+=str(input_result[ch])
    levels.append(newstring)

def truth_fix(input_result):
    for n, i in enumerate(input_result):
        if i == True:
            result[n] = 1
        if i == False:
            result[n] = 0

def getheader(cc):
    che=['Test Pattern']

    for ch in range(cc):
        ches=cc-1-ch
        che.append('Level-'+str(ches))
        if ch == cc-1:
            che.append('Level-'+str(cc-1))
    return che
def getheaders(cc,lines):
    che=[lines]
    for ch in range(cc):
        che.append(lines)
        if ch == cc-1:
            che.append(lines)
    return che


lines =str('a,b,c,d')
lines=lines.replace(',','')
testPatterns = table = test_sets
for p in testPatterns:
    levels = list()
    a,b,c,d = p
    result = [a,b,c,d]
    truth_push(result)

    b = (a and c and d) ^ b
    result = [a,b,c,d]
    truth_fix(result)
    truth_push(result)
    truth_push(result)
    total.append(levels)
count = 1

che=list()

che=getheader(count)

ches=getheaders(count,lines)

total.insert(0,che)

total.insert(1,ches)

sheet=pe.Sheet(total)

outs.write(str(sheet.content))

sheet.save_as('tests.csv')



value=len(sheet.column_range())
sheet.column.select([0,value-1])
sheet.save_as('/home/joy/Desktop/output.csv')


value=len(sheet.column_range())
sheet.column.select([0,value-1])
sheet.save_as('/home/joy/Desktop/outputs.csv')

