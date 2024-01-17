from django.db import models
from django.urls import reverse
from datetime import date

MEALS = (
    # this is a tuple with multiple tuples
    # each of these is called a 2-tuple
    ('B', "Breakfast"),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)

# the Toy Model for our M:M relationship
class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.color} {self.name}"
    
    def get_absolute_url(self):
        return reverse('toy_detail', kwargs={'pk': self.id})

# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

# cats and Toys have a M:M relationship
# Cats >--< Toys
    toys = models.ManyToManyField(Toy)

    def __str__(self):
        return self.name
    
    # this is the get_absolute_url method, it redirects to the detail page where appropriate
    def get_absolute_url(self):
        return reverse('detail', kwargs={'cat_id': self.id})
    
    # this is how we can view related data from the main parent model
    def fed_for_today(self):
        # we can use django's filter, which produces a queryset for all feedings
        # we will look at the array(QuerySet) and compare it to the length od the MEALS tuple
        # we can return a boolean, that will be useful in our detail template
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

# The model for feeding - this is a 1:M relationship with cat
# one cat caan have many feedings
class Feeding(models.Model):
    # we can add a custom label to show up on our forms
    date = models.DateField('Feeding date')
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
    
    # change the defualt sort
    class Meta:
        ordering = ['-date']