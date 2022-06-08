import unittest

from HTMLTestRunner import HTMLTestRunner
from api.base import Base

test_report = 'test_reporter.html'

if __name__ == '__main__':
    # 进行一次登录
    base = Base()
    base.login()  # 登录放在入口脚本这里，在这里登录的时候，后面的测试用例就不需要就不需要登录了，因为这里一登录，返回的token 就会到缓存中了，后面的测试用例调用的接口都是从缓存中去拿
    # 创建一个套件
    suite = unittest.TestLoader().discover('cases', pattern='test*.py')

    with open(test_report, 'wb') as f:
        runner = HTMLTestRunner(f, title='wshop测试报告', description='简化版的测试框架')
        runner.run(suite)
