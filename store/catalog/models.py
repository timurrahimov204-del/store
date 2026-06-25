
class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    slug = models.SlugField(max_length=64, unique=True, blank=True, null=True)

    class Meta:
        ordering = ['name']


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("catalog:product_list_by_category", args=[self.slug])
    
    

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=128)
    description = models.TextField()
    picture = models.ImageField(upload_to='products', blank = True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_created_at = models.DateField(auto_now_add=True)
    date_updated_at = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=128, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:product_detail', args=[self.id, self.slug])


# class Order(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
#     quantity = models.IntegerField()
#     location = models.CharField(max_length=128)
#     payment_method = models.CharField(max_length=128)
