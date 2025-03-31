# 개발 환경 설정
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView,SpectacularRedocView,SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),  # 관리자페이지
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"
    ),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]
