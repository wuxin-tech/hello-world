#-*- coding:utf-8 -*-#
#-------------------------------------------------------------------------
#ProjectName:       xianxingWeb
#FileName:          Run_All.py
#Author:            wuxin
#Date:              2020/12/28 11:25
#Description:
#--------------------------------------------------------------------------
import unittest
from web_object.test_case_object.Test_E_Login_shujufenli import Login_Test
from web_object.test_case_object import Test_E_Login_shujufenli
from web_object.test_case_object import Test_Login
from types import ModuleType
from web_object.lib_object import HTMLTestReportCN
from web_object.lib_object.Send_Mail import SendMail
from web_object.common_object import constant

class RunAll():
    def test_all(self):
        #获取测试套件对象
        #suite=unittest.TestSuite()
        #suite.addTest(Login_Test('test_login_success'))  #
        #suite.addTest(Login_Test('test_switch_language_to_English'))
        #get_suite=unittest.TestLoader().loadTestsFromTestCase()    #该方法无法解决参数化的测试用例。
        #get_suite=unittest.TestLoader().loadTestsFromModule(ModuleType("Test_Login_shujufenli"))
        #print(get_suite)
        #print(type(get_suite))
        # get_suite1=unittest.TestLoader().loadTestsFromModule(Test_Login_shujufenli)
        # #print(get_suite1)
        # #print(type(get_suite1))
        # get_suite2=unittest.TestLoader().loadTestsFromModule(Test_Login)
        # # print(get_suite2)
        # # print(type(get_suite2))
        # suite.addTest(get_suite1)
        # suite.addTest(get_suite2)  #用于添加测试
        discover=unittest.defaultTestLoader.discover('../xianxingweb',pattern="Test_*.py")
        #suite.addTest(get_default)
        #创建对象，调用run方法即可开始跑
        # runner=unittest.TextTestRunner()
        # runner.run(suite)
        with open("report.html",mode="w",encoding='utf-8') as fp:
            runner=HTMLTestReportCN.HTMLTestRunner(fp,description="以下为用例具体情况",tester="武鑫")
            runner.run(discover)


        list_to_addr = ["1034587024@qq.com","374521734@qq.com"]#发给谁
        send = SendMail("smtp.qq.com", "1034587024@qq.com", "czpaysvozbwqbbcb", "1034587024@qq.com", list_to_addr)
        send.send_mail("自动化测试报告", "此次自动化测试的结果是：", filepath=constant.report_dir,
                       reportname='Web testing report.html',filepath2=constant.pic_dir)




if __name__ == '__main__':
    run=RunAll()
    run.test_all()


























