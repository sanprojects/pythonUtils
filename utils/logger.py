import logging, logging.config, warnings, time, sys, traceback


class MultilineFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord):
        save_msg = record.msg
        output = ""
        for line in save_msg.splitlines():
            record.msg = line
            output += super().format(record) + "\n"
        record.msg = save_msg
        record.message = output
        return output


# formatter = MultilineFormatter(
#     fmt='%(asctime)s.%(msecs)03dZ\t%(levelname)-8s\t%(name)-8s\t%(filename)s:%(lineno)d\t%(message)s',
#     datefmt='%Y-%m-%dT%H:%M:%S',
# )

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        # 'standard': formatter,
        'standard': {
            'format': '%(asctime)s.%(msecs)03dZ\t%(levelname)-8s\t%(name)-8s\t%(filename)s:%(lineno)d\t%(message)s',
            'datefmt': '%Y-%m-%dT%H:%M:%S',
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stderr',  # Default is stderr
        },
    },
    'loggers': {
        '': {  # root logger
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}

logging.config.dictConfig(LOGGING)
logging.Formatter.converter = time.gmtime


def getStack():
    return traceback.format_stack()[-3].replace('\n', ' ')

def customWarning(*args, **kwargs):
    logging.warning(f'{args} {kwargs} {getStack()}')


warnings.warn = customWarning


# log unhandled exceptions
def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    logging.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))


sys.excepthook = handle_exception