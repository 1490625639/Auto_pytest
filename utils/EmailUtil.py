from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


class SendEmail:

    def __init__(self, smtp_addr, username, password, recv,
                 title, content=None, file=None):
        self.smtp_addr = smtp_addr
        self.username = username
        self.password = password
        self.recv = recv
        self.title = title
        self.content = content
        self.file = file

    # 发送邮件方法
    def send_mail(self):
        # MINE
        msg = MIMEMultipart()
        # 初始化邮件信息
        msg.attach(MIMEText(self.content, _charset="utf-8"))
        msg["Subject"] = self.title
        msg["From"] = self.username
        msg["To"] = self.recv
        # 邮件附件
        if self.file:
            # MINE读取文件
            att = MIMEText(open(self.file).read())
            # 设置内容类型
            att["Content-Type"] = "application/octet-stream"
            # 设置附件头
            att["Content-Disposition"] = 'attachment;filename="%s"'
            # 将内容附件到邮件主体中
            msg.attach(att)
        # 登录邮件服务器
        self.smtp = smtplib.SMTP(self.smtp_addr, port=25)
        # self.smtp=smtplib.SMTP_SSL("smtp.qq.com", 465) #两种方式都可以发送邮件
        self.smtp.login(self.username, self.password)
        # 发送邮件
        self.smtp.sendmail(self.username, self.recv, msg.as_string())


# smtp地址,用户名,密码,标题,内容,附件
if __name__ == '__main__':
    # 初始化类
    from config.Conf import ConfigYaml

    email_info = ConfigYaml().get_email_info()
    smtp_addr = email_info["smtpserver"]
    username = email_info["username"]
    password = email_info["password"]
    recv = email_info["receiver"]
    email = SendEmail(smtp_addr, username, password, recv, "测试邮件123123")
    email.send_mail()

