from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm, UserRegistrationForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.
def home(request):
    tweets = Tweet.objects.all().order_by("-created_at")
    return render(request, 'tweet/home.html', {"tweets": tweets})

def search_tweets(request):
    query = request.GET.get("query")

    if query:
        tweets = Tweet.objects.filter(text__icontains=query)
    else:
        tweets = Tweet.objects.all()
    
    context = {
        'query': query,
        'tweets': tweets
    }

    return render(request, 'tweet/search.html', {"context": context})

@login_required
def my_tweets(request):
    tweets = Tweet.objects.filter(user=request.user)

    return render(request, 'user/my_tweets.html', {"tweets": tweets})

@login_required
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

@login_required
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

@login_required
def delete_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk = tweet_id, user = request.user)
    
    if request.method == "POST":
        tweet.delete()
        return redirect("home")
    
    return render(request, 'tweet/delete.html', {"tweet": tweet})


def auth_register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {"form": form})
