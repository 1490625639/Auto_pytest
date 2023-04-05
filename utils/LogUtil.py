
# 封装一个log工具类
import logging
import time
from config import Conf
import datetime
from  config.Conf import ConfigYaml
import os
#添加一个log文件的映射
log_l={
    "info":logging.INFO,
    "debug":logging.DEBUG,
    "warning":logging.WARNING,
    "error":logging.ERROR

}

"""1. 创建类
2. 定义参数
    #输出文件名称，loggername,日志级别
3. 编写输出控制台或文件"""


class Logger:
    def __init__(self, log_file, log_name, log_level):
        self.log_file = log_file  # 日志文件扩展名
        self.log_name = log_name  # 日志记录器名称
        self.log_level = log_level  # 日志级别

        # 输出到控制台
        # 1. 创建日志记录器对象
        self.logger = logging.getLogger(self.log_name)
        # 2. 设置日志级别
        self.logger.setLevel(log_l[self.log_level])
        # 3. 输出控制台
        # 判断是否存在handr
        if not self.logger.handlers:
            # 创建控制台处理器
            fh_stream = logging.StreamHandler()
            formatter = logging.Formatter("%(asctime)s %(levelno)s  %(levelname)s %(message)s")
            fh_stream.setFormatter(formatter)

            # 创建文件处理器

            data_time = time.strftime('%Y-%m-%d-%H-%M-%S')
            #fh_file = logging.FileHandler(self.log_file)
            fh_file = logging.FileHandler(self.log_file, encoding='utf-8')
            fh_file.setLevel(log_l[self.log_level])
            fh_stream.setFormatter(formatter)


            # 6.添加处理器
            self.logger.addHandler(fh_stream)
            self.logger.addHandler(fh_file)
# 1 初始化参数数据
    # 日志文件名称，日志文件级别
    # 日志文件名称=logs目录+当前时间+扩展名
log_path=Conf.get_log_path()
#当前时间
current_time=datetime.datetime.now().strftime("%Y-%m-%d")
#扩展名
log_extension=ConfigYaml().get_conf_extension()

#拼接合同
logfile=os.path.join(log_path,current_time+log_extension)
#print(logfile)

#日志文件级别
log_level=ConfigYaml().get_conf_log()
#print(log_level)


# 2 对外方法,初始log工具类,提供其他类使用
def my_log(log_name=__file__):
    return Logger(log_file=logfile,log_name=str(log_name),log_level=log_level).logger

if __name__ == '__main__':
    my_log().debug("debug测试")