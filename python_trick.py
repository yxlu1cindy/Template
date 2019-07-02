#字典相关

# 对字典进行排序：
works = {0:{"company":xxx,"end":"2016/7",job:"developer"},1:{"company":xxx,"end":"2018/7",job:"designer"}

# 对结束时间进行排序:
works = dict(sorted(works.items(), key=lambda d: d[1]['end'], reverse=True))

# 对字典的key进行排序:
works = dict(sorted(works.items(), key=lambda d: d[0], reverse=True))

# list不能作为字典的key,所以一半存储是会变成str:

# 列表用第二个元素进行排序
def takeSecond(elem):
    return elem[1]
    
#或者
import operator
list1 = sorted(csv1, key=operator.itemgetter(1, 2)) #对两列排序 
#或者             
sorted(list, key=lambda x: (x[0], -x[1])) #对两列排序 


#str2list:
eval()

#win32com:
#可以执行word相关，python2时对于中文的处理有些复杂

#'gbk' codec can't encode character '\xa9' in position 2604: illegal multibyt
#错误原因跟编码有关，试下来最好的解决方式：
fh = open(path+"/txt/"+filename, 'wb')   #'b'代表着用二进制打开
fh.write(text_all.encode("utf-8"))  # 'encode' 转成2进制，'decode'2进制转成字符串

#python2 vs python3：
#- print
#- input的时候python2需要手动加上''
#- python3 默认用utf-8，python2的话要设置sys.setdefaultencoding
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
reload(sys)

#word转txt有可能会丢失文本框之内的字符，但先转成pdf的话就可以保留
             
#怎么提高pandas赋值的速度（新版本好像无所谓了）：
             #不要用会建立副本的method,用ix  ：https://stackoverflow.com/questions/26660040/faster-way-to-assign-new-values-in-pandas-dataframe
             #https://stackoverflow.com/questions/31569384/set-value-for-particular-cell-in-pandas-dataframe-with-iloc#

#pdf2txt:
#python3的话有pdfminer6和pdfplumber，pdfminer只支持python2,其中pdfplumber虽然基于pdfminer，但解析的顺序可能会和pdfminer的有所不同

#pymongo可以连接MongoDB:
conn11 = MongoClient('mongodb://user:password@address:port/admin')  以admin身份登入

#Agglomorative可以对图像进行聚类

ord("char") #得到对应的ascii码
             
# 对数组按第二列进行排序
return_np = return_np[return_np[:,1].argsort()]

# 直接range就逆序循环
range(10,0,-1)  => #含10无1
