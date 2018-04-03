#coding=utf-8
import sys
import jieba
from snownlp import SnowNLP

a='展开全文'
b='展开全文'
flag=b.startswith(a)
print flag

l=[['展开全文',0.33]]
print(l[0][0])
print(l[0][1])
f = open('test.txt', 'w')
f.write(l[0][0])
f.write(str(l[0][1]))
f.close()

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
c='该干滴都干啦！在东乌旗一样的天气里吃了完美早餐喝了观赏性奶昔一起读了书之后去看了演出（虽然看了之后更加更加想去看于意 哭哭）看电影了逛街了吃虾吃虾涮了午夜聊天了睡懒觉了用音响了吃了完美的外卖看着高等之后试了喜欢的裤子听了于意的单口相声赶着火车也狂骂操蛋的破烂地方然后顺其自然的开心 ...展开全文c'
c=c[:c.__len__()-13]
cc=jieba.cut(c)
print ','.join(cc)
sc=SnowNLP(c)
print ','.join(sc.words)

a='0'.encode('utf-8')
print int(a)
print c.decode('utf-8')


