import yagmail

class SendEmail():

  def send_email(self):
    yagmail.SMTP(
            host='smtphz.qiye.163.com', user='zhuhongcheng04417@hellobike.com',
            password='G6HghRf3Qm9Tkhyp', smtp_ssl=True
          ).send('zhuhongcheng04417@hellobike.com', '信用卡分销测试报告', 'report/report.html')
