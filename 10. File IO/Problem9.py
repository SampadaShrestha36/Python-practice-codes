#check whether content of one file is identical to another file
with open("dynamite.txt") as f:
    c1=f.read()
    with open("copy.txt") as g:
        c2=g.read()
    g.close()
f.close()
if c1==c2:
    print("The files are identical")
else:
    print("The files are not identical")