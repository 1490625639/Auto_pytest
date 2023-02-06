import logging
import time

# 输出到控制台
# 1. 设置logger名称
logger=logging.getLogger("log_file_demo")
# 2. 设置log级别
logger.setLevel(logging.INFO)
# 3. 创建hander
fh_stream=logging.StreamHandler()
# 写入文件
data_time=time.strftime('%Y-%m-%d-%H-%M-%S')
print(data_time)
fh_file=logging.FileHandler("./"+data_time+".log")
# 4. 设置日志级别
fh_stream.setLevel(logging.INFO)
fh_file.setLevel(logging.INFO)
# 5. 定义输出级别
formatter=logging.Formatter("%(asctime)s %(levelno)s  %(levelname)s %(message)s")
fh_stream.setFormatter(formatter)
# 6. 添加hander
logger.addHandler(fh_stream)
logger.addHandler(fh_file)
# 7. 运行输出
logger.info("this is a info")
logger.debug("this is a debug")
logger.warning("this is a warning")