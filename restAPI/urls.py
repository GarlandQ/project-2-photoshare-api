from django.urls import path
from restAPI import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # path("api/", views.profile_list),
    # path("api/<int:pk>/", views.profile_detail),
    path("api/profiles/", views.ProfileList.as_view()),
    path("api/profiles/<int:pk>/", views.ProfileDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)