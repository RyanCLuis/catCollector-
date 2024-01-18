from django.contrib import admin
# import our cat model
# add Feeding to the import
from .models import Cat, Feeding, Toy, Photo
# Register your models here.
admin.site.register(Cat)
# register the new Feeding Model 
admin.site.register(Feeding)
# register the new Toy Model 
admin.site.register(Toy)
admin.site.register(Photo)