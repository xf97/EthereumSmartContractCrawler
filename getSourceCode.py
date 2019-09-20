'''
该文件接收含有合约源代码的url,
从中获取源码, 保存为文件.
默认命名方式为: 合约地址.sol
'''

from bs4 import BeautifulSoup
import requests
import os
import re

def getCode(_url):
	#拼接出正确的url
	url = "https://" + _url
	#获得指定网页的文本
	r = requests.get(url, timeout = 50)
	r.raise_for_status()	#如果状态码不是200，则引发异常
	#r.encoding = "utf-8"
	r.encoding = r.apparent_encoding	#给定正确编码
	#判断是否是多文件形式的solidity
	if demo.find("Multiple") != -1:
		#本程序暂不读取多文件形式的solidity源代码
		return ""
	#煲汤
	soup = BeautifulSoup(demo, "html.parser")
	#获得源代码
	#第一个pre标签中的string就是源代码
	pre = soup.find("pre", id="editor")
	text = str(pre)
	#去掉首尾的pre标签
	begin = text.find("/**")
	end = text.find("</pre>")
	#获得最终字符串
	return text[begin : end]

#从给定的url中摘取出地址
#拼接文件名
def getFileName(_url):
	try:
		regex = re.compile(r"0x(\w){40}")
		s = regex.search(_url)
		return s.group(0) + ".sol"
	except:
		print("获得文件名错误. 出错url: ",_url)
		return "error.sol"

#根据给定的文件名和给定的源代码字符串
#写入到文件中
def codesToFile(filename, code, _path = ""):
	path = _path + "\\" + filename
	if os.path.isfile(path):
		print("该文件已存在: ", filename)
	else:
		f = open(path, "w", encoding = "utf-8")
		f.write(code)
		f.close()

def getsourcecode(url, path = ""):
	#判断该文件是否已经存在，若存在则不扒取源码
	if isFileExists(url, path):
		return
	code = getCode(url)
	if code == "":
		print("不支持多文件格式的solidity合约爬取: ", url)
		return
	else:
		filename = getFileName(url)
		codesToFile(filename, code, path)

#该函数用于检测文件是否已经存在
#存在则跳过，加快爬取进度
def isFileExists(url, path):
	#截取文件名
	filename = url[-47:-5]
	#获得目录下文件名列表
	filelist = os.listdir(path)
	#遍历寻找
	for i in filelist:
		if filename in i:
			return True
	return False 



#单元测试代码
if __name__ == "__main__":
	url = "etherscan.io/address/0x4abe410ae11835263203d4ca8ee222a38725396b#code"
	path = r"D:\智能合约源代码合约_爬虫爬取"
	code = getCode(url)
	print("Codes get.")
	if code == "":
		print("不支持多文件格式的solidity合约爬取: ", url)
	else:
		filename = getFileName(url)
		print("Filename get.")
		codesToFile(filename, code, path)
		print(filename, " Done.")
