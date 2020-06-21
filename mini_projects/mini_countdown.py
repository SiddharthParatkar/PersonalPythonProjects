import  time

def recursive_countdown(n):
    if n == 0:
        print(0)
        return 0
    else:
        print(n)
        time.sleep(1)
        return recursive_countdown(n-1)

z = 5
recursive_countdown(5)