# 0.5 Lab

u=[20,10, 15,75]
print sum(u)/len(u)

#0.5.11
z = [[x,y] for x in ['A','B','C'] for y in [1,2,3]]
print z

#0.5.12
LoL=[[.25, .75,.1],[-1,0],[4,4,4,4]]
print sum([sum(x) for x in LoL])

#0.5.13
#[x,y] = [1]

#0.5.14
L={-4,-2,1,2,5,0}
s=[(i,j,k) for i in L for j in L for k in L if i+j+k==0]
print s

