#read te3xt from a file and check presence a specific word in it
f=open("poem.txt")
c=f.read()
if("twinkle" in c):
    print("Twinkle is present in the file")
else:
    print("Twinkle is not present in the file")