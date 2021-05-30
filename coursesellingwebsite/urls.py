from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('course.urls')),
    path('user/', include('user.urls')),
    path('payment/', include('payment.urls')),
    path('cart/', include('cart.urls')),
    path('instructor/', include('instructor.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)