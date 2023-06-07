import pytest
import allure
import json
import os
import logging
from api.AppFinanceCreditCardService import HttpRequest
from utils.do_excel import DoExcel
from common.conftest import logger
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

@allure.feature()
class TestCase():

  def setup(self):
    print('测试开始')

  @allure.story("信用卡分销平台")
  def test_api(self):
    t1 = DoExcel('/Users/zhuhongcheng/PycharmProjects/MyAutoTestTool/data/credit_card/信用卡分销接口测试用例.xlsx', 'test_data').do_excel()
    for case in t1:
      title = case['title']
      case_id = case['case_id']
      url = case['url']
      data = case['data']
      expected = case['ExpectedResult']
      t2 = DoExcel('/Users/zhuhongcheng/PycharmProjects/MyAutoTestTool/data/credit_card/信用卡分销接口测试用例.xlsx', 'test_data')
      try:
        res = HttpRequest(url, eval(data)).http_request()
        logger.info("请求响应： %s", res)
        assert res == json.loads(expected)
        test_result = 'PASS'
      except AssertionError as e:
        print("执行用例报错啦:{0}".format(e))
        test_result = 'FAIL'
        raise e
      finally:
        t2.write_data(case_id + 1, 7, str(res))
        t2.write_data(case_id + 1, 8, str(test_result))

      print(title + '的测试结果是:', res)

  def teardown(self):
    print('测试结束')

if __name__ == '__main__':
  # -s打印结果  -v 输出更详细的信息
  # pytest.main(['--continue-on-collection-errors'])#跳过失败用例继续执行
  pytest.main(['-vs','/Users/zhuhongcheng/PycharmProjects/MyAutoTestTool/api/credit_card/test_credit_card_api.py','--alluredir','./report/xml'])
  os.system('./allure-2.13.8/bin/allure generate ./report/xml -o ./report/html --clean')

