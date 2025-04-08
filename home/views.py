from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    context = {
        'title': 'Welcome to My Portfolio',
        'heading': 'Hello, I am John Doe',
        'description': 'I am a web developer with a passion for Machine Learning and Artifical Intelligence.',
        'skills': ['HTML', 'CSS', 'JavaScript', 'Python'],
    }
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    return render(request, 'contact.html')