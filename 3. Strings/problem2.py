#use replace() function
letter='''
Dear <|name|>,
You are selected!
<|date|>
'''
print(letter.replace("<|name|>","sam").replace("<|date|>","14 july"))
