#find line number of a word in the file
line=0
with open("hello.txt") as f:
    lines=f.readlines()
    n=1
    for line in lines:
        if("side" in line):
            print("side is present in line",n)
            break
        n+=1

