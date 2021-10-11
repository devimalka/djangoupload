from django.urls import path
from . import views

app_name='blogdev'

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:id>/',views.post,name='post'),
    # path('tag/<slug:tag__slug>/',views.tagged,name='tagged'),
    path('search',views.search,name='search'),
]
