from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=30)

    def save_loc(self):
        self.save()

    def delete_loc(self):
        self.delete()


class Category(models.Model):
    name = models.CharField(max_length=30)

class Picture(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='uploads/', default='default.jpg')
    description = models.TextField()
    location = models.ForeignKey(Location , on_delete=models.CASCADE)
    category = models.ForeignKey(Category ,on_delete=models.CASCADE)

    def save_pic(self):
        self.save()

    def delete_pic(self):
        self.delete()

    @classmethod
    def search_by_category(cls,category):
        pic = cls.objects.filter(category__name__icontains = category)
        return pic

    @classmethod
    def filter_by_location(cls, location):
        pic = cls.objects.filter(location__name__icontains=location)
        return pic

    def get_image_by_id(id):
        pic = Picture.objects.get(id)
        return pic
