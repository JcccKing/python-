from urllib import request
from urllib import parse
import json
import random
import _md5
import hashlib
 
 
def process(Request_URL,Form_Data):
    # 使用urlencode方法转换标准格式
    data = parse.urlencode(Form_Data).encode('utf-8')
    # 传递Request对象和转换完格式的数据
    response = request.urlopen(Request_URL, data)
    # 读取信息并解码
    html = response.read().decode('utf-8')
    # 使用JSON
    translate_results = json.loads(html)
    return  translate_results
 
def Jinshan(onlyone=1,word=None):
    Request_URL = 'http://fy.iciba.com/ajax.php?a=fy'
    #创建Form_Data字典，存储Form Data
    Form_Data = {'f' : 'auto',
                 't' : 'auto'}
    if onlyone==0:
        Form_Data['w']=word
        translate_results = process(Request_URL, Form_Data)
        # 找到翻译结果
        if 'out' in translate_results['content']:
            translate_results = translate_results['content']['out']
        else:
            translate_results = translate_results['content']['word_mean']
        # 打印翻译信息
        print("金山翻译结果是：%s" % translate_results)
        return
    print('正在使用金山词霸\n')
    while 1:
        Form_Data['w'] = input("请输入要翻译的内容:")
        if Form_Data['w'].lower()=='exit':
            print('已退出金山词霸')
            return
        translate_results=process(Request_URL,Form_Data)
        #找到翻译结果
        if 'out' in translate_results['content']:
            translate_results = translate_results['content']['out']
        else:
            translate_results = translate_results['content']['word_mean']
        #打印翻译信息
        print("金山翻译结果：%s" % translate_results)
 
def Youdao(onlyone=1,word=None):
    #对应上图的Request URL
    Request_URL = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    #创建Form_Data字典，存储Form Data
    Form_Data = {'type' : 'AUTO',
                 'from' : 'AUTO',
                 'to'   : 'AUTO',
                 'smartresult':'dict',
                 'doctype': 'json',
                 'version': '2.1',
                 'keyfrom': 'fanyi.web',
                 'action' : 'FY_BY_REALTIME'
                 }
 
    if onlyone==0:
        Form_Data['i']=word
        translate_results = process(Request_URL, Form_Data)
        # 找到翻译结果
        result = translate_results['translateResult'][0][0]['tgt']
        # 打印翻译信息
        print("有道翻译结果：%s" % result)
        return
    print('正在使用有道翻译\n')
    while 1:
        Form_Data['i'] = input("请输入要翻译的内容:")
        if Form_Data['i'].lower()=='exit':
            print('已退出有道翻译')
            return
        translate_results = process(Request_URL, Form_Data)
        #找到翻译结果
        result = translate_results['translateResult'][0][0]['tgt']
        # 打印翻译信息
        print("有道翻译结果：%s" % result)
 
def Baidu(onlyone=1,word=None):
    Request_URL = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
    # 创建Form_Data字典，存储Form Data
    Form_Data = {'from' : 'auto',
                 'to'   : 'zh',
                 'appid':'20151113000005349',
                 'salt': random.randint(32768, 65536).__str__(),
                 }
    secretKey = 'osubCEzlGjzvw8qdQc41'
 
    if onlyone==0:
        Form_Data['q']=word
        sign = Form_Data['appid'] + Form_Data['q'] + Form_Data['salt'] + secretKey
        Form_Data['sign'] = hashlib.md5(sign.encode(encoding='gb2312')).hexdigest()
        translate_results = process(Request_URL, Form_Data)
        # 找到翻译结果
        result = translate_results['trans_result'][0]['dst']
        # 打印翻译信息
        print("百度翻译结果：%s" % result)
        return
    print('正在使用百度翻译\n')
    while 1:
        Form_Data['q'] = input("请输入要翻译的内容:")
        if Form_Data['q'].lower()=='exit':
            print('已退出百度翻译')
            return
        sign =Form_Data['appid'] + Form_Data['q'] + Form_Data['salt'] + secretKey
        Form_Data['sign'] = hashlib.md5(sign.encode(encoding='gb2312')).hexdigest()
 
        translate_results = process(Request_URL, Form_Data)
        #找到翻译结果
        #print(translate_results)
        result = translate_results['trans_result'][0]['dst']
 
        # 打印翻译信息
        print("\n百度翻译结果：%s" % result)
 
def all():
    while 1:
        word=input("请输入要翻译的内容：")
        if word=='exit':
            print('已退出')
            return
        Youdao(0,word)
        Jinshan(0,word)
        Baidu(0,word)
 
if __name__ == '__main__':
    soft=input("请选择要使用的翻译软件：1.有道翻译 2.金山词霸 3.百度翻译 4.都看一下呗")
    if soft=='1':
        Youdao()
    elif soft=='2':
        Jinshan()
    elif soft == '3':
        Baidu()
    elif soft=='4':
        all()
    else:
        print('hhh,您这输的小的没设置的选项啊')
 
    print("白白，欢迎下次再来使用")
