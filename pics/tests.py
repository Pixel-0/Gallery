from django.test import TestCase
from .models import Image,Category,Location

# Create your tests here.

class ImageTestClass(TestCase):
    def setUp(self):
        self.james= Image(name = 'James', 
                        description ='Potrait of a Kenyan man in serious thought', 
                        image ='images/james.jpg',
                        upload_date ='2019-05-10 17:30:36.627472+03')

    def test_instance(self):
        self.assertTrue(isinstance(self.james,Image))

    def test_save_method(self):
        self.james.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_method(self):
        self.james.save_image()
        self.james.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

class CategoryTestClass(TestCase):
    def setUp(self):
        self.james= Image(name = 'James', 
                        description ='Potrait of a Kenyan man in serious thought', 
                        image ='images/james.jpg',
                        upload_date ='2019-05-10 17:30:36.627472+03',
                        category = 'Potraits')

        def test_instance(self):
        self.assertTrue(isinstance(self.james.category,Category))