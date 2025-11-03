from django.shortcuts import render

def index(request):
    return render(request, "index.html", {})

def Web_view(request):
    return render(request, 'game.html',{})

def challenges_view(request):
    return render(request, 'challenges.html',{})

def resources_view(request):
    return render(request, 'resources.html',{})

def solutions_view(request):
    return render(request, 'solutions.html',{})

def takeaction_view(request):
    return render(request, 'take-action.html',{})

#css
def baseStyle_view(request):
    return render(request, 'static/styles/baseStyle.css',{})
def layoutStyle_view(request):
    return render(request, 'static/styles/layout.css',{})
def resourcesStyle_view(request):
    return render(request, 'static/styles/resources.css',{})

