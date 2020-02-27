from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.home),
    url(r'users/',views.user.as_view()),
    url(r'user/(?P<pk>[0-9])', views.user_detail_view.as_view())

]