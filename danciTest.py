import requests,json,time
headers={
    'referer': 'https://www.shanbay.com/bdc/client/vocabtest/welcome',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
def english_select():
    url='https://www.shanbay.com/api/v1/vocabtest/category/'
    res=requests.get(url,headers=headers)
    resjson=json.loads(res.text)
    i=int(input('''请输入你选择的词库编号，按Enter确认.
        1，GMAT  2，考研  3，高考  4，四级  5，六级
        6，英专  7，托福  8，GRE  9，雅思  10，任意
        >'''))
    ciku=resjson['data'][i-1][0]
    #print(ciku)
    Test(ciku)
def Test(ciku):
    url='https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category='+str(ciku)
    res=requests.get(url,headers=headers)
    resjson=json.loads(res.text)
    f=0 #题号
    word_ranks=[]
    know_list=[]#认识的词汇
    no_list=[]#不认识的词汇
    for x in resjson['data']:
        f=f+1
        print(str(f)+'. '+x['content'])
        word_ranks.append(x['rank'])
        m=input('\n 这个单词你认识吗，输入Y/N >')
        if m== 'Y' :
            know_list.append(x)
        else:
            no_list.append(x)
    # for x in know_list:
    #     print(x)
    # print('不认识的词汇：')
    # for x in no_list:
    #     print(x)
    select_know(know_list,word_ranks,ciku,no_list)
def select_know(know_list,word_ranks,ciku,no_list):
    print('接下来选出你认识的单词的词意：')
    f=0#题号
    not_list=[]
    right_ranks=[]
    final_list=[]
    
    for x in know_list:
        f=f+1
        print(str(f)+'. '+x['content'])#单词
        print('A. 词意：'+x['definition_choices'][0]['definition'])
        print('B. 词意：'+x['definition_choices'][1]['definition'])
        print('C. 词意：'+x['definition_choices'][2]['definition'])
        print('D. 词意：'+x['definition_choices'][3]['definition'])
        a=input('你的选择是：')

        dict={
            'A':x['definition_choices'][0]['rank'],
            'B':x['definition_choices'][1]['rank'],
            'C':x['definition_choices'][2]['rank'],
            'D':x['definition_choices'][3]['rank']
        }
        dict_rank={
            x['definition_choices'][0]['rank']:x['definition_choices'][0]['definition'],
            x['definition_choices'][1]['rank']:x['definition_choices'][1]['definition'],
            x['definition_choices'][2]['rank']:x['definition_choices'][2]['definition'],
            x['definition_choices'][3]['rank']:x['definition_choices'][3]['definition']
        }
        if a!='':
            if dict[a]==x['rank']:
                print('回答正确。')
                right_ranks.append(x['rank'])
            else:
                print('回答错误。 正确答案：'+dict_rank[x['rank']])
                final=x['content']+'解释：'+dict_rank[x['rank']]
                not_list.append(str(final))
        else:
            pass
    #存不认识的词和意思
    for x in no_list: 
        dict_rank={ #通过rank值确定 正确意思
            x['definition_choices'][0]['rank']:x['definition_choices'][0]['definition'],
            x['definition_choices'][1]['rank']:x['definition_choices'][1]['definition'],
            x['definition_choices'][2]['rank']:x['definition_choices'][2]['definition'],
            x['definition_choices'][3]['rank']:x['definition_choices'][3]['definition']
        }
        final=x['content']+'  解释：'+dict_rank[x['rank']]
        final_list.append(str(final))
    #将list转换成str 
    word_ranks= ','.join('%s' %id for id in word_ranks)
    right_ranks=','.join('%s' %id for id in right_ranks)
    next(ciku,right_ranks,word_ranks,not_list,final_list)

def next(ciku,right_ranks,word_ranks,not_list,final_list):
    url='https://www.shanbay.com/api/v1/vocabtest/vocabularies/'
    Payload={
        'category':ciku,
    'right_ranks':right_ranks,
    'word_ranks':word_ranks
    }
    res=requests.post(url,data=Payload,headers=headers)
    jsonres=json.loads(res.text)

    print('你的词汇量约为：'+str(jsonres['data']['vocab']))
    print(jsonres['data']['comment'])
    x=input('是否打印错词集：Y/N>')
    if x=='Y':
        k=open('错题集.txt','a+',encoding='utf-8')
        try:
            k.write('你不认识的词汇：\n')
            f=0
           
            for x in final_list:
                f=f+1
                k.write(str(f)+'. '+x+'\n')
            k.write('\n你选错的词汇：\n')
            n=0
            for x in not_list:
                n=n+1
                k.write(str(n)+'. '+x+'\n')
            print('打印成功，存在当前目录下。')
        except :
            pass
        k.close()
       

print('五分钟，测试英语词汇量。')
english_select()