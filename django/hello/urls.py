from django.conf.urls import url

from hello.views import HelloView

urlpatterns = [
    url(r'^hello$', HelloView.as_view(), name='home'),
]
