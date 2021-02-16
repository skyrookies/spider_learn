from bs4 import BeautifulSoup#网页解析
import re   #正则表达式
import urllib.request,urllib.error   #指定统一资源定位器URL
import sqlite3  #SQLlite数据库操作
import xlwt     #excel操作
import sys
import io
import time
FindLink=re.compile(r'<a href="(.*)">')
#影片图片
FindImgSrc = re.compile(r'<img.*src="(.*?)"',re.S)#re.S..让换行符包含在字符中
#影片片名
FindTitle = re.compile(r'<span class="title">(.*)</span>')
#影片评分
FindRating = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
#找到概况
FindInq= re.compile(r'<span class="inq">(.*)</span>',re.S)
#找到影片的相关内容
FindBd = re.compile(r'<p class="">(.*?)</p>',re.S)
# 添加附加数据
def getdate():
    baseurl="https://movie.douban.com/top250?start="
    datalist=[]
    for i in range(0,10):
        print(i*25,"~~",(i+1)*25)
        url=baseurl+str(i*25)
        html_get=geturl(url)
        #上述已获得网页html信息
        #对获取数据逐一解析
        aftersoup=BeautifulSoup(html_get,"html.parser")
        #print(aftersoup.title)
        for item in aftersoup.find_all('div',class_='item'):
            data=[]
            item_str = str(item)
            #print(item_str)
            titlefind = re.findall(FindTitle, item_str)
            if (len(titlefind) >= 2):
                ctitle = titlefind[0]                   # 添加中文名
                data.append(ctitle)
                otitle = titlefind[1].replace("/", "")
                otitle=otitle.replace(r"\xa0","")       # 去掉无关的符号
                data.append(otitle)                      # 添加外国名
            else:
                data.append(titlefind[0])
                data.append(' ')                        # 外国名字留空
            #print(ctitle,otitle)
            linkfind=re.findall(FindLink,item_str)[0]
            #print(linkfind)
            data.append(linkfind)
            imgSrcfind = re.findall(FindImgSrc, item_str)[0]
            #print(imgSrcfind)
            data.append(imgSrcfind)
            ratingfind = re.findall(FindRating, item_str)[0]
            #print(ratingfind)
            data.append(ratingfind)
            inqfind = re.findall(FindInq, item_str)
            if(len(inqfind)!=0):
                inqfind=inqfind[0].replace("。"," ")
                data.append(inqfind)
                # print(inqfind)
            else:
                data.append(" ")
                # print("\n")

            bdfind = re.findall(FindBd, item_str)[0]
            bdfind=re.sub('<br(\s+)?/>(\s+)?',"",bdfind)
            bdfind=re.sub('/',"",bdfind)
            bdfind=str(bdfind)
            data.append(bdfind.strip())
            #print(bdfind,end='')

            #print(data)
            datalist.append(data)
    return datalist
def geturl(urlofgoal):
    # dict = {
    #     'hello': 'world'
    # }
    # data = bytes(urllib.parse.urlencode(dict), encoding='utf8')
    # 添加包头
    headersofgoal = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.50"

    }
    # method = 'GET'
    # url = 'https://www.baidu.com'
    #标准Request函数构造
    #req = urllib.request.Request(url=urlofgoal,date=dataofgoal,headers=headersofgoal,method=methodofgoal)
    req = urllib.request.Request(url=urlofgoal, headers=headersofgoal)
    #封装包
    html=''
    try:
        response = urllib.request.urlopen(req,timeout=3)
        html=response.read().decode('utf-8')
        #print(html)
        #response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    except:
        print('TIME OUT')
    else:
        print("Request Successfully")

    return html

def savedatetoexcel(datalist,savepath):
    workbook=xlwt.Workbook(encoding='utf-8')
    sheet = workbook.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)  # 创建工作表
    col = ("电影中文名", "电影外文名", "电影情况详细链接", "电影图片链接", "豆瓣评分", "概况", "相关信息")
    for i in range(0,7):
        sheet.write(0,i,col[i]) #列名
    for i in range(0, 250):
        print("第{0}条完成保存".format(i))
        data = datalist[i]
        for j in range(0, 7):
            sheet.write(i + 1, j, data[j])  # 数据
    workbook.save(savepath)
def savedatetodb():
    conn = sqlite3.connect("test.db")
    print("成功建立连接")
    c = conn.cursor()
    sqlin = '''
        insert into company(id,name,age,address,salary)
            values(2,"jiang",23,"here",40000)

    '''

    c.execute(sqlin)
    conn.commit()
    conn.close()
    print("插入成功")
if __name__=="__main__":
    # 主函数入口
    sys.stdout =io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
    #修改print函数默认输出编码，方便重定向
    url = "https://movie.douban.com/top250?start="
    #geturl(url)
    datalist=getdate()
    savepath=r"./douban_top250.xls"
    #savedatetoexcel(datalist, savepath)
