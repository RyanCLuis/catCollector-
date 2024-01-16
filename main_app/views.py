from django.shortcuts import render
# importing our Class-Based-Views (CBVs)
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Cat

# Create your views here.
# this was to build our initial view
# cats = [
#     {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
#     {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
#     {'name': 'Donut', 'breed': 'siamese', 'description': 'cute but kindof scary', 'age': 0},
# ]
# define home view here - '/'
# Ger - Home
def home(request):
    # unlike with ejs, we need our html file extension
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# index view - shows all the cats at '/cats'
def cats_index(request):
    # collect our objects from the database
    # this uses the objects object on the Cat model class
    # the objects object has a method called all
    # all grabs all of the entities using the parent model(in this case, Cat)
    cats = Cat.objects.all()
    # print(cats)
    # for cat in cats:
    #     print(cat)
    # just like in ejs, we can pass some data to our views
    return render(request, 'cats/index.html', { 'cats' : cats })

# detail view - shows one cat at '/cats/:id'
def cats_detail(request, cat_id):
    # find one cat with its id
    cat = Cat.objects.get(id=cat_id)

    return render(request, 'cats/detail.html', { 'cat': cat })

# inherit from the CBV - CreateView, to make our cats create view
class CatCreate(CreateView):
    # tell the createview to use the Cat model for all its functionality
    model = Cat
    # this view creates a form, so we need to identify which fields to use
    fields = '__all__'
    # we can add other options inside this view
    # success_url = '/cats/{cat_id}'

# Update View - extends the UpdateView class
class CatUpdate(UpdateView):
    model = Cat
    # let's make it so you can't rename a cat
    # we could simply say fields = "__all__" or we can customize like this:
    fields = ['breed', 'description', 'age']

# Delete View - extends DeleteView
class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats'