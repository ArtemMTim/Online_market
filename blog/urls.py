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
    path("blogs/create/", PostCreateView.as_view(), name="post_create"),
    path("blogs/<slug>/", PostDetailView.as_view(), name="post_detail"),
    path("blogs/<slug>/update/", PostUpdateView.as_view(), name="post_update"),
    path("blogs/<slug>/delete/", PostDeleteView.as_view(), name="post_delete"),
]
