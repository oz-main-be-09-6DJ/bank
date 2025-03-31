# 배포 환경 설정
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),  # 관리 페이지
    # path('api/', include('yourapp.urls')),  # 앱의 URL들
]
