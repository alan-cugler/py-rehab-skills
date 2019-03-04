if __name__ == '__main__':
    n = int(input())
    arr = sorted(map(int, input().split()))

x = True
n = arr[-1]
v = 1
while x == True:
    n = arr[-v]
    v+=1
    if n != arr[-1]:
        x = False
print(n)
