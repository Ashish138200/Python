def pattern(n):
    for i in range(n,1,-1):
        j=str(i)
        s=(j+'*')*i
        l=len(s)-1
        print(s[:l])
        if(i==2):
            print('1')
def revpat(n):
    for i in range(2,n+1):
        j=str(i)
        if(i==2):
            print('1')
        s=(j+'*')*i
        l = len(s) - 1
        print(s[:l])

n = int(input())
pattern(n)
revpat(n)