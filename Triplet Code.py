#Triplet sum

n=int(input())
a=list(map(int,input().split()))
a.sort()
k=int(input())
ans=[]
for i in range(n-2):
    l=i+1
    r=n-1
    while(l<r):
        if(a[i]+a[l]+a[r]==k):
            ans=[a[l],a[r],a[i]]
            break
        elif(a[i]+a[l]+a[r]<k):
            l+=1
        else:
            r-=1
if(ans==[]):
    print("No Triplet found")
else:
    print(ans)
    