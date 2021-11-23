lis=[65,87,1,148,2,541,30,5,12,541]
n=541
def linear_search(lis,n):
    for i in range(len(lis)):
        if(n==lis[i]):
           print("Search of ",n ,"found in postion of ",i+1)
           break
    else:
        print("search of ",n , "not found" )

linear_search(lis,n)


lis=[65,87,1,148,2,541,30,5,12,541]
n=541
pos=-1
i=0
def linear_search(lis,n):
    for i in range(len(lis)):
        if(n==lis[i]):
            globals() ['pos'] = i
            return True
    else:
        False
if linear_search(lis,n):
    print("Search of ", n, "found in postion of ",pos+ i )
else:
    print("search of ",n , "not found" )
