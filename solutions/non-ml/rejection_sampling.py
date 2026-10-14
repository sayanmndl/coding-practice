import random

def rand7():
    return random.randint(1,7)

def rand10():
    while True:
        x = (rand7() - 1) * 7 + rand7()

        if x <= 40:
            return (x - 1) % 10 + 1


def rand3():
    return random.randint(1,3)

def rand10():
    while True:
        x = (
            (rand3()-1)*9
            + (rand3() -1)*3
            + rand3()
        )

        if x <=20:
            return (x-1)%10 +1