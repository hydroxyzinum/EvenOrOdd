num = raw_input('Enter number(s) of solider(s) (separate each number by space): ').split(' ')
number = map(int,num)

even = [i for i in number if i%2 == 0 ]
print 'Evens army: ', even      #Shows all even numbers in decimal format

odd = [i for i in number if i%2]
print 'Odds army: ', odd        #Shows all odd numbers in decimal format

l = len(number)     #Counts how many numbers are in the array

sum1 = 0
sum2 = 0

x = []
for i in even:
    x.append("{0:b}".format(i))     #Converting decimal into binary even numbers
    l = len(even)

y = []
for i in odd:
    y.append("{0:b}".format(i))     #Converting decimal into binary odd numbers
    k = len(odd)

for i in range(l):
    a = x[i].count('0')     # Counts how many '0' are in all integers of even numbers
    sum1 += int(a)          # Then sum up all '0' from even numbers


for i in range(k):
    b = y[i].count('1')     # Counts how many '1' are in all integers of odd numbers
    sum2 += int(b)          # Then sum up all '1' from odd numbers


print x
print 'Score of even soliders: ', sum1      # Shows even numbers in binary format,
                                            #then shows score of suming up '0'
print y
print 'Score of odd soliders: ', sum2       # Shows odd numbers in binary format,
                                            #then shows score of suming up '1'

print 'Who is gonna win the war?'
if sum1 > sum2:
    print 'Evens win!'
elif sum1 == sum2:
    print 'Tie!'
elif sum1 < sum2:
    print 'Odds win!'
