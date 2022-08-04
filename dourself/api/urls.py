from django.urls import path
from . import views


urlpatterns = [
    path('',views.post_item),
    path('get/',views.get_item),
]