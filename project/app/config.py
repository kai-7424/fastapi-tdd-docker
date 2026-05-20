
#这些是在做项目配置管理，从环境变量读取变量，测试开发/测试/生产 环境， 给fastapi提供统一配置

from pydantic_settings import BaseSettings # BaseSetting是自动从环境变量读取配置
import logging
from functools import lru_cache

# get uvicorn log uvicorn的日志器， log.info()打印日志
log = logging.getLogger('uvicorn')

# class basesetting, basesetting会自动从env，docker和系统中读取环境变量
class Settings(BaseSettings): # BaseSetting是一个类，Settings 继承BaseSetting 面向父类编程polymorphism
    environment: str = 'dev' # export environemnt = shit then Settings().environment = shit
    testing: bool = bool(0)

# 依赖提供器，因为depends需要一个function作为input
#def get_settings() -> BaseSettings: #return type annotation 返回的是一个BaseSetting的类型
   # log.info("Loading config settings from the environment...")
   # return Settings()

@lru_cache #防止每次刷新的时候都要重新加载一次config
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()


    

    

    
    

