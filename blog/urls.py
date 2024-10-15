from django.urls import path

from blog.apps import BlogConfig
from blog.views import PostListView, PostDetailView, PostCreateView, ContactsView, PostDeleteView, PostUpdateView

app_name = BlogConfig.name


urlpatterns = [
    path("post/", PostListView.as_view(), name="post_list"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/create/", PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),

]