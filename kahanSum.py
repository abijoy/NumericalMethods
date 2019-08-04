
def kahan_sum(numbers):
    sum = 0.0
    c = 0.0
    for i in numbers:
        y = i - c
        t = sum + y
        c = (t - sum) - y
        sum = t
    return sum


def neumaier_sum(numbers):
    sum = 0.0
    c = 0.0
    for i in numbers:
        t = sum + i
        if abs(sum) >= abs(i):
            c += (sum -t) + i
        else:
            c += (i-t) + sum
        sum = t

    return sum + c