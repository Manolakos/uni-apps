number = int(input("Type a number: "))

def f(x):
    x = x*3 + 1
    x = str(x)
    y = 0
    for j in range(len(x)):
        y = y + int(x[j])

    return y

rep = f(number)
print(rep)

if rep >= 10:
    while rep >= 10:
        print(f(rep))
        rep = f(rep)


