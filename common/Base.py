from config.Conf import ConfigYaml
from utils.MysqlUtil import Mysql

# 测试push时候是否需要进行登录
# 数据库的初始化  相当于将get_db_conf_info()中进行了封装.
# 1 定义init_db
def init_db(db_alias):
    # 2 初始化数据化信息,通过配置
    db_info = ConfigYaml().get_db_conf_info(db_alias)
    print(db_info)
    host = db_info["db_host"]
    user = db_info["db_user"]
    password = db_info["db_password"]
    db_name = db_info["db_name"]
    charset = db_info["db_charset"]
    port = int(db_info["db_port"])
# 01点10分
    # 3 初始化mysql对象
    conn = Mysql(host, user, password, db_name, charset, port)
    print(conn)
    return conn




if __name__ == '__main__':
    init_db("db_2")
