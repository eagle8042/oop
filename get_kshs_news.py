import re
import urllib.request

class KSHS_Bot:

    def get_web_content(self):
        bot = urllib.request.urlopen('https://www.kshs.kh.edu.tw/view/index.php?WebID=269')
        content = bot.read().decode('utf8')

    def fetch_kshs_news(content):
        for each_news in re.findall(r'28016.+NowSubId=0">(.+)</a>', content):
            print(each_news)


bot = KSHS_Bot
bot.show_news()

