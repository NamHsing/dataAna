from selenium import webdriver
import time
import pymysql

dr = webdriver.Firefox()#executable_path='~/PycharmProjects/webtest')
dr.get('http://weibo.com')
dr.implicitly_wait(10)

try:
    elem1=dr.find_element_by_xpath('//input[@node-type="username"]')
    elem1.clear()
    dr.implicitly_wait(10)
    elem1.send_keys("flowerysai@gmail.com")
    elem2=dr.find_element_by_xpath('//input[@node-type="password"]')
    dr.implicitly_wait(10)
    elem2.send_keys("")
    time.sleep(5)
    dr.implicitly_wait(10)
    elem3=dr.find_elements_by_xpath('//a[@action-type="btn_submit"]/span[@node-type="submitStates"]')
    dr.implicitly_wait(10)
    time.sleep(5)
    elem3[0].click()
    dr.implicitly_wait(10)

    time.sleep(5)

except:
    print 'time out!'

# time.sleep(20)

# con=pymysql.connect(host='123.206.55.50', port=3306, user='sa', passwd='sail1989', db='test', charset='utf8')
# cursor=con.cursor()
f=open('out.txt','w')
outtxt=""

j=1

while j<21:
    dr.get('https://s.weibo.com/weibo/%25E7%259C%258B%25E7%2594%25B5%25E5%25BD%25B1&region=custom:11:1000&typeall=1&suball=1&page='+str(j))
    j=j+1
    dr.implicitly_wait(10)
    time.sleep(5)

    try:
        datas=dr.find_elements_by_xpath('//div[@node-type="feed_list"]/div')
    except:
        continue


    leng=len(datas)

    for data in datas:
        # temp=data.find_element_by_xpath('./div[@action-type="feed_list_item"]/div[@class="WB_feed_detail clearfix"]/dl[@class="W_texta"]/div[@class="feed_list feed_list_new W_linecolor"]/div[@class="content clearfix"]/div[@class="feed_content wbcon"]/p[@class="comment_txt"]').text.encode('utf-8')

        tempElem=data.find_element_by_xpath('.//p[@class="comment_txt"]')
        temp=''


        temp=tempElem.text.encode('utf-8')
        print temp
        # sqlsen="INSERT INTO `wbc`(`content`, `var`) VALUES ('"+temp+"',0)"
        # cursor.execute(sqlsen)
        outtxt=outtxt+temp+"\r\n"

f.write(outtxt)
f.close()

# con.commit()
# cursor.close()
# con.close()
print 'Browser will close'
dr.quit()
print 'Browser closed'
