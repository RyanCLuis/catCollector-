from django.db import models
from django.urls import reverse

# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
    # this is the get_absolute_url method, it redirects to the detail page where appropriate
    def get_absolute_url(self):
        return reverse('detail', kwargs={'cat_id': self.id})
    
MEALS = (
    # this is a tuple with multiple tuples
    # each of these is called a 2-tuple
    ('B', "Breakfast"),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)

# The model for feeding - this is a 1:M relationship with cat
# one cat caan have many feedings
class Feeding(models.Model):
    date = models.DateField()
    # meals are a charfield with maaax_length of one, because we're only going to save the first initial of each meal
    # this will help generate a dropdown in the automagically created modelform
    # B-reakfat
    # L-unch
    # D-inner
    meal = models.CharField(
        max_length=1,
        # add the custom 'choices' field options
        # this is what will create our dropdown menu
        choices=MEALS,
        # set the default choice, to a 'B'
        default=MEALS[0][0]
    )
    # creates the one to many relationships - Cat-< Feedings
    # models.ForeignKey needs two args, the model, and what to do if the parents model is deleted.
    # in the db, the column in the feeding table for the FK will be called cat_id, because django, by default, appends _id to the name of the model
    # DO NOT CONFUSE THIS WITH MONGODB AND THIER `._id` NOT THE SAME
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date} for {self.cat}"