START = 2
END = 11
HALF = 2

for i in range(START, END):
    for j in range(START, END // HALF + 1):
        print(f"{j:>2} X {i:>2} = {i * j:>2}", end="\t")
    print()
print()
for i in range(START, END):
    for j in range(END // HALF + 1, END):
        print(f"{j:>2} X {i:>2} = {i * j:>2}", end="\t")
    print()

