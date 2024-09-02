#writing tables in different files inside a folder
def table(n):
    s=""
    for i in range(1,11):
        s=s+f"{n}X{i}={n*i}\n"
    with open(f"tables/table_{n}.txt","w") as f:
        f.write(s)
for i in range(2,21):
    table(i)