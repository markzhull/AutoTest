from mail.send_email import SendEmail
import pytest
import time
from datetime import datetime
from threading import Timer
import os

def task():
  args = ['--continue-on-collection-errors', '--html=report.html', '--self-contained-html']
  pytest.main(args)
  now = datetime.now()
  ts = now.strftime("%Y-%m-%d %H:%M:%S")
  print(ts)

def func():
  task()
  t = Timer(3600, func)
  t.start()



if __name__ == '__main__':
  func()

  # pytest.main(['--continue-on-collection-errors'])
  # pytest.main(['-vs', '/Users/zhuhongcheng/PycharmProjects/MyAutoTestTool/api/credit_card/test_credit_card_api.py', '--alluredir', './report/xml', "--self-contained-html"])
  # os.system('./allure-2.13.8/bin/allure generate ./report/xml -o ./report/html --clean')
  # SendEmail().send_email()


