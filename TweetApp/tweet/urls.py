from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.home, name="home"),
    path("create/", view=views.create_tweet, name="create_tweet"),
    path("<int:tweet_id>/update/", view=views.update_tweet, name="update_tweet"),
    path("<int:tweet_id>/delete/", view=views.delete_tweet, name="delete_tweet"),
    path("register/", view=views.auth_register,name="register" ),
]
