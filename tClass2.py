#coding=utf-8
from selenium import webdriver
import time
import pymysql
from snownlp import SnowNLP
import sys
from selenium.common.exceptions import NoSuchElementException
class WeiboDataGet():

    def __init__(self):
        self.driver = webdriver.Firefox()

    def Connect(self,address):
        self.driver.get('http://weibo.com')
        self.driver.implicitly_wait(10)

    def Close(self):
        print 'Browser will close'
        self.driver.quit()
        print 'Browser closed'

    def Login(self):
        try:
            elem1 = self.driver.find_element_by_xpath('//input[@node-type="username"]')
            elem1.clear()
            self.driver.implicitly_wait(10)
            elem1.send_keys("flowerysai@gmail.com")
            elem2 = self.driver.find_element_by_xpath('//input[@node-type="password"]')
            self.driver.implicitly_wait(10)
            elem2.send_keys("")
            time.sleep(5)
            self.driver.implicitly_wait(10)
            elem3 = self.driver.find_elements_by_xpath('//a[@action-type="btn_submit"]/span[@node-type="submitStates"]')
            self.driver.implicitly_wait(10)
            time.sleep(5)
            elem3[0].click()
            self.driver.implicitly_wait(10)

            time.sleep(30)

        except:
            print 'time out!'

        # time.sleep(20)

    def GetData(self,pages):
        non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
        j=1
        self.textData=[]
        while j < pages:
            self.driver.get(
                'https://s.weibo.com/weibo/%25E7%259C%258B%25E7%2594%25B5%25E5%25BD%25B1&region=custom:11:1000&typeall=1&suball=1&page=' + str(
                    j))
            j = j + 1
            self.driver.implicitly_wait(10)
            time.sleep(5)

            try:
                datas = self.driver.find_elements_by_xpath('//div[@node-type="feed_list"]/div')
            except:
                continue

            leng = len(datas)

            for data in datas:
                try:
                    data.find_element_by_xpath(
                        ".//div[@class='feed_content wbcon']/p[@class='comment_txt']/a[@class='WB_text_opt']").is_displayed()
                    flag = True
                except:
                    flag = False
                    # 如果需要展开全文，点击后提取文本
                self.driver.implicitly_wait(10)
                if (flag and data.find_element_by_xpath(
                    ".//div[@class='feed_content wbcon']/p[@class='comment_txt']/a[@class='WB_text_opt']").text.encode(
                    'utf-8').startswith(
                    '展开全文c')):
                    self.driver.implicitly_wait(10)
                    data.find_element_by_xpath(
                        ".//div[@class='feed_content wbcon']/p[@class='comment_txt']/a[@class='WB_text_opt']").click()
                    time.sleep(1)
                    WBNR = data.find_element_by_xpath(
                        ".//div[@class='feed_content wbcon']/p[@node-type='feed_list_content_full']").text.encode(
                        'utf-8')
                    WBNR = WBNR[:WBNR.__len__() - 13]
                    # 没有展开全文，直接提取微博内容
                else:
                    WBNR = data.find_element_by_xpath(
                        ".//div[@class='feed_content wbcon']/p[@class='comment_txt']").text.encode('utf-8')
                #获取时间戳
                timestamp=data.find_element_by_xpath(
                    './/a[@node-type="feed_list_item_date"]').get_attribute('date').encode('utf-8')
                timestamp=timestamp[:timestamp.__len__()-3]
                #获取转发数
                try:
                    zf=data.find_element_by_xpath(
                        './/div[@class="feed_action clearfix"]/ul/li[2]/a/span/em').text.encode('utf-8')
                except NoSuchElementException:
                    zf=''
                if zf=='':
                    zf='0'
                #获取评论数
                try:
                    pl=data.find_element_by_xpath(
                        './/div[@class="feed_action clearfix"]/ul/li[3]/a/span/em').text.encode('utf-8')
                except NoSuchElementException:
                    pl=''
                if pl=='':
                    pl='0'
                #获取点赞数
                try:
                    dz=data.find_element_by_xpath(
                        './/div[@class="feed_action clearfix"]/ul/li[4]/a/span/em').text.encode('utf-8')
                except NoSuchElementException:
                    dz=''
                if dz=='':
                    dz='0'
                lctime=time.strftime("%Y%m%d%H%M%S",time.localtime(int(timestamp)))
                print [WBNR,zf,pl,dz,lctime,timestamp]
                self.textData.append([WBNR,zf,pl,dz,lctime,timestamp])
                break

    def GetWeiboData(self,address):
        self.textWeiboData=[]
        self.driver.get(address)
        self.driver.implicitly_wait(10)
        time.sleep(5)

        try:
            datas = self.driver.find_elements_by_xpath('//div[@node-type="feed_list"]/div')
        except:
            return

        for data in datas:
            try:
                data.find_element_by_xpath(
                    ".//div[@class='feed_content wbcon']/p[@class='comment_txt']/a[@class='WB_text_opt']").is_displayed()
                flag = True
            except:
                flag = False
                # 如果需要展开全文，点击后提取文本
            self.driver.implicitly_wait(10)
            if (flag and data.find_element_by_xpath(
                ".//div[@class='feed_content wbcon']/p[@class='comment_txt']/a[@class='WB_text_opt']").text.encode(
                'utf-8').startswith(
                '展开全文c')):
                self.driver.implicitly_wait(10)
                data.find_element_by_xpath(
                    ".//div[@class='feed_content wbcon']/p[@class='comment_txt']/a[@class='WB_text_opt']").click()
                time.sleep(1)
                WBNR = data.find_element_by_xpath(
                    ".//div[@class='feed_content wbcon']/p[@node-type='feed_list_content_full']").text.encode(
                    'utf-8')
                WBNR = WBNR[:WBNR.__len__() - 13]
                # 没有展开全文，直接提取微博内容
            else:
                WBNR = data.find_element_by_xpath(
                    ".//div[@class='feed_content wbcon']/p[@class='comment_txt']").text.encode('utf-8')

            print(WBNR)

            self.textWeiData.append([WBNR])


    def WriteFile(self,filePath):
        f = open(filePath, 'w')
        for text in self.textData:
            f.write(text[0])
            f.write(str(text[1]))
        f.close()

    def DataBaseOut(self):
        con=pymysql.connect(host='123.206.45.78', port=3306, user='sa', passwd='sail1989', db='test', charset='utf8')
        cursor=con.cursor()
        for text in self.textData:
            sqlsen=\
                "INSERT INTO `wbdata`(`content`, `zf`,`pl`,`dz`,`sendts`,`sendtsint`) VALUES ('"+\
                text[0]+"',"+text[1]+","+text[2]+","+text[3]+",'"+text[4]+"',"+text[5]+")"
            cursor.execute(sqlsen)
        con.commit()
        cursor.close()
        con.close()

if __name__=="__main__":
    x=WeiboDataGet()
    #x.Connect('http://weibo.com')
    #x.Login()
    #time.sleep(20)
    x.GetData(2)
    #x.WriteFile('out.txt')
    x.DataBaseOut()
    x.Close()