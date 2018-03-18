from snownlp import SnowNLP
import pymysql

f=open('out1.txt','r')
text=f.read()
# print(text)

f.close()
s = SnowNLP(text)

# for sentence in s.sentences:
#     print(sentence)

for word in s.words:
    print(word)
