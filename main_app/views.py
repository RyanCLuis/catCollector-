from django.shortcuts import render

# Create your views here.
cats = [
    {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
    {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
    {'name': 'Donut', 'breed': 'siamese', 'description': 'cute but kindof scary', 'age': 0},
]
# define home view here - '/'
# Ger - Home
def home(request):
    # unlike with ejs, we need our html file extension
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# index view - shows all the cats at '/cats'
def cats_index(request):
    # just like in ejs, we can pass some data to our views
    return render(request, 'cats/index.html', { 'cats' : cats })