from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import get_object_or_404,redirect

# Create your views here.
def home(request):
    tweets = Tweet.objects.all().order_by("-created_at")
    return render(request, 'tweet/home.html', {"tweets": tweets})

def create_tweet(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('home')
    else:
        form = TweetForm()

    return render(request, 'tweet/create.html', {"form": form})

def update_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk = tweet_id, user = request.user)
    
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('home')
    else:
        form = TweetForm(instance=tweet)

    return render(request, 'tweet/create.html', {"form": form})

def delete_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk = tweet_id, user = request.user)
    
    if request.method == "POST":
        tweet.delete()
        return redirect("home")
    
    return render(request, 'tweet/delete.html', {"tweet": tweet})