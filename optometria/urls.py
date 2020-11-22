from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from main import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('usuarios/', include('usuario.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)