# 개발 환경 설정

from .base import *

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]


INSTALLED_APPS += ["drf_spectacular", "user"]  # 개발용 Swagger 추가

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}