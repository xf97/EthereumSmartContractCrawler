'''
该文件用于获取要爬取源代码的
500个合约的URL，
使用方法，调用getUrl函数
'''

import requests
import re 
import os

#给定url
def getWebContent(url):
	try:
		r = requests.get(url, timeout = 50)
		r.raise_for_status()	#如果状态码不是200，则引发异常
		r.encoding = r.apparent_encoding	#给定正确编码
		return r.text
	except:
		return "爬取网页出现异常.\n"

#通过给定的网页文本，摘录出100个合约地址，返回列表
def getContractsAddr(text):
	try:
		regex = re.compile(r"/address/0x\w{40}#code")
		ilist = regex.findall(text)
		return ilist
	except:
		print("解析网页出现异常.\n")
		return list()

#通过给定的网页文本，依次摘录出100个合约使用的编译器，返回列表
#未完成
def getContractCompiler(text):
	try:
		regex = re.compile(r"<td>Solidity(.)*?</td>")
		ilist = regex.findall(text)
		return ilist
	except:
		print("获得合约编译器出现错误.\n")
		return list()

#通过给定的网页文本，获得100个合约的存款，返回列表
#未完成
def getContractBalance(text):
	try:
		regex = re.compile()
	except:
		pass



#将给定列表写入文件
def writeInFile(ilist, name, prefix = ""):
	filename = name
	f = open(filename, "a")
	for add in ilist:
		addr = prefix + str(add) + "\n"
		f.write(addr)
	f.close()

#功能集成函数
def getUrl(address_path):
	path = r"https://etherscan.io/contractsVerified/"
	filename = address_path + "\\" + "address.txt"
	#如果原地址文件已存在，则删除后再写入
	if os.path.isfile(filename):
		print("原地址文件已删除.")
		os.remove(filename)
	for i in range(1,6):
		try:
			url = path + str(i) + "?ps=100"
			print("当前爬取页面url: ", url)
			text = getWebContent(url)
			li = getContractsAddr(text)
			writeInFile(li, filename, "etherscan.io")
			print("\r获取url进度: {}%".format((i/5)*100))
		except:
			print("出现检索错误.")
			continue
	print("获取url完成.")




#单元测试代码
if __name__ == "__main__":
	getUrl()


