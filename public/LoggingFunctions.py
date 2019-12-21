# STL Imports
import logging

log_format = (
    "[%(asctime)s] [%(filename)22s:%(lineno)-4s] [%(levelname)8s]    %(message)s"
)

log_levels = {
    "NOTSET": logging.NOTSET,
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL,
}


def init_logger(
    log_level: str = "WARNING", log_file: str = "errors.log", log_file_level: str = "ERROR"
) -> None:
    log_level = log_levels[log_level]
    log_file_level = log_levels[log_file_level]
    logging.basicConfig(level=log_level, format=log_format)
    if log_file:
        file_hander = logging.FileHandler(log_file)
        file_hander.setLevel(log_file_level)
        file_hander.setFormatter(logging.Formatter(log_format))
        logging.getLogger().addHandler(file_hander)
