# 환경 변수에 따라 자동 로딩

import os

env = os.getenv("DJANGO_ENV", "dev")  # 기본값: dev
if env == "prod":
    from .prod import *
else:
    from .dev import *
