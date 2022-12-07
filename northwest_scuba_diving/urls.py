from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    # path('courses/', include('courses.urls')),
    # path('qualified/', include('qualified.urls')),
    # path('gear/', include('gear.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
