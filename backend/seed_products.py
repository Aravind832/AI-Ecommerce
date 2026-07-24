import os
import random
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from products.models import Product

# Clear old data
Product.objects.all().delete()

categories = {
    "Electronics": [
        "iPhone 16 Pro", "Samsung Galaxy S25 Ultra", "OnePlus 13",
        "Google Pixel 10", "MacBook Air M4", "Dell XPS 15",
        "HP Spectre x360", "Lenovo ThinkPad X1", "Sony WH-1000XM5",
        "Apple Watch Series 10", "Samsung Smart Watch",
        "iPad Air", "Galaxy Tab S10", "Logitech MX Master 3S",
        "Mechanical Keyboard", "Gaming Mouse", "4K Monitor",
        "Bluetooth Speaker", "Wireless Earbuds", "Power Bank"
    ],

    "Clothing": [
        "Men's Cotton T-Shirt", "Women's Casual Dress", "Blue Jeans",
        "Formal Shirt", "Hoodie", "Leather Jacket",
        "Sports Jacket", "Cotton Shorts", "Women's Leggings",
        "Sweater", "Polo T-Shirt", "Cargo Pants",
        "Winter Coat", "Kurta", "Saree",
        "Blazer", "Track Pants", "Denim Jacket",
        "Skirt", "Night Suit"
    ],

    "Footwear": [
        "Nike Running Shoes", "Adidas Sneakers", "Puma Sports Shoes",
        "Woodland Boots", "Bata Formal Shoes", "Flip Flops",
        "Women's Sandals", "Kids School Shoes", "Trekking Shoes",
        "Loafers", "High Heels", "Canvas Shoes",
        "Slippers", "Football Boots", "Cricket Shoes"
    ],

    "Books": [
        "Python Programming", "Django for Beginners",
        "Clean Code", "Atomic Habits",
        "Rich Dad Poor Dad", "The Psychology of Money",
        "System Design Interview", "Data Structures & Algorithms",
        "Deep Learning", "Machine Learning Basics"
    ],

    "Home & Kitchen": [
        "Pressure Cooker", "Rice Cooker", "Air Fryer",
        "Mixer Grinder", "Electric Kettle",
        "Dinner Set", "Vacuum Cleaner",
        "Microwave Oven", "Gas Stove",
        "Water Bottle", "Coffee Maker",
        "Ceiling Fan", "Wall Clock",
        "Dining Table", "Office Chair"
    ],

    "Beauty": [
        "Face Wash", "Moisturizer", "Lip Balm",
        "Perfume", "Body Lotion", "Hair Oil",
        "Shampoo", "Conditioner",
        "Sunscreen", "Face Serum"
    ],

    "Groceries": [
        "Basmati Rice", "Wheat Flour",
        "Sugar", "Salt",
        "Sunflower Oil", "Coffee Powder",
        "Tea Powder", "Honey",
        "Peanut Butter", "Dark Chocolate"
    ],

    "Fitness": [
        "Dumbbells", "Yoga Mat",
        "Resistance Bands", "Skipping Rope",
        "Exercise Bike", "Treadmill",
        "Gym Gloves", "Protein Shaker",
        "Foam Roller", "Pull-Up Bar"
    ],

    "Toys": [
        "LEGO Blocks", "Remote Control Car",
        "Barbie Doll", "Football",
        "Basketball", "Chess Board",
        "Puzzle Game", "Toy Train",
        "Teddy Bear", "Cricket Bat"
    ],

    "Pet Supplies": [
        "Dog Food", "Cat Food",
        "Pet Shampoo", "Dog Leash",
        "Pet Bed", "Bird Cage",
        "Fish Food", "Cat Toy",
        "Dog Toy", "Pet Bowl"
    ]
}

count = 0

for category, items in categories.items():
    for item in items:
        Product.objects.create(
            name=item,
            description=f"High quality {item} from {category} category.",
            price=round(random.uniform(199, 150000), 2),
            stock=random.randint(5, 100)
        )
        count += 1

print(f"Successfully inserted {count} products!")