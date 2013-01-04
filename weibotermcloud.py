# -*- coding: cp936 -*-
import urllib2,re,jieba,urllib,time
from bs4 import BeautifulSoup
import collections
keyword='网站分析'
gsid='XXXXX'##替换为weibo.cn登陆后参数
page=100
def get_posts(keyword,gsid,page=1):
    url='http://weibo.cn/search/mblog?hideSearchFrame=&'+'&keyword='+urllib.quote_plus(keyword.decode('gbk').encode('utf-8'))+'&page='+str(page)+'&gsid='+gsid
    ##url='http://www.cloga.info'
##    print url
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    req = urllib2.Request(
        url = url,
        headers = headers
    )
    html=urllib2.urlopen(req).read()
    soup=BeautifulSoup(html,'xml')
    screen_names=[Screen_Name.get_text() for Screen_Name in soup.find_all('a',attrs={'class':'nk'})]
    contents=[content.get_text() for content in soup.find_all('span',attrs={'class':'ctt'})]
    return contents
contents=[]
for n in range(page):
    contents+=get_posts(keyword,gsid,page=n+1)
    print n
    time.sleep(30)

text=' '.join(contents)
stop_words='''#\n、1、2、3、4、5、6、7、8、9、0、啊、阿、哎、哎呀、哎哟、的、吗、唉、俺、俺们、按、按照、吧、吧哒、把、罢了、被、本、本着、比、比方、比如、鄙人、彼、彼此、边、别、别的、别说、
并、并且、不比、不成、不单、不但、不独、不管、不光、不过、不仅、不拘、不论、不怕、不然、不如、不特、不惟、不问、不只、朝、朝着、趁、趁着、乘、冲、除、除此之外、除非、除了、此、此间、此外、
从、从而、打、待、但、但是、当、当着、到、得、的、的话、等、等等、地、第、叮咚、对、对于、多、多少、而、而况、而且、而是、而外、而言、而已、尔后、反过来、反过来说、反之、非但、非徒、否则、
嘎、嘎登、该、赶、个、各、各个、各位、各种、各自、给、根据、跟、故、故此、固然、关于、管、归、果然、果真、过、哈、哈哈、呵、和、何、何处、何况、何时、嘿、哼、哼唷、呼哧、乎、哗、还是、还有、
换句话说、换言之、或、或是、或者、极了、及、及其、及至、即、即便、即或、即令、即若、即使、几、几时、己、既、既然、既是、继而、加之、假如、假若、假使、鉴于、将、较、较之、叫、接着、结果、借、
紧接着、进而、尽、尽管、经、经过、就、就是、就是说、据、具体地说、具体说来、开始、开外、靠、咳、可、可见、可是、可以、况且、啦、来、来着、离、例如、哩、连、连同、两者、了、临、另、另外、
另一方面、论、嘛、吗、慢说、漫说、冒、么、每、每当、们、莫若、某、某个、某些、拿、哪、哪边、哪儿、哪个、哪里、哪年、哪怕、哪天、哪些、哪样、那、那边、那儿、那个、那会儿、那里、那么、那么些、
那么样、那时、那些、那样、乃、乃至、呢、能、你、你们、您、宁、宁可、宁肯、宁愿、哦、呕、啪达、旁人、呸、凭、凭借、其、其次、其二、其他、其它、其一、其余、其中、起、起见、起见、岂但、恰恰相反、
前后、前者、且、然而、然后、然则、让、人家、任、任何、任凭、如、如此、如果、如何、如其、如若、如上所述、若、若非、若是、啥、上下、尚且、设若、设使、甚而、甚么、甚至、省得、时候、什么、什么样、
使得、是、是的、首先、谁、谁知、顺、顺着、似的、虽、虽然、虽说、虽则、随、随着、所、所以、他、他们、他人、它、它们、她、她们、倘、倘或、倘然、倘若、倘使、腾、替、通过、同、同时、哇、万一、往、
望、为、为何、为了、为什么、为着、喂、嗡嗡、我、我们、呜、呜呼、乌乎、无论、无宁、毋宁、嘻、吓、相对而言、像、向、向着、嘘、呀、焉、沿、沿着、要、要不、要不然、要不是、要么、要是、也、也罢、
也好、一、一般、一旦、一方面、一来、一切、一样、一则、依、依照、矣、以、以便、以及、以免、以至、以至于、以致、抑或、因、因此、因而、因为、哟、用、由、由此可见、由于、有、有的、有关、有些、
又、于、于是、于是乎、与、与此同时、与否、与其、越是、云云、哉、再说、再者、在、在下、咱、咱们、则、怎、怎么、怎么办、怎么样、怎样、咋、照、照着、者、这、这边、这儿、这个、这会儿、这就是说、
这里、这么、这么点儿、这么些、这么样、这时、这些、这样、正如、吱、之、之类、之所以、之一、只是、只限、只要、只有、至、至于、诸位、着、着呢、自、自从、自个儿、自各儿、自己、自家、自身、综上所述、
总的来看、总的来说、总的说来、总而言之、总之、纵、纵令、纵然、纵使、遵照、作为、兮、呃、呗、咚、咦、喏、啐、喔唷、嗬、嗯、嗳、\n、\n\n'''
url=re.compile(r'http://[^\s]+')
urls=re.findall(url, text)
text=re.sub(url, '', text)
terms=list(jieba.cut(text))+urls
##terms=list(jieba.cut(open('十八大报告.txt').read()))
c=collections.Counter(terms)
topX=c.most_common(200)

pre='''<!DOCTYPE html>
<html>
  <head>
    <title>TermCloud</title>
    <link rel="stylesheet" type="text/css" href="../jqcloud/jqcloud.css" />
    <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.js"></script>
    <script type="text/javascript" src="../jqcloud/jqcloud-1.0.2.js"></script>
    <script type="text/javascript">
      var word_list = ['''
next='''      ];
      $(function() {
        $("#my_favorite_latin_words").jQCloud(word_list);
      });
    </script>
  </head>
  <body>
    <h1>TermCloud</h1>
    <div id="my_favorite_latin_words" style="width: 1200px; height: 550px; border: 1px solid #ccc;"></div>
  </body>
</html>'''
termcloud=''.join(['{text:"%s",weight:%i},' % (i[0],i[1]) for i in topX if i[0].encode('gbk','ignore') not in stop_words.split('、') and i[1]>1]).encode('gbk','ignore')
with open('termcloud.html','w') as f:
    f.write(pre+termcloud+next)
    


