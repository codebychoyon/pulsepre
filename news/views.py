from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def category(request):
    return render(request, 'category.html')


def single_post(request):
    return render(request, 'single-post.html')


def about(request):
    return render(request, 'about-us.html')


def contact(request):
    return render(request, 'contact.html')


def disclaimer(request):
    return render(request, 'disclaimer.html')


def privacy_policy(request):
    return render(request, 'privacy.html')
