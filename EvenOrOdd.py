num = raw_input('Enter number(s) of solider(s) (separate each number by space): ').split(' ')
number = map(int,num)

even = [i for i in number if i%2 == 0 ]
print 'Evens army: ', even

odd = [i for i in number if i%2]
print 'Odds army: ', odd

l = len(number)

sum1 = 0
sum2 = 0

x = []
for i in even:
    x.append("{0:b}".format(i))
    l = len(even)

y = []
for i in odd:
    y.append("{0:b}".format(i))
    k = len(odd)

for i in range(l):
    a = x[i].count('0')
    sum1 += int(a)


for i in range(k):
    b = y[i].count('1')
    sum2 += int(b)


print x
print 'Score of even soliders: ', sum1

print y
print 'Score of odd soliders: ', sum2

print 'Who is gonna win the war?'
if sum1 > sum2:
    print 'Evens win!'
elif sum1 == sum2:
    print 'Tie!'
elif sum1 < sum2:
    print 'Odds win!'
