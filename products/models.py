from django.db import models
import uuid
from django.utils.text import slugify
from django.db.models.signals import pre_save
from brands.models import Brand


class Product(models.Model):

    name = models.CharField(max_length=50)
    brand = models.OneToOneField(Brand, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()
    slug = models.SlugField(null=False, unique=True, blank=False)
    image = models.ImageField(upload_to='products/', null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)

    # def save(self, *args, **kwargs):
    #    self.slug = slugify(self.name)
    #    super(Product, self).save(*args, *kwargs)

    def __str__(self):
        return self.name


def set_slug(sender, instance, *args, **kwargs):  # callback
    if instance.name and not instance.slug:
        slug = slugify(instance.name)
        while Product.objects.filter(slug=slug).exists():
            slug = slugify(
                f'{instance.name}, { str(uuid.uuid4())[:8] }'
            )
        instance.slug = slug


pre_save.connect(set_slug, sender=Product)
