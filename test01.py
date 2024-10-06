import os

#返回系统相关信息
print(os.name)
#返回路径分隔符
print(os.sep)
#返回当前平台使用的行终止符
print(repr(os.linesep))
#返回当前工作目录
print(os.getcwd())
#改变当前工作目录
# os.chdir(r'/Users/zhengzhen/Desktop/pythonTest/a123')
#当前工作路径下创建和删除文件夹
os.mkdir('test')
os.rmdir('test')