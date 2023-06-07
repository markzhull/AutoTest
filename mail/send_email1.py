import smtplib
from mail.mime.text import MIMEText
from mail.mime.multipart import MIMEMultipart
from mail.mime.application import MIMEApplication


class SendEmail():
  def send_email(self, email_to, file_path):
    # 邮件头
    msg = MIMEMultipart()
    msg['Subject'] = '信用卡分销平台测试报告'
    msg['From'] = 'zhuhongcheng04417@hellobike.com'
    msg['To'] = email_to

    # 邮件正文
    msg_1 = MIMEText('信用卡分销平台测试报告')
    msg.attach(msg_1)

    # 添加附件
    msg_2 = MIMEApplication(open(file_path, 'rb').read())
    msg_2.add_header('Content-disposition', 'attachment', filename=file_path)
    msg.attach(msg_2)

    # 登录邮件服务器
    s = smtplib.SMTP_SSL('smtphz.qiye.163.com')
    s.login('zhuhongcheng04417@hellobike.com', 'G6HghRf3Qm9Tkhyp')  # xxx是授权码，不是邮箱的登录密码
    s.sendmail('zhuhongcheng04417@hellobike.com', email_to, msg.as_string())
    s.close()


if __name__ == '__main__':
  SendEmail().send_email('zhuhongcheng04417@hellobike.com', '../report/report.html')
