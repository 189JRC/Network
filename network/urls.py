from django.urls import path

from . import views

urlpatterns = [
    # login/registration/profile edit & creation
    path("login", views.user_login, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("users/<int:id>/", views.profile_update, name="profile_update"),
    # site navigation
    path("", views.index, name="index"),
    path("following", views.following, name="following"),
    path("profile/<int:post_user_id>", views.profile_view, name="profile_view"),
    path("all_users", views.all_users, name="all_users"),
    # user actions
    path("add_post/<int:user_id>", views.add_post, name="add_post"),
    path("edit_post/<int:post_id>", views.edit_post, name="edit_post"),
    path("delete_post/<int:post_id>", views.delete_post, name="delete_post"),
    # user interactions
    path("follow", views.follow, name="follow"),
    path("unfollow", views.unfollow, name="unfollow"),
    path("like/<int:post_id>", views.like, name="like"),
    path("unlike/<int:post_id>", views.unlike, name="unlike"),
]
