from django.db import models


# Create your models here.


class Location(models.Model):
    location_name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()
        

    class Meta:
        ordering = ['location_name']

        
    def delete_location(self):
        self.delete()
    
    def update_location(self, update):
        self.location_name = update
        self.save()
  
    @classmethod
    def tag_articles(cls):
        tags = cls.objects.all()
        return tags
 
    @classmethod
    def get_location_id(cls, id):
        locate = Location.objects.get(pk = id)
        return locate
        
class Category(models.Model):
    categoryName = models.CharField(max_length=40, unique=True)
    def __str__(self):
        return self.categoryName
    
    
    def save_category(self):
        self.save()

    def delete_catgory(self):
        self.delete()
   
    def update_category(self, update):
        self.categoryName = update
        self.save()
    
    
    @classmethod
    def get_category_id(cls, id):
        category = Category.objects.get(pk = id)
        return category

    def __str__(self):
        return self.name

    

class Image(models.Model):
    imageName = models.CharField(max_length =30)
    imageDescription = models.TextField()
    imagePath = models.ImageField(upload_to = 'pictures/')
    image_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    image_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add = True,)
    
    def __str__(self):
        return self.imageName

    def save_image(self):
        self.save()
    def delete_image(self):
        self.delete()
        
    @classmethod
    def update_image(cls, id ,imageName, imageDescription , image_location, image_category):
        update = cls.objects.filter(id = id).update(imageName = imageName, imageDescription = imageDescription ,image_location = image_location,image_category = image_category)

    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.filter(id= id).all()
        return image
    
    
    @classmethod
    def search_by_category(cls,image_category):
        images = Image.objects.filter(image_category__name__icontains=image_category)
        return images
    
    @classmethod
    def filter_by_location(cls, image_location):
        images_location = cls.objects.filter(image_location__id=image_location)
        return images_location
    
    class Meta:
        ordering = ['imageName']
        
    
