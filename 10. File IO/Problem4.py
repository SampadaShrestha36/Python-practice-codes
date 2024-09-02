# replacing a word in the file by updating
with open("file.txt") as f:
    c=f.read()
newc=c.replace("BTS","Bangtan Sonyeondan")
with open("file.txt","w") as f:
    f.write(newc)