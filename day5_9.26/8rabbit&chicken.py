print('请输入总头数：')
h=int(input())
f=1
check=0
while f%2!=0:
    print('请输入总脚数（必须是偶数）')
    f=int(input())
for c in range(0,h+1):
    r=h-c
    if(2*c+4*r==f):
        print(str.format('鸡有{0}只    兔有{1}只',c,r))
        check=1
        break
if(check!=1):
    print('无解 请重新输入')
