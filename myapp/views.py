from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "index.html")


def hero(request):
    return render(request, "components/hero.html")


def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, "services.html")


def portfolio(request):
    return render(request, "components/portfolio.html")


def team(request):
    return render(request, "components/team.html")


def blog(request):
    return render(request, "components/blog.html")


def contact(request):
    return render(request, "components/contact.html")


def blog_details(request):
    return render(request, "components/blog-details.html")


def portfolio_details(request):
    return render(request, "components/portfolio-details.html")


def service_details(request):
    return render(request, "components/service-details.html")
