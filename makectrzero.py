
# DFL 18/07/2020

# This file is used as part of the restart mechanism in setstatus_1.py

counter=0
print (counter)

# is this more complex than required, storing ctr as string,
# but the file can be edit using notepad.

# write counter to ctr.txt, the file name could have been parameterised

f = open('ctr.txt','w')
f.write(str(counter))
f.close()

# read ctr.txt, add one to it and write it out

g = open('ctr.txt','r')
d = int(g.read())
g.close()

d = d + 1
counter = d
print(int(d))

f = open('ctr.txt','w')
f.write(str(counter))
f.close()
