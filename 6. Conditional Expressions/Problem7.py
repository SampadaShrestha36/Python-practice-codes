#find out whether a given post is about "sam" or not
post=input("enter the post")
if("sam".lower() in post.lower()):
    print("it is talking about sam")
else:
    print("this post is not about sam")
