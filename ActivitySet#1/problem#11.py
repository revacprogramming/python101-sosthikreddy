
name = input("Enter file:")
if len(name) < 1:
     name = "mbox-short.txt"
handle = open(name)
d={}
t=[]
for line in handle:
    if line.startswith('From:'): continue
    if not line.startswith('From'): continue
    index=line.find(':')
    st=line[index-2:index]
    if st not in d:
        d[st]=1
    else:
        d[st]+=1

t = list(d.items())
t.sort()
for a,b in t:
    print(a,b)