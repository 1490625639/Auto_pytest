
# 封装一个log工具类
import logging
import time
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
        self.log_file = log_file
        self.log_name = log_name
        self.log_level = log_level

        # 输出到控制台
        # 1. 设置logger名称
        self.logger = logging.getLogger(self.log_name)
        # 2. 设置log级别
        self.logger.setLevel(log_l[self.log_level])
        # 3. 输出控制台
        # 判断是否存在handr
        if not self.logger.handlers:

            fh_stream = logging.StreamHandler()
            formatter = logging.Formatter("%(asctime)s %(levelno)s  %(levelname)s %(message)s")
            fh_stream.setFormatter(formatter)
            # 写入文件
            data_time = time.strftime('%Y-%m-%d-%H-%M-%S')
            fh_file = logging.FileHandler(self.log_file + data_time + ".log")
            fh_file.setLevel(log_l[self.log_level])
            fh_stream.setFormatter(formatter)


            # 6. 添加hander
            self.logger.addHandler(fh_stream)
            self.logger.addHandler(fh_file)
