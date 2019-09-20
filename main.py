'''
爬取智能合约主程序
用于驱动程序
'''

import getContractUrl
import getSourceCode
import os

def main():
	path = input("请输入智能合约源文件存入的路径: ")
	address_path = input("请输入合约url地址文件的保存位置: ")
	if os.path.exists(path) == False or os.path.exists(address_path) == False:
		print("错误的路径, 请检查后重新输入.\n")
		return
	#获取500个url
	print("开始获取合约地址Url.")
	getContractUrl.getUrl(address_path)
	count = 0
	exc = 0
	#对每一个获取的地址，获取源代码
	for addr in open( address_path + "\\address.txt", "r"):
		if addr == "":
			count = count + 1
			continue
		else:
			try:
				getSourceCode.getsourcecode(addr, path)
				count = count + 1
			except:
				exc = exc + 1
				print("获取源码出现异常, 数量:", exc)
				count = count + 1
		print("\r爬取进度: {:.2f}%".format((count / 500) * 100), end=" ")
	print("All done.")

main()

