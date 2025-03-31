# 배포 환경 설정
from django.urls import path, include

urlpatterns = [
    path('admin/', include('django.contrib.admin.urls')),  # 관리 페이지
    # path('api/', include('yourapp.urls')),  # 앱의 URL들
]