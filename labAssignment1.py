

# floating point summation
import random
import sys


class RandomNumbers:
    def __init__(self):
        pass

    def generate(self, n):
        with open('numbers.txt', 'w+') as f:
            f.write(str(n))
            f.write('\n\n')
            count = 0
            for i in range(n):
                num = self.rnd()
                f.write('{:>22}  '.format(num))
                count += 1
                if count % 4 == 0:
                    f.write('\n')
        print("random number generated successfully! saved as numbers.txt in the current directory.")

    def read(self):
        numbers = []
        with open('numbers.txt', 'r') as f:
            for line in f.readlines():
                numbers.extend(list(map(float, line.split())))
        return numbers

    def rnd(self):
        random.seed();
        exp = random.randint(-32, 32)
        base = random.uniform(0, 9)
        return base * 10**exp

    def summation(self, numbers):
        sum = 0.0
        for i in numbers:
            sum += i
        return sum


class AccurateSum:
    def __init__(self):
        pass

    def kahan_sum(self, numbers):
        sum = 0.0
        c = 0.0
        for i in numbers:
            y = i - c
            t = sum + y
            c = (t - sum) - y
            sum = t
        return sum

    def neumaier_sum(self, numbers):
        sum = 0.0
        c = 0.0
        for i in numbers:
            t = sum + i
            if abs(sum) >= abs(i):
                c += (sum - t) + i
            else:
                c += (i - t) + sum
            sum = t

        return sum + c

if __name__ == '__main__':
    n = 35000
    if len(sys.argv) == 2:
        n = int(sys.argv[1])

    rn = RandomNumbers()
    acs = AccurateSum()
    rn.generate(n)
    numbers = rn.read()
    # print(numbers)
    sumAsGivenSeq = rn.summation(numbers)
    sumIncrOrder = rn.summation(sorted(numbers))
    sumDecrOrder = rn.summation(sorted(numbers, reverse=True))
    accurateSum = acs.kahan_sum(numbers)
    # neumaier_sum = acs.neumaier_sum(numbers)
    print(f'Kahan Summation is: {accurateSum}')
    # print(f'neumaier sum is: {acs.neumaier_sum(numbers)}')

    # relative errors
    err1 = abs(sumAsGivenSeq - accurateSum) / accurateSum
    err2 = abs(sumIncrOrder - accurateSum) / accurateSum
    err3 = abs(sumDecrOrder - accurateSum) / accurateSum
    err4 = abs(accurateSum - accurateSum) / accurateSum

    # displaying the results
    print(f'\tMethod\t\t\tSum\t\t\tRelative error')
    print(f'1) as given sequence\t{sumAsGivenSeq}\t{err1}')
    print(f'2) increasingly sorted\t{sumIncrOrder}\t{err2}')
    print(f'3) decreasingly sorted\t{sumDecrOrder}\t{err3}')
    print(f'4) most accurate\t\t{accurateSum}\t{err4}')



