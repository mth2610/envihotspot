"""envihotspot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, patterns, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from home import views as home_views
from mappage import views as mappage_views
from rest_api import views as api_views
from rest_framework import routers
from account import views as account_views

router = routers.DefaultRouter()
router.register(r'hotspots', api_views.HotSpotViewSet, base_name='hotspots')

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^auth/', include('rest_framework_social_oauth2.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_views.home),
    url(r'signup/', account_views.signup),
    url(r'signup_success/', account_views.signup_success),
    url(r'^mappage/', include('mappage.urls')),
    url(r'^hotspots/', include('hotspots.urls')),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
