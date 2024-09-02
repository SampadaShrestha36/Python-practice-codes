#find if a word is in the file or not
with open("hello.txt") as f:
    c=f.read()
if("side" in c):
    print("side is present")
else:
    print("side is not present")