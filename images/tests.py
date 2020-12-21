from django.test import TestCase
from ..models import *
# Create your tests here.

class ImageTestCase(TestCase):

    # set up method
    def setUp(self):
        self.loc =Location(name='Kigali City')
        self.loc.save_loc()
        self.new= Picture(name='My Picture', description='Beutiful Rwanda ', category='hotels&lodge', location=self.loc,image='akagera.jpg')
        self.new.save_pic()


    def test_instance(self):
        self.assertTrue(isinstance(self.new,Picture))

    def test_save_method(self):
        self.new.save_pic()
        pics=Picture.objects.all()
        self.assertTrue(len(pics) > 0)


    def test_delete_method(self):
        self.new.delete_pic()
        pics=Picture.objects.all()
        self.assertTrue(len(pics) < 0)


class LocationTestCase(TestCase):

    # set up method
    def setUp(self):
        self.loc =Location(name='Kigali City')
        self.loc.save_loc()

    def test_instance(self):
        self.assertTrue(isinstance(self.loc,Location))

    def test_save_method(self):
        self.loc.save_loc()
        locs=Location.objects.all()
        self.assertTrue(len(locs) > 0)


    def test_delete_method(self):
        self.loc.delete_loc()
        locs=Location.objects.all()
        self.assertTrue(len(locs) < 0)