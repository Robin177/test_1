import unittest
import time
from Report.HTMLTestRunner import HTMLTestRunner

# 加载当前目录
test_dir="./"
# 加载当前目录下iweb开头的.py文件
discover=unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")
if __name__ == '__main__':
    # 定义报告目录
    file_dir="../Report/"
    # 定义报告名称格式
    nowtime=time.strftime("%Y-%m-%d %H_%M_%S")
    # 报告完整路径和名称
    file_name=file_dir+nowtime+"Report.html"
    with open(file_name,"wb")as f:
        # 实例化HTMLTestRunenr对象，传入报告文件流f
        runner=HTMLTestRunner(stream=f,title="Web自动化测试报告",description="操作系统:win10,开发语言:Python浏览器：火狐浏览器,",save_last_try = False)
        runner.run(discover)
