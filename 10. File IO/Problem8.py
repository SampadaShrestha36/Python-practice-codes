#make copy of a file
with open("dynamite.txt") as f:
    c=f.read()
    with open("copy.txt","w") as g:
        g.write(c)
    g.close()
f.close()