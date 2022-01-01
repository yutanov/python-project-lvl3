logger_config = {
    'version': 1,  # обязательный ключ и значение
    'disable_existing_loggers': False,
    # Если указано значение False, логгеры, существующие при выполнении
    # этого вызова, остаются включенными. По умолчанию — True

    # форматеры:
    'formatters': {
        'std_format': {
            'format':
                '{asctime} - {levelname}'
                ' - {module}: {funcName}: {lineno} - {message}',
                'style': '{'
            # {module}:{funcName}:{lineno} ->
            # <имя модуля>:<имя функции>:<номер строки>
            # 'style': '{' ->
            # указывается из-за отличия стиля
            # форматирования от дефолтного
        },
        'console_format': {
            'format':
                '{message}',
                'style': '{'
        }
    },
    # обработчики:
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            # путь до конкретного класса в модуле logging
            'level': 'DEBUG',
            'formatter': 'console_format'
        },
        'to_file': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'std_format',
            'filename': 'myapp1.log',
            'mode': 'w'
        }
    },
    # логгеры:
    'loggers': {
        'app_logger': {
            'level': 'DEBUG',
            'handlers': ['to_file']
            # 'propagate': False по умолчанию True
        },
        # 'logger_for_console': {
        #     'level': 'DEBUG',
        #     'handlers': ['console']
        # }
    },

    # 'filters': {},
    # 'root': {}  # '': {} пустая строка в виде ключа означает корневой логгер
    # 'incremental': True
}
# ! создал словарь logger_config
# ! в своих модулях импортирую logging.config
# ! загружаю словарь logger_config в модуль logging:
# logging.config.dictConfig(logger_config)
# ! у logging.config есть метод dictConfig, которому передается
# ! созданный словарь logger_config
