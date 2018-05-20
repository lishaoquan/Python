# -*- coding: utf-8 -*-
# 普通文本邮件
import smtplib
from email.mime.text import MIMEText

msg = MIMEText("这个是普通文本邮件!","plain","utf-8")
from_addr = "123@126.com"
to_addr = "555@qq.com"
passwd = "123456"
smtp_server = "smtp.126.com"
smtp = smtplib.SMTP(smtp_server,25)
smtp.set_debuglevel(1)
smtp.login(from_addr,passwd)
smtp.sendmail(from_addr,[to_addr],msg.as_string())
smtp.quit()
