from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class ProductQuerySet(models.QuerySet):
    def filterByParams(self, search=None, category=None, tag=None):
        queryset = self

        if search:
            queryset = queryset.filter(
                models.Q(name__icontains = search) | models.Q(description__icontains = search)
            )
        if category:
            queryset = queryset.filter(category = category)
        if tag:
            queryset = queryset.filter(tags = tag)
        
        # using distinct because tag are many to many and can produce duplicate products
        return queryset.distinct()
    
class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, db_index=True)
    tags = models.ManyToManyField(Tag, blank = True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    objects = ProductQuerySet.as_manager()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

