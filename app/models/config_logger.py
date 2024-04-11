logger_output = {
    'version': 1,
    'formatters': {
        'console_out': {
            'format': '{asctime} {filename}: {lineno} {levelname} | {process_time} | {method} | {url} | {status_code} |',
            'style': '{'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'console_out'
        }
    },
    'loggers': {
        'output': {
            'level': 'INFO',
            'handlers': ['console']
        }
    }
}