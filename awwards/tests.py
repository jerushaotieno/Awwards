from django.test import TestCase
from datetime import datetime
from .models import Project, UserProfile, UserRating
from django.contrib.auth.models import User

# Create your tests here.

class UserProfileTest(TestCase):
    ''' 
    test class for the UserProfile model
    '''
    
    def setUp(self):
        ''' 
        method called before running each test case
        '''
        self.user = User.objects.create_user(username='Jay')

    def tearDown(self):
        ''' 
        method clears all setup instances after running each test 
        '''
        self.user.delete()

    def test_profile_creation(self):
        ''' 
        method tests user profile instance is created once for each user 
        '''
        
        self.assertIsInstance(self.user.profile, UserProfile)
        self.user.save()
        self.assertIsInstance(self.user.profile, UserProfile)
        

class TestProject(TestCase):
    ''' 
    test class for the project image model 
    '''
    
    def setUp(self):
        ''' 
        method called before each test case
        '''
        self.test_user = User(username='Linet', password='code')
        self.test_user.save()
        self.test_profile = self.test_user.profile
        self.test_profile.save()

        self.test_post = Project(image='images/', title='sample text',description='sample description', profile=self.test_profile, live_link='https://www.google.com', posted_on=datetime.now())

    def test_instance(self):
        ''' 
        test method ensures project instance is created 
        '''
        self.assertTrue(isinstance(self.test_project, Project))

    def test_save_and_delete(self):
        ''' 
        test method that saves abd deletes project instance to the database 
        '''
        self.test_project.save_project()
        self.assertEqual(len(Project.objects.all()), 1)
        self.test_project.delete_project()
        self.assertEqual(len(Project.objects.all()), 0)

    def test_search_project(self):
        ''' 
        test method searches projects by title 
        '''
        self.test_project.save_project()
        result = Project.search_project('sample text')
        self.assertIsNotNone(result)

    def tearDown(self):
        ''' 
        method clears all setup instances after running each test 
        '''
        self.test_user.delete()
        Project.objects.all().delete()


class TestRating(TestCase):
    ''' 
    test class for UserRating model 
    '''

    def setUp(self):
        ''' 
        method that's called before all tests 
        '''
        
        self.test_user = User(username='Linet', password='code')
        self.test_user.save()
        self.test_profile = self.test_user.profile
        self.test_profile.save()
        self.test_project = Project(image='images/', title='sample text',description='some description', profile=self.test_profile, live_link='https://www.google.com', posted_on=datetime.now())
        self.test_project.save()

        self.test_rating = UserRating(interface=5, experience=6, content=5, user=self.test_profile, project=self.test_project)

    def tearDown(self):
        ''' 
        method that's called after running every test 
        '''
        
        self.test_user.delete()
        Project.objects.all().delete()
        UserRating.objects.all().delete()

    def test_instance(self):
        ''' 
        method that tests instance creation 
        '''
        
        self.assertIsInstance(self.test_rating, UserRating)

    def test_save_and_delete_rating(self):
        ''' 
        test method that saves and deletes project ratings
        '''
        
        self.test_rate.save_rating()
        self.assertEqual(len(UserRating.objects.all()), 1)
        self.test_rate.delete_rating()
        self.assertEqual(len(UserRating.objects.all()), 0)