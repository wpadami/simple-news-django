from django.urls import path

from . import views

app_name = "news"
urlpatterns = [
    path('', views.BlogIndexView.as_view(), name='newsindex'),
    path('<slug:cat_slug>/<slug:slug>/', views.DetailedView.as_view(), name='newsdetail'),
    path('<slug:cat_slug>/', views.CategoryListView.as_view(), name='catindex'),
]