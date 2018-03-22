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

if __name__=="__main__":
    x=WeiboDataGet()
    x.Connect('http://weibo.com')
    x.Close()