from django.conf.urls import url
from TT import views

app_name = 'TT'

urlpatterns = [
    url(r'^$', views.CreateTimeTable.as_view(), name='create'),
    url(r'^Fill', views.FillTimeTable.as_view(), name='Fill'),
]