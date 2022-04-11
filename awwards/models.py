import profile
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
import datetime as dt


# Create your models here.

#  Individual project view

class Project(models.Model):
    ''' 
    a model for project posts 
    '''
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True)
    live_link = models.URLField()
    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True)

    
    def save_project(self):
        ''' 
        method saves posted project instance 
        '''
        self.save()

    def delete_project(self):
        '''
        method deletes posted project instance 
        '''
        self.delete()

    @classmethod
    def search_project(cls, search_term):
        ''' 
        searches posted projects by title 
        '''
        return cls.objects.filter(title__icontains=search_term).all()


    @classmethod
    def projects_of_day(cls):
        date = dt.date.today()
        projects_of_day = cls.objects.filter(posted_on = date)
        return projects_of_day


    def test_get_projects_by_date(self):
        test_date = '2022-04-10'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        projects_by_date = Project.days_projects(date)
        self.assertTrue(len(projects_by_date) == 0)


    @classmethod
    def days_projects(cls,date):
        projects = cls.objects.filter(posted_on = date)
        return projects


# Profile view

class UserProfile(models.Model):
    ''' 
    extends the user model 
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    photo = models.ImageField(default='default.jpg', upload_to='avatars/')
    bio = models.TextField(max_length=500, blank=True, default=f'Hi, thanks for checking out my profile')

    def __str__(self):
        return f'{self.user.username}'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



# Rating View

class UserRating(models.Model):
    ''' 
    model allows users to rate posted projects based on the design, userbility and content
    '''
    
    Rating_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10')
    )

    interface = models.PositiveIntegerField(choices=Rating_CHOICES, default=1)
    experience = models.PositiveIntegerField(choices=Rating_CHOICES, default=1)
    content = models.PositiveIntegerField(choices=Rating_CHOICES, default=1)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.post}'s rating"

    def save_user_rating(self):
        ''' 
        method saves a user's project rating 
        '''
        self.save()

    def delete_rating(self):
        ''' 
        method deletes a user's project rating 
        '''
        self.delete()


