from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.home, name="home"),
    path("search/", view=views.search_tweets, name="search_tweets"),
    path("my-tweets/", view=views.my_tweets, name="my_tweets"),
    path("create/", view=views.create_tweet, name="create_tweet"),
    path("<int:tweet_id>/update/", view=views.update_tweet, name="update_tweet"),
    path("<int:tweet_id>/delete/", view=views.delete_tweet, name="delete_tweet"),
    path("register/", view=views.auth_register,name="register" ),
]
