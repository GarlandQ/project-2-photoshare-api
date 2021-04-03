from django.urls import path
from restAPI import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("api/", views.api_root),
    path("api/profiles/", views.ProfileList.as_view(), name="profile-list"),
    path(
        "api/profiles/<int:pk>/", views.ProfileDetail.as_view(), name="profile-detail"
    ),
    path("api/posts/", views.PostList.as_view(), name="post-list"),
    path("api/posts/<int:pk>/", views.PostDetail.as_view(), name="post-detail"),
    path(
        "api/posts/<int:pk>/comments/",
        views.CommentList.as_view(),
        name="comment-list",
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)