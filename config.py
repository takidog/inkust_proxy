import os
SUPPORT_PATH = [
    '/nkust/ag_pro/ag003.jsp',
    '/nkust/ag_pro/ag304_01.jsp',
    '/nkust/ag_pro/ag008.jsp',
    '/nkust/ag_pro/ag222.jsp',
    '/nkust/ag_pro/ag009.jsp',
    '/nkust/ak_pro/ak010.jsp',
    '/nkust/ag_pro/ag302_01.jsp',
    '/nkust/ag_pro/ag302_02.jsp',
    'nkust/perchk.jsp',
]


try:
    TARGET_HOST = os.environ['TARGET_HOST']
except KeyError:
    TARGET_HOST = '127.0.0.1'
