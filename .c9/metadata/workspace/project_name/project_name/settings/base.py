{"filter":false,"title":"base.py","tooltip":"/project_name/project_name/settings/base.py","undoManager":{"mark":57,"position":57,"stack":[[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":64,"column":4},"end":{"row":64,"column":5}},"text":"#"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":84,"column":0},"end":{"row":84,"column":15}},"text":"    #'website',"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":126,"column":0},"end":{"row":126,"column":78}},"text":"########## END DATABASE CONFIGURATION ########################################"},{"action":"removeLines","range":{"start":{"row":113,"column":0},"end":{"row":126,"column":0}},"nl":"\n","lines":["########## DATABASE CONFIGURATION ###########################################","# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases","DATABASES = {","    'default': {","        'ENGINE': 'django.db.backends.postgresql_psycopg2',","        'CONN_MAX_AGE': 60,","        'NAME': '',","        'HOST': '',","        'USER': '',","        'PASSWORD': '',","        'TIME_ZONE': 'UTC'","    }","}"]},{"action":"insertText","range":{"start":{"row":113,"column":0},"end":{"row":113,"column":78}},"text":"# ######### DATABASE CONFIGURATION ###########################################"},{"action":"insertText","range":{"start":{"row":113,"column":78},"end":{"row":114,"column":0}},"text":"\n"},{"action":"insertLines","range":{"start":{"row":114,"column":0},"end":{"row":119,"column":0}},"lines":["#","# DATABASE CONFIGURATION in:","# dev = dev.py >> using sqlite3","# pro = pro.py >> using postgresql+psycopg2","#"]},{"action":"insertText","range":{"start":{"row":119,"column":0},"end":{"row":119,"column":78}},"text":"########## GENERAL CONFIGURATION #############################################"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":119,"column":11},"end":{"row":119,"column":31}},"text":"GENERAL CONFIGURATIO"},{"action":"insertText","range":{"start":{"row":119,"column":11},"end":{"row":119,"column":34}},"text":" DATABASE CONFIGURATION"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":119,"column":11},"end":{"row":119,"column":12}},"text":"E"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":119,"column":12},"end":{"row":119,"column":13}},"text":"N"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":119,"column":13},"end":{"row":119,"column":14}},"text":"D"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":119,"column":83},"end":{"row":119,"column":84}},"text":"#"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":119,"column":82},"end":{"row":119,"column":83}},"text":"#"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":119,"column":81},"end":{"row":119,"column":82}},"text":"#"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":119,"column":80},"end":{"row":119,"column":81}},"text":"#"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":119,"column":79},"end":{"row":119,"column":80}},"text":"#"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":119,"column":78},"end":{"row":119,"column":79}},"text":"#"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":250,"column":0},"end":{"row":250,"column":1}},"text":"}"},{"action":"removeLines","range":{"start":{"row":228,"column":0},"end":{"row":250,"column":0}},"nl":"\n","lines":["LOGGING = {","    'version': 1,","    'disable_existing_loggers': False,","    'filters': {","        'require_debug_false': {","            '()': 'django.utils.log.RequireDebugFalse'","        }","    },","    'handlers': {","        'mail_admins': {","            'level': 'ERROR',","            'filters': ['require_debug_false'],","            'class': 'django.utils.log.AdminEmailHandler'","        }","    },","    'loggers': {","        'django.request': {","            'handlers': ['mail_admins'],","            'level': 'ERROR',","            'propagate': True,","        },","    }"]},{"action":"insertText","range":{"start":{"row":228,"column":0},"end":{"row":228,"column":11}},"text":"LOGGING = {"},{"action":"insertText","range":{"start":{"row":228,"column":11},"end":{"row":229,"column":0}},"text":"\n"},{"action":"insertLines","range":{"start":{"row":229,"column":0},"end":{"row":272,"column":0}},"lines":["    'version': 1,","    'disable_existing_loggers': False,","    'formatters': {","        'verbose': {","            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'","        },","        'simple': {","            'format': '%(levelname)s %(message)s'","        },","    },","    'filters': {","        'require_debug_false': {","            '()': 'django.utils.log.RequireDebugFalse'","        }","    },","    'handlers': {","        'mail_admins': {","            'level': 'ERROR',","            'filters': ['require_debug_false'],","            'class': 'django.utils.log.AdminEmailHandler'","        },","        'null': {","            'level': 'DEBUG',","            'class': 'logging.NullHandler',","        },","        'console': {","            'level': 'DEBUG',","            'class': 'logging.StreamHandler',","            'formatter': 'verbose'","        },","    },","    'loggers': {","        'django.request': {","            'handlers': ['mail_admins'],","            'level': 'DEBUG',","            'propagate': True,","        },","        'django_jinja': {","            'handlers': ['console', 'mail_admins'],","            'level': 'DEBUG',","            'propagate': False,","        },","    },"]},{"action":"insertText","range":{"start":{"row":272,"column":0},"end":{"row":272,"column":1}},"text":"}"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":51,"column":0},"end":{"row":51,"column":54}},"text":"#print(SITE_NAME, SITE_ROOT,  BASE_DIR, DATABASE_ROOT)"}]}],[{"group":"doc","deltas":[{"action":"removeLines","range":{"start":{"row":50,"column":0},"end":{"row":51,"column":0}},"nl":"\n","lines":[""]}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":51,"column":78},"end":{"row":52,"column":0}},"text":"\n"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":87,"column":78},"end":{"row":88,"column":0}},"text":"\n"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":99,"column":77},"end":{"row":100,"column":0}},"text":"\n"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":106,"column":77},"end":{"row":107,"column":0}},"text":"\n"}]}],[{"group":"doc","deltas":[{"action":"removeLines","range":{"start":{"row":115,"column":0},"end":{"row":116,"column":0}},"nl":"\n","lines":[""]}]}],[{"group":"doc","deltas":[{"action":"removeLines","range":{"start":{"row":136,"column":0},"end":{"row":137,"column":0}},"nl":"\n","lines":[""]}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":146,"column":78},"end":{"row":147,"column":0}},"text":"\n"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":161,"column":78},"end":{"row":162,"column":0}},"text":"\n"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":178,"column":77},"end":{"row":179,"column":0}},"text":"\n"}]}],[{"group":"doc","deltas":[{"action":"removeText","range":{"start":{"row":208,"column":76},"end":{"row":209,"column":0}},"text":"\n"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":1,"column":47},"end":{"row":2,"column":0}},"text":"\n"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":2,"column":0},"end":{"row":3,"column":0}},"text":"\n"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":3,"column":0},"end":{"row":3,"column":1}},"text":"U"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":3,"column":1},"end":{"row":3,"column":2}},"text":"s"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":3,"column":2},"end":{"row":3,"column":3}},"text":"i"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":3,"column":3},"end":{"row":3,"column":4}},"text":"n"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":3,"column":4},"end":{"row":3,"column":5}},"text":"g"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":3,"column":5},"end":{"row":3,"column":6}},"text":" "}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":3,"column":6},"end":{"row":3,"column":7}},"text":"J"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":3,"column":7},"end":{"row":3,"column":8}},"text":"i"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":3,"column":8},"end":{"row":3,"column":9}},"text":"n"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":3,"column":9},"end":{"row":3,"column":10}},"text":"j"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":3,"column":10},"end":{"row":3,"column":11}},"text":"a"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":3,"column":11},"end":{"row":3,"column":12}},"text":"2"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":3,"column":12},"end":{"row":3,"column":13}},"text":" "}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":3,"column":13},"end":{"row":3,"column":14}},"text":"t"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":3,"column":14},"end":{"row":3,"column":15}},"text":"e"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":3,"column":15},"end":{"row":3,"column":16}},"text":"m"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":3,"column":16},"end":{"row":3,"column":17}},"text":"p"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":3,"column":17},"end":{"row":3,"column":18}},"text":"l"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":3,"column":18},"end":{"row":3,"column":19}},"text":"a"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":3,"column":19},"end":{"row":3,"column":20}},"text":"t"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":3,"column":20},"end":{"row":3,"column":21}},"text":"i"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":3,"column":21},"end":{"row":3,"column":22}},"text":"n"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":3,"column":22},"end":{"row":3,"column":23}},"text":"g"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":3,"column":23},"end":{"row":3,"column":24}},"text":" "}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":3,"column":24},"end":{"row":3,"column":25}},"text":"s"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":3,"column":25},"end":{"row":3,"column":26}},"text":"y"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":3,"column":26},"end":{"row":3,"column":27}},"text":"s"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":3,"column":27},"end":{"row":3,"column":28}},"text":"t"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":3,"column":28},"end":{"row":3,"column":29}},"text":"e"}]}],[{"group":"doc","deltas":[{"action":"insertText","range":{"start":{"row":3,"column":29},"end":{"row":3,"column":30}},"text":"m"}]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":3,"column":30},"end":{"row":3,"column":30},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1414261670675,"hash":"7ed6975dff68519bddfb3a6c5bb8c098c85e6fea"}