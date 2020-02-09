import email.mime.text
import email.utils


import smtplib
from email.mime.text import MIMEText


self_user = '1617491825@qq.com'
def mail(self_user):
    ret = True
    try:

        sender = '13020207396@163.com'  # 发件人邮箱(最好写全, 不然会失败)
        receivers = ['1617491825@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

        msg = MIMEText('邮件内容', 'plain', 'utf-8')
        msg['From'] = "{}".format(sender)
        msg['To'] = ",".join(receivers)
        msg['Subject'] = '主题'

        # server = smtplib.SMTP_SSL('applesmtp.163.com', 465)
        # server.connect('applesmtp.163.com', 25)
        # server.login('qp10161118@163.com', 'Qzxcvb50')
        # server.sendmail(msg['From'],msg['To'] ,  msg.as_string())

        server = smtplib.SMTP_SSL('applesmtp.163.com', 465)  # 启用SSL发信, 端口一般是465
        server.login('qp10161118@163.com', 'Qzxcvb50')  # 登录验证
        server.sendmail('13020207396@163.com', [self_user], msg.as_string())  # 发送

        server.quit()
    except Exception:
        ret = False
    return ret


if __name__ == '__main__':
    print(mail('1617491825@qq.com'))
