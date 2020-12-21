# -*- coding:utf-8 -*-
import os,time
def Files(id):
   str = [
       '',
       'http://pypi.douban.com/simple/',
       'http://mirrors.aliyun.com/pypi/simple/',
       'https://pypi.tuna.tsinghua.edu.cn/simple/',
       'http://pypi.mirrors.ustc.edu.cn/simple/',
       'http://pypi.hustunique.com/'
   ]
   str1 =[
       '',
       'pypi.douban.com',
       'mirrors.aliyun.com',
       'pypi.tuna.tsinghua.edu.cn',
       'pypi.mirrors.ustc.edu.cn',
       'pypi.hustunique.com'
   ]
   file_str ="[global]\nindex-url = "+str[id]+"\n\n[install]\n"+"trusted-host = "+ str1[id]
   System_path = os.environ['AppData']+"\\"+"pip\\"
   fileName = "pip.ini"
   try:
       if os.path.exists(System_path+fileName) and os.path.exists(System_path) :
           with open(file=System_path+fileName,mode='w') as f1:
                f1.write(file_str)
                f1.close()
       else:
           os.mkdir(path=System_path)
           with open(file=System_path+fileName,mode='w+') as f1:
               f1.write(file_str)
               f1.close()
       print("更换成功!")
   except Exception as e:
       print("更换失败,原因+"+e)
def run():
    print("----------------------------------------------------------")
    print("1、豆瓣 http://pypi.douban.com/simple/")
    print("2、阿里云 http://mirrors.aliyun.com/pypi/simple/")
    print("3、清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/")
    print("4、中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/")
    print("5、华中科技大学 http://pypi.hustunique.com/")
    print("----------------------------------------------------------")
    s = int(input("请输入源序列:"))
    if s < 6 and s > 0:
        Files(s)
    else:
        print("输入错误")
        exit(5)
if __name__ == '__main__':
    run()