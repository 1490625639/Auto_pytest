import logging
# 1. 导包

# 2.设置对应的配置信息
logging.basicConfig(level=logging.INFO,format='%(name)s %(levelno)s  %(levelname)s %(asctime)s')
# 3.定义日志名称getlogger

logger=logging.getLogger("log_demo")
# 4.info debug
logger.info("info")
# logger.warning("警告")
# logger.error("错误")
#logger.debug("debug")
