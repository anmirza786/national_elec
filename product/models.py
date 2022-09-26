import re
from PIL import Image
from io import BytesIO
from django.db import models
from django.core.files import File
from django.core.validators import MaxValueValidator, MinValueValidator

# from vendor.models import Vendor


class Category(models.Model):
    title = models.CharField(
        max_length=255, verbose_name='Sub Category', unique=True)
    parent = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.CASCADE, verbose_name='Parent Category', default=None)
    slug = models.SlugField(max_length=255, blank=True)
    catlevel = models.PositiveIntegerField(
        default=1, verbose_name='Category Level', validators=[MaxValueValidator(2), MinValueValidator(1)])

    def __str__(self):
        return self.title

    def save(self):
        slug = self.title
        slug = slug.lower()
        slug = slug.replace(" ", "_")
        slug = re.sub("[^A-Za-z0-9]", "", slug)
        self.slug = slug
        if self.parent is None:
            self.catlevel = 1
        else:
            self.catlevel = 2
        return super().save()


class ProductStatusEnum(models.IntegerChoices):
    SOON = 1, 'Comming Soon'
    AVAILABLE = 2, 'Available'
    OUTOFSTOCK = 3, 'Out of Stock'


# def make_thumbnail(image, size=(300, 200)):
#     img = Image.open(image)
#     img.convert('RGB')
#     img.thumbnail(size)

#     thumb_io = BytesIO()
#     img.save(thumb_io, 'PNG', quality=85)

#     thumbnail = File(thumb_io, name=image.name)

#     return thumbnail


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE)
    # vendor = models.ForeignKey(
    #     Vendor, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    available_quantity = models.IntegerField(
        blank=False, null=False, verbose_name='Quantity Available', help_text='Enter the Available Quantity Greater than 0', default=0)
    product_status = models.SmallIntegerField(
        choices=ProductStatusEnum.choices, default=ProductStatusEnum.AVAILABLE)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    main_varient = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', blank=False, null=False)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x180.jpg'

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'PNG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

    def save(self):
        slug = self.title
        slug = slug.lower()
        slug = slug.replace(" ", "_")
        slug = re.sub("[^A-Za-z0-9]", "", slug)
        self.slug = slug
        return super().save()


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    # thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x180.jpg'

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'PNG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

    def __str__(self):
        return f'image:({str(id)})'


class ProductVarient(models.Model):
    product = models.ForeignKey(
        Product, related_name='varients', on_delete=models.CASCADE)
    varient = models.CharField(max_length=255, blank=True, null=True)
