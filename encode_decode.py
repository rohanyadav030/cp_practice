#cp practice encode decode problem

n=input("enter a string")

l=[]
for i in n:
  l.append(ord(i))
print("coded string")  
print(l)
l1=[]
for i in l:
  l1.append(chr(i))
print("decoded string")
print(l1)

'''
*************** output ***************
enter a stringrohan
coded string
[114, 111, 104, 97, 110]
decoded string
['r', 'o', 'h', 'a', 'n']
 '''
