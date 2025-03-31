# 개발 환경 설정
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView

urlpatterns = [
    path('api/schema/', include('drf_spectacular.urls')),  # OpenAPI 3.0 문서화
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),  # Swagger UI
    path('admin/', include('django.contrib.admin.urls')),  # 관리 페이지
    path('api/', include('yourapp.urls')),  # 앱의 URL들
]