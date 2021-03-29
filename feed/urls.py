from django.urls import path

from feed import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('new', views.new_post, name='new_post'),
    path('<int:_id>', views.post_details, name='post_details')
]
