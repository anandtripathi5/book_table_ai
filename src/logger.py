import logging
import sys
from functools import wraps


def set_logger():
    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        fmt='%(process)d - %(asctime)s - %(filename)s - %(module)s - '
            '%(funcName)s - %(lineno)d - [%(levelname)s] - %(message)s')
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    log.addHandler(handler)
    return log


log = set_logger()


def function_logger(logger):
    def wrap(func):
        @wraps(func)
        def function_log(*args,     **kwargs):
            logger.debug(
                "Inside Function {} with parameters: {},{}".format(
                    func.__name__,
                    args,
                    kwargs
                )
            )
            return_param = func(*args, **kwargs)
            logger.debug(
                "Function: {} returns {}".format(
                    func.__name__,
                    return_param
                )
            )
            return return_param
        return function_log
    return wrap
