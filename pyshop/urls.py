from django.conf.urls import url, include
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings

from django.views.generic import TemplateView
from.import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^products/', include('products.urls')),
    url(r'^$', views.home)
    # url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
