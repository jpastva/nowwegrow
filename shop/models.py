''' Models for shop app, including Category, Product '''
from django.db import models
from django.urls import reverse

class Category(models.Model):
    ''' Model for product categories '''
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        ''' Return URL for product category for filtering '''
        return reverse('shop:product_list_by_category',
                       args=[self.slug])

class Product(models.Model):
    ''' Product data '''
    merchant = models.ForeignKey('register.User', limit_choices_to={'is_merchant':True}, on_delete=models.CASCADE, verbose_name='merchant', related_name='product')
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    description = models.TextField(blank=True)
    sale_unit = models.CharField(max_length=25)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        ''' Return link to individual product '''
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])
