import pytest
import allure
import json
from api.AppFinanceCreditCardService import HttpRequest
from utils.do_excel import DoExcel

@allure.feature()
class TestCase():
  t1 = DoExcel('/Users/zhuhongcheng/PycharmProjects/MyAutoTestTool/data/credit_card/信用卡分销接口测试用例.xlsx', 'test_data')

  def setup(self):

    print('测试开始')

  @pytest.mark.parametrize('case',t1.do_excel())
  @allure.story("信用卡分销平台")
  def test_api(self,case):
    case_id = case['case_id']
    url = case['url']
    data = case['data']
    expected = case['ExpectedResult']
    res = HttpRequest(url,eval(data)).http_request()
    self.t1.write_data(case_id+1,7,str(res))
    if res == json.loads(expected):
      test_result = 'PASS'
    else:
      test_result = 'FAIL'
    self.t1.write_data(case_id + 1, 8, str(test_result))


  def teardown(self):
    print('测试结束')

if __name__ == '__main__':
  # -s打印结果  -v 输出更详细的信息
  pytest.main(['-vs','test_http_request1.py'])
