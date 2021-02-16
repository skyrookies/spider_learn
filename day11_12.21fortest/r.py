line_no=0
with open('text.txt','r',encoding='utf8') as f:
    for line in f:
        line_no+=1
        print(line_no,':',line)
f.close()