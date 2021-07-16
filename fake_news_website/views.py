
# import SolrRepo
# from bottle import route, run, post, request, static_file
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "fake_news_website/index.html")


def about(request):
    return render(request, "fake_news_website/about.html")


def check(request):
    result = "not-fake"
    # res variable is going to
    user_input = request.POST
    print(user_input)

    # returning dummy page
    return render(request, "fake_news_website/result.html", user_input)

    # we will send the user_input dictionary to the model and it has to provide a result text(fake, not-fake, document-not-found) and matching document table(list)
    # we wull then send these results to result.html and add them to the template dynamically
