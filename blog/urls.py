from django.urls import path

from blog.apps import BlogConfig
from blog.views import (
    ContactsView,
    PostCreateView,
    PostDeleteView,
    PostDetailView,
    PostListView,
    PostUpdateView,
)

app_name = BlogConfig.name


urlpatterns = [
    path("blogs/", PostListView.as_view(), name="post_list"),
    path("blogs/contacts/", ContactsView.as_view(), name="contacts"),
    path("blogs/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("blogs/create/", PostCreateView.as_view(), name="post_create"),
    path("blogs/<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),
    path("blogs/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
]
