
x = 4

for i in range(x):
    for j in range(x-i-1):
        print(" ", end="")

    for j in range(i+1):
        print("*", end=" ") 

    print()

