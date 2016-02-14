import urllib.request

from html.parser import HTMLParser

data = urllib.request.urlopen('https://tw.movies.yahoo.com/movieinfo_main.html/id=5644') 

content = data.read().decode('utf_8')

data.close()

numberIndex=content.find('photoplayer.html?id=')+20
number=content[numberIndex]+content[numberIndex+1]+content[numberIndex+2]+content[numberIndex+3]
numberTxt=number+'.txt'
file = open(numberTxt, 'w', encoding = 'UTF-8')


class myparser(HTMLParser):







    def __init__(self):

        HTMLParser.__init__(self)

        self.chineseName=0

        self.englishName=0

        self.date=0

        self.type=0

        self.time=0

        self.dir=0

        self.act=0

        self.cop=0

        self.web=0
        self.introduction=0


    def handle_starttag(self,tag,attrs):

        if tag=='h4' and self.getpos()[0]<230:

            self.chineseName=1

        if tag=='h5' and self.getpos()[0]<230:

            self.englishName=1

        if tag=='div' and attrs==[('class','text full')]:
            print("劇情簡介:")
            file.write("劇情簡介:"+'\n')
            self.introduction=1
        if tag=='span' and attrs==[('class','date')]:
            self.introduction=0

    def handle_data(self,data):

        if self.chineseName==1:

            print("電影名稱(中):",data)
            file.write("電影名稱(中):"+data+'\n')

            self.chineseName=0

        if self.englishName==1:

            print("電影名稱(英):",data)
            file.write("電影名稱(英):"+data+'\n')

            self.englishName=0

        if self.date==1:

            print("上映日期:",data)
            file.write("上映日期:"+data+'\n')

            self.date=0

        if data=="上映日期：":

            self.date=1

        if self.type==1:

            print("類型:",data)
            file.write("類型:"+data+'\n')

            self.type=0

        if data=="類　　型：":

            self.type=1

        if self.time==1:

            print("片長:",data)
            file.write("片長:"+data+'\n')

            self.time=0

        if data=="片　　長：":

            self.time=1

        if self.dir==1:

            print("導演:",data)
            file.write("導演:"+data+'\n')
            

            self.dir=0

        if data=="導　　演：":

            self.dir=1


        if self.cop==1:

            print("發行公司:",data)
            file.write("發行公司:"+data+'\n')
            self.cop=0

        if data=="發行公司：":
            self.act=0
            file.write('\n')
            self.cop=1



        if self.act==1:

            print(data)
            file.write(data)

            

        if data=="演　　員：":

            self.act=1
            print("演員:")
            file.write("演員:")






        

        if self.web==1:

            print("官方網站:",data)
            file.write("官方網站:"+data+'\n')

            self.web=0

        if data=="官方網站：":

            self.web=1


        if self.introduction==1:
            print(data)
            file.write(data+'\n')





Parser=myparser()

Parser.feed(content)

file.close()
