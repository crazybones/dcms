from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from dcm import views

app_name = 'dcm'
urlpatterns = [
    url(r'^$', views.ContainerList.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns = format_suffix_patterns(urlpatterns)
