import random
import urllib
from time import sleep
import pymysql
import requests
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
options = webdriver.ChromeOptions()
num = str(float(random.randint(500, 600)))
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/{}"
                     " (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/{}".format(num, num))
# 禁止图片和css加载
prefs = {"profile.managed_default_content_settings.images": 2, 'permissions.default.stylesheet': 2}
options.add_experimental_option("prefs", prefs)
options.add_argument('--window-position=0,0');
#chrome 启动初始位置
options.add_argument('--window-position=0,0');
#chrome 启动初始大小
options.add_argument('--window-size=1080,800');

browser=webdriver.Chrome(options=options)

def getM3U8(strURL):
        browser.get('https://v.7cyd.com/vip/?url='+strURL+'&mm=1&title=七彩解析_永久免费_高速稳定&yuming=https://jx.7cyd.com/&jiazai=正在加载中！请稍等....&beiyong=')
        cookie = browser.get_cookies()
        sleep(0.5)

        #拿到 js中动态参数做post传值
        jsm1 = 'return m1'
        return_valjsm1=browser.execute_script(jsm1)
        jsm2 = 'return m2'
        return_valjsm2 = browser.execute_script(jsm2)
        jsm3 = 'return m3'
        return_valjsm3 = browser.execute_script(jsm3)
        jsmxxx = 'return ഈഇആഅ'
        return_valjsmxxx = browser.execute_script(jsmxxx)  #执行javascript
        poststr='lg=4&time='+return_valjsm3+'&ip=223.91.29.107&key='+return_valjsm1+'&key2='+return_valjsm2+'&key3='+return_valjsmxxx+'&url='+strURL+''

        cookiename = cookie[0]['name']
        cookieval = cookie[0]['value']
        cookiename1 = cookie[2]['name']

        cookieval1 =urllib.parse.unquote(cookie[2]['value'])
        headers = {
            'Host': 'v.7cyd.com',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac 05 X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
            'Accept':'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With':'XMLHttpRequest',
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin':'https://v.7cyd.com',
            'Sec-Fetch-Site':'same-origin',
            'Sec-Fetch-Mode':'cors',
            'Accept-Encoding':'gzip, deflate, br',
            'Cookie':'_51cke_=;'+cookiename+'='+cookieval+';'+cookiename1+'='+cookieval1
        }
        re=requests.post('https://v.7cyd.com/vip/api_vip_vp_a8g.php',  data=poststr,headers=headers,verify=False)

        return re.content

if __name__ == '__main__':
    # 连接database
    conn = pymysql.connect(host='localhost', user ='rootaw', password ='rootaw', database ='rootaw', charset ='utf8')
    # 得到一个可以执行SQL语句的光标对象
    cursor = conn.cursor()

    # 定义要执行的SQL语句

    for i in range(0,100):

        sql = 'select vod_url from ff_vod limit %d,1' % i
        # 执行SQL语句
        cursor.execute(sql)
        strUrls=cursor.fetchall()
        listUrls=str(strUrls).replace(',','').replace(')','').replace('\'','').split('$')
        for url in listUrls:
            if(url.find('iqiyi.com')!=-1):
                urlhtml=url.split('\\r')[0]
                m3u8=str(getM3U8(urlhtml))
                #m3u8='b\'{"play":"dp","title":null,"code":200,"success":1,"lg":"4","cache":"iqiyi","url":"https:\\/\\/v.7cyd.com\\/api\\/data\\/iqiyi\\/d390b7a3887d06eb2d1d82497b970634.m3u8","type":"m3u8"}\''
                if(m3u8.find('.m3u8')!=-1&m3u8.find('http')!=-1):
                    m3u8=m3u8[m3u8.find('http'): m3u8.find('.m3u8')+5].replace('/','').replace('\\\\','\\')
                    print(m3u8)  #m3u8连接是动态显示的，加密方式需要继续破解
    # 关闭光标对象
    cursor.close()
    # 关闭数据库连接
    conn.close()



