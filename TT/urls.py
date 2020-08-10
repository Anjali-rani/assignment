from django.conf.urls import url
from TT import views

app_name = 'TT'

urlpatterns = [



    url(r'^$', views.Listviews.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.TTDetailView.as_view(), name='detail'),
    url(r'^create/$', views.TTCreate.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/$', views.TTUpdate.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.TTDelete.as_view(), name='delete'),
]