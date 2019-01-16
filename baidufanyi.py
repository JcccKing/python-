import requests,json,pyperclip
yuanwen =input('输入内容：')
url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
data={
    'i': yuanwen,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '15473834586710',
    'sign': '7e71e2eb05a997e17d91240eca69c7f3',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTIME',
    'typoResult': 'false'
}
headers={
    'Referer': 'http://fanyi.youdao.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
r = requests.post(url,data=data,headers=headers)
answer=json.loads(r.text)
print ('翻译的结果是：'+answer['translateResult'][0][0]['tgt'])

#复制到剪贴板
pyperclip.copy(answer['translateResult'][0][0]['tgt'])
input('输入enter结束。')