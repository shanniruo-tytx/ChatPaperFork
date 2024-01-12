import logging
class CustomClass:
    def __init__(self):
        # 创建自己的日志记录器
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        # 创建一个处理器并设置日志文件路径
        handler = logging.FileHandler('custom_class.log')
        handler.setLevel(logging.INFO)

        # 设置日志格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        # 将处理器添加到日志记录器
        self.logger.addHandler(handler)

    def perform_action(self):
        # 在类的方法中记录日志
        self.logger.info('Performing some action.')