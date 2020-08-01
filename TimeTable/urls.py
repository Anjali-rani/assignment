from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from.import views

urlpatterns =[

path('admin/', admin.site.urls),
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^test/$', views.TestPage.as_view(), name='test'),
    url(r'^thanks/$', views.ThanksPage.as_view(), name='thanks'),
    url(r'^TT/', include('TT.urls', namespace='TT')),


]