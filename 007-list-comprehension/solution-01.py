if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

a = []

for s in range(x+1):
    for t in range(y+1):
        for v in range(z+1):
            if not s+t+v == n:
                b = [s,t,v] 
                a.append(b)

print(a)
