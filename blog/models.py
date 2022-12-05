from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #one to many relation, an author can have many posts
#But a post has one author

class Post(models.Model):
    title = models.CharField(max_length=100) #Char type input
    content = models.TextField() #Unrestricted text
    date_posted = models.DateTimeField(default = timezone.now) #Django utility to get current time
    author = models.ForeignKey(User, on_delete=models.CASCADE) #On delete makes the post dissapear if the user is deleted

    def __str__(self):
        return self.title