SOURCE_TOKEN = 'e65NLrb2gBtXAwwFipUA6R6c'
HOST = 's1516033.eu-nbg-2.betterstackdata.com'


def get_logger():
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        'handlers': {
            'logtail': {
                'class': 'logtail.LogtailHandler',
                'source_token': '$SOURCE_TOKEN',
                'host': 'https://$INGESTING_HOST',
            },
        },
        "loggers": {
            "": {
                "handlers": [
                    "logtail",
                ],
                "level": "INFO",
            },
        },
    }
