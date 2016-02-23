import urllib.request
import urllib
import re
import time

def web(url):
	#url='http://www.xuexiku.com.cn/Index.html'
	content=urllib.request.urlopen(url).read().decode('gbk')

	num=re.findall(r'(?<=>)\d{1,5}(?=</i>)', content)
	name=re.findall(r'(?<=title=").*?(?=" target)', content)
	web=re.findall(r'(?<=href=").*?(?=" title)', content)[95:]

	# for x in range(len(name)):
	# 	print(name[x])
	# 	print('http://www.xuexiku.com.cn'+web[x])
	return web


def link_web(url):
	#url='http://www.xuexiku.com.cn/html/zonghe/moxingcaizhi/38668.html'
	content=urllib.request.urlopen(url).read().decode('gbk')

	size=re.findall(r'(?<=center">).*?(?=</td>)', content)
	name=[]
	link=[]
	data=re.findall(r'(?<=a href=")[ed2k].*?(?=</a>)', content)
	for each_data in data:
		each_data=each_data.split('"')
		link.append(each_data[0])
		name.append(each_data[1][2:])
		
	for x in range(len(name)):
		print('资源:'+name[x])
		print('大小:'+size[x])
		print('下载地址:'+link[x]+'\n')
		# with open('xuexiku.txt','a') as f:
		# 	f.write('资源:'+name[x]+'\n')
		# 	f.write('大小:'+size[x]+'\n')
		# 	f.write('下载地址:'+link[x]+'\n\n')


if __name__=='__main__':
	start=time.clock()
	url='http://www.xuexiku.com.cn/Index.html'
	web=web(url)
	for each_web in web:
		start1=time.clock()
		link_web('http://www.xuexiku.com.cn'+each_web)
		end1=time.clock()
		# print('此页面抓取时间:%s Seconds' %(end1-start1)+'\n')
	end=time.clock
	print('一共抓取时间:%s Seconds' %(end-start))