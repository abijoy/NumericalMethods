import random

def rnd():
    random.seed();
    exp = random.randint(-32, 32)
    base = random.uniform(0, 9)
    return base * 10**exp


def generate(n):
    with open('numbers.txt', 'w+') as f:
        f.write(str(n))
        f.write('\n\n')
        count = 0
        for i in range(n):
            num = rnd()
            f.write('{:>22}  '.format(num))
            count += 1
            if count % 4 == 0:
                f.write('\n')
