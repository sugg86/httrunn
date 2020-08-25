#author:mcc
#project:httrun
#data:2020/8/24
#time:16:44




pip install httprunner == 3.1.1

hrun：httprunner 的缩写，功能与 httprunner 完全相同
hmake：httprunner make的别名，用于将YAML/JSON测试用例转换为pytest文件
har2case：辅助工具，可将标准通用的 HAR 格式（HTTP Archive）转换为YAML/JSON格式的测试用例 -2y/-2j




项目结构
---------------------------------------------------------------------------------
		|debugtalk.py 放置在项目根目录下（借鉴了pytest的conftest文件的设计）
		|.env 放置在项目根目录下，可以用于存放一些环境变量
		|reports 文件夹：存储 HTML 测试报告
		|testcases 用于存放测试用例
		|har 可以存放录制导出的.har文件
		|configpackage 可以存放第三方脚架
		|log 脚本输出日志
		|OUTPUTS 存放测试报告	
		|testsuite 存放测试用例集




使用方法：
1.安装Python3环境（未在Python2上运行后，不知道有没有问题）
2.下载代码到本地并解压
3.cmd到根目录下安装相关依赖包
 pip install -r requirements.txt
4.具体testcase和testsuite之间的调用可以写也可以不写单独运行
5.main函数直接运行会生产测试报告，单独跑case只会有log
6.主运行函数需要已test_*或*_test命名，参见pytest规则
		