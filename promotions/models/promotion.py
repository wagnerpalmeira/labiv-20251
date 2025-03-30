from django.db import models
from .category import Category
from .tag import Tag

class Promotion(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    url = models.URLField()
    image_cover = models.ImageField(upload_to='promotions', null=True, blank=True)

    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.name} - {self.price} R$'

    class Meta:
        verbose_name = 'Promoção'
        verbose_name_plural = 'Promoções'