from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ("Electronics", "Electronics"),
        ("Clothing", "Clothing"),
        ("Footwear", "Footwear"),
        ("Books", "Books"),
        ("Home", "Home"),
        ("Beauty", "Beauty"),
        ("Grocery", "Grocery"),
        ("Sports", "Sports"),
        ("Toys", "Toys"),
        ("Furniture", "Furniture"),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()

    category = models.CharField(
    max_length=100,
    choices=CATEGORY_CHOICES
)

    brand = models.CharField(max_length=100)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    discount = models.PositiveIntegerField(default=0)

    stock = models.PositiveIntegerField(default=0)

    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        default=4.0
    )

    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True
    )

    is_featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name