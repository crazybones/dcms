from django.conf.urls import url, include
from django.views.generic import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns

from dcm import views

app_name = 'dcm'
urlpatterns = [
    url(r'^api/list/', views.ContainerList.as_view()),
    url(r'^index/', TemplateView.as_view(template_name='index.html')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns = format_suffix_patterns(urlpatterns)
