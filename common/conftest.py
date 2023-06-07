import logging
import os
import pytest


@pytest.fixture(scope='session', autouse=True)
def logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # 设置日志输出到文件
    log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "log")
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    log_file = os.path.join("/Users/zhuhongcheng/PycharmProjects/MyAutoTestTool/log", "pytest.log")
    fh = logging.FileHandler("/Users/zhuhongcheng/PycharmProjects/MyAutoTestTool/log/pytest.log")
    fh.setLevel(logging.INFO)

    # 设置日志输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # 定义日志格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # 添加handler
    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger

def pytest_html_report_title(report):
  report.title = "信用卡分销平台测试报告"
