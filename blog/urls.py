from django.urls import include,path,re_path
from . import views

app_name = "blog"

urlpatterns = [
    path("create/", views.BlogCreateView.as_view(),name="create_view"),
    re_path(r'^(?P<pk>\d+)/(?P<title>[\w\s:-]+)$', views.BlogDetailView.as_view(), name = "detail_view"),
    path("",views.BlogListView.as_view(), name = "default_list"),
    re_path(r'^(?P<pk>\d+)/(?P<title>[\w\s:-]+)/update/', views.BlogUpdateView.as_view(), name = "update_view"),
    re_path(r'^(?P<pk>\d+)/(?P<title>[\w\s:-]+)/delete/', views.BlogDeleteView.as_view(), name = "delete_view")
]