
class Secrets:
    class Email:
        emailHost = 'smtp.qq.com'
        emailPort = 25
        emailAddr = '1484929973@qq.com'
        emailPasswd = 'prcgmccixlbojhaj'# 邮箱 SMTP 授权码，此处为虚拟，须修改

    class DataBase:
        # database information

        host = 'localhost'
        user = 'root'
        passwd = '123456'  # 修改为您本地或远程的 mysql数据库信息
        db = 'questionnaire'

    class Host:  # 修改为django允许运行的网址
        allowedHost = ['localhost', '127.0.0.1', 'xxxxx']

    class RootUrl:
        webFront = 'http://127.0.0.1:8080'

        # webBack = 'http://127.0.0.1:8000'
        webBack = 'http://127.0.0.1:8080/api/api/qs'
