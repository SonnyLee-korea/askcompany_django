from . import views
from django.urls import path

app_name = 'blog1' # URL Reverse 에서 namespace역할을 하게 된다.

urlpatterns = [
    path('',views.post_list,name='post_list'),
]