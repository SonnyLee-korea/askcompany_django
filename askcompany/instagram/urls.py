from . import views
from django.urls import path,re_path,register_converter
from django.views.generic import ListView
from .models import Post
from .converters import YearConverter,MonthConverter,DayConverter

class ItemListView(ListView):
    model = Post
    
item_list = ItemListView.as_view()



register_converter(YearConverter,'year')
register_converter(MonthConverter,'month')
register_converter(DayConverter,'day')

app_name = 'instagram' # URL Reverse 에서 namespace역할을 하게 된다.


urlpatterns=[
    path('new/',views.post_new,name='post_new'),
    path('',views.post_list,name='post_list'),
    path('<int:pk>/',views.post_detail,name='post_detail'),
    path('items/',item_list,name='item_list'),

    # path('archives/<int:year>/',views.archives_year),
    # re_path(r'archives/(?P<year>20\d{2})/',views.archives_year),
    path('archive/',views.post_archive,name='post_archive'),
    path('archive/<year:year>/',views.post_archive_year,name='post_archive_year'),
    # path('archive/<year:year>/<month:month>/',views.post_archive_month,name='post_archive_month'),
    # path('archive/<year:year>/<month:month>/<day:day>/',views.post_archive_day,name='post_archive_day'),

]