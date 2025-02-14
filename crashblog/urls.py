from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.contrib import admin
from django.urls import path, include

from .sitemaps import CategorySitemap, PostSitemap

sitemaps = {'category': CategorySitemap, 'post': PostSitemap}

urlpatterns = [
    path('sitemaps.xml', sitemap, {'sitemaps': sitemaps}),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', include('core.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)