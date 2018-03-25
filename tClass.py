from selenium import webdriver
import time
import pymysql

class WeiboDataGet():

    def __init__(self):
        self.driver = webdriver.Firefox()

    def Connect(self,address):
        self.driver.get('http://weibo.com')

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

            time.sleep(5)

        except:
            print 'time out!'

        # time.sleep(20)

    def GetData(self,pages):
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
                # temp=data.find_element_by_xpath('./div[@action-type="feed_list_item"]/div[@class="WB_feed_detail clearfix"]/dl[@class="W_texta"]/div[@class="feed_list feed_list_new W_linecolor"]/div[@class="content clearfix"]/div[@class="feed_content wbcon"]/p[@class="comment_txt"]').text.encode('utf-8')

                tempElem = data.find_element_by_xpath('.//p[@class="comment_txt"]')
                temp = ''

                temp = tempElem.text.encode('utf-8')
                #print temp
                # sqlsen="INSERT INTO `wbc`(`content`, `var`) VALUES ('"+temp+"',0)"
                # cursor.execute(sqlsen)
                #outtxt = outtxt + temp + "\r\n"
                self.textData.append(temp)

    def WriteFile(self,filePath):
        f = open(filePath, 'w')
        for text in self.textData:
            f.write(text)
        f.close()

    def DataBaseOut(self):
        con=pymysql.connect(host='123.206.45.78', port=3306, user='sa', passwd='sail1989', db='test', charset='utf8')
        cursor=con.cursor()
        for text in self.textData:
            sqlsen="INSERT INTO `wbc`(`content`, `var`) VALUES ('"+text+"',0)"
            cursor.execute(sqlsen)
        con.commit()
        cursor.close()
        con.close()

if __name__=="__main__":
    x=WeiboDataGet()
    x.Connect('http://weibo.com')
    x.GetData(2)
    x.WriteFile('out.txt')
    x.Close()