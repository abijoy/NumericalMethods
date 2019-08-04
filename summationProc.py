import sys
import kahanSum
import random_numbers

random_numbers.generate(int(sys.argv[1]))
print("random number generated successfully! saved as numbers.txt in the current directory.")

numbers = []
with open('numbers.txt', 'r') as f:
    for line in f.readlines():
        numbers.extend(list(map(float, line.split())))

#print(numbers)

# getting actual sum using Kahan algorithm
actualSum = kahanSum.kahan_sum(numbers[1:])
print(actualSum)

# getting sum as given sequence
sumAsGivenSeq = 0.0
for i in numbers[1:]:
    sumAsGivenSeq += i

# getting sum in increasing order of the sequence.
sumIncrOrder = 0.0
for i in sorted(numbers[1:], reverse=False):
    sumIncrOrder += i

# getting sum in decreasing order of the sequence.
sumDecrOder = 0.0
for i in sorted(numbers[1:], reverse=True):
    sumDecrOder += i


# relative errors
err1 = abs(sumAsGivenSeq - actualSum) / actualSum
err2 = abs(sumIncrOrder - actualSum) / actualSum
err3 = abs(sumDecrOder - actualSum) / actualSum
err4 = abs(actualSum - actualSum) / actualSum

print(f'\tMethod\t\t\t\t\t\tSum\t\t\t\t\tRelative error')
print(f'1) as given sequence\t{sumAsGivenSeq}\t{err1}')
print(f'2) increasingly sorted\t{sumIncrOrder}\t{err2}')
print(f'3) decreasingly sorted\t{sumDecrOder}\t{err3}')
print(f'4) most accurate\t\t{actualSum}\t{err4}')


