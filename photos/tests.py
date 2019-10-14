from django.test import TestCase
from .models import Image,Location,Category
# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
        self.new_category = Category(category_name='shoes female')
        self.new_category.save_category()
        self.new_location = Location(location_name = 'france')
        self.new_location.save_location()
    
    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))
        self.assertTrue(isinstance(self.new_category,Category))
        self.assertTrue(isinstance(self.new_location,Location))
    
    def test_save_method(self):
        self.new_image.save_image()
        all_objects = Image.objects.all()
        self.assertTrue(len(all_objects)>0)

    def test_delete(self):
        self.new_image.save_image()
        filtered_object = Image.objects.filter(imageName='media')
        Image.delete_image(filtered_object)
        all_objects = Image.objects.all()
        self.assertTrue(len(all_objects) == 0)
        
    def test_display_all_objects_method(self):
        self.new_image.save_image()
        all_objects = Image.retrieve_all()
        self.assertEqual(all_objects.get(id=1).imageName,'media')

