#近一百期双色球开奖号
import urllib.request
import urllib
import re

def get_mes():
	url='http://baidu.lecai.com/lottery/draw/list/50?type=latest&num=100'
	content=urllib.request.urlopen(url).read().decode('utf-8')
	num=re.findall(r'(?<=target="_blank">)\d{1,10}(?=</a>)', content) #开奖期号

	date_time=re.findall(r'(?<=<td>)\d{4}[-]\d{2}[-]\d{2}.*?(?=</td>)', content) #开奖日期

	data_num=re.findall(r'(?<=<em>)\d*?(?=</em>)', content) #开奖号码
	temp=[]
	data=[]
	for x in range(0,len(data_num),7):
		temp=data_num[x:x+7:1]
		data.append(temp)
	data_num=data

	return num,date_time,data_num

def show(num,date_time,data_num):
	data_dict1=dict(zip(num,date_time))
	data_dict2=dict(zip(num,data_num))
	print('  期号\t'+'\t\t\t开奖日期\t'+'\t\t\t\t\t 开奖号码')
	for x in range(len(num)):
		print(str(num[x])+'\t',end='')
		print('\t\t'+str(data_dict1[num[x]]),end='\t\t\t')
		for y in data_dict2[num[x]]:
			print(str(y),end='\t')
		print('\n')

if __name__=='__main__':
	num=get_mes()[0]
	date_time=get_mes()[1]
	data_num=get_mes()[2]
	show(num,date_time,data_num)
	input('输入回车结束...')