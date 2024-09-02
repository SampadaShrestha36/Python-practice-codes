#wipe out content of a file
with open("randomfiletowipeout.txt","w") as f:
    f.write("")
f.close()