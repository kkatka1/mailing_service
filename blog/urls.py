from django.urls import path

from blog.apps import BlogConfig
from blog.views import (
    toggle_activity,
    PostCreateView,
    PostListView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
)

app_name = BlogConfig.name

urlpatterns = [
    path("create/", PostCreateView.as_view(), name="create"),
    path("post_list/", PostListView.as_view(), name="list"),
    path("view/<int:pk>/", PostDetailView.as_view(), name="view"),
    path("update/<int:pk>/", PostUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", PostDeleteView.as_view(), name="delete"),
]
