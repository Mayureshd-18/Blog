from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
from django.urls import path

# It is called in the urls.py of the project. The returned result is matched in the paths of the url patterns.
# So if about/ was returned from the project urls.py then after matching in path it performs the necc action .
# That is here it goes to views.about which is just a HTTP response.

#blog ->templates->blog->template.html
urlpatterns = [
    path("", PostListView.as_view(),name='blog-home'),
    path("user/<str:username>", UserPostListView.as_view(),name='user-posts'),
    path("post/<int:pk>", PostDetailView.as_view(),name='post-detail'),
    path("post/<int:pk>/update/", PostUpdateView.as_view(),name='post-update'),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(),name='post-delete'),
    path("post/new/", PostCreateView.as_view(),name='post-create'),#pk is expected
    path("about/",views.about,name='blog-about'),
    #We can actually add names of variables inside the route

]
