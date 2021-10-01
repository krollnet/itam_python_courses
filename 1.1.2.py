
#1.1.1
'''
a = list(map(int,input().split()))
print(a)
a=a[::-1]
print(a)
'''
#1.1.2
'''
a=list(map(int,input().split()))
ma=-10000
mi=10000
for x in a:
    if x>ma:
        ma=x
    if x<mi:
        mi=x
print(ma,mi)
'''
#1.1.3
'''
a=input()
if len(a)>=6:
    print(a[3],a[5],end=' ')
else:
    a=a[::-1]
    for i in range(0,len(a),2):
        print(a[i])
'''
#1.1.4
'''
a=list(map(int,input().split()))
k=n=m=0
for x in a:
    if x<0:
        k+=1
    if x>8:
        n+=1
    if x%2==0:
        m+=1
print(k,n,m)
'''
#1.2.1
'''
n=int(input())
k1=k2=0
for i in range(n):
    a,b,c,d=list(input().split())
    if d=='True':
        k1+=1
    if d=='False': k2+=1
print(k1,k2)
'''
#1.2.3
'''
a=input()
n1=n2=n3=0
c=''
for i in range(len(a)):
    if 64<=ord(a[i])<=90:
        n1=i;break
for i in range(n1,len(a)):
    if 48<=ord(a[i])<=57:
        n2=i;break
for i in range(n2,len(a)):
    if ord(a[i])==46:
        n3=i;break
print(n1,n2,n3)
h=n2-n1
for i in range(n1,n3+1,h+1):
    c+=a[i]
print(c)
'''    
    
    
        
        
        
