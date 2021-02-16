import sys,random
n=int(sys.argv[1])
m=int(sys.argv[2])
l=sys.argv[3:]
def test(a,b,c):
    for i in range(a):
        print(random.randrange(0,b))
    for j in range(len(c)):
        print(c[j])
test(n,m,l)
print(l)
