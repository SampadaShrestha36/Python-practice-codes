# replacing a list of words in the file by updating
words=["hello","from","the","outside"]
with open("hello.txt") as f:
    c=f.read()
for i in words:
    c=c.replace(i,"*"*len(i))
with open("hello.txt","w") as f:
        f.write(c)