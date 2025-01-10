from django.test import TestCase
from django.contrib.auth.models import User
from base.models import Product

class ProductModelTests(TestCase):

    def setUp(self):
        # Create a user to associate with the product
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.product = Product.objects.create(
            user=self.user,
            name="Test Product",
            brand="Test Brand",
            category="Test Category",
            description="A test product description.",
            rating=4.5,
            numReviews=10,
            price=100.00,
            countInStock=20
        )

    def test_product_creation(self):
        # Check that the product is created successfully
        product = Product.objects.get(name="Test Product")
        self.assertEqual(product.brand, "Test Brand")
        self.assertEqual(product.price, 100.00)

    def test_product_string_representation(self):
        # Check the string representation of the product
        expected_representation = "Test Product | Test Brand | 100.0"
        self.assertEqual(str(self.product), expected_representation)

    def test_default_values(self):
        # Check default values for a new product
        new_product = Product.objects.create(
            user=self.user,
            name="New Product"
        )
        self.assertEqual(new_product.numReviews, 0)
        self.assertEqual(new_product.countInStock, 0)
        self.assertEqual(new_product.image.name, "/images/placeholder.png")

    def test_product_update(self):
        # Update a product and verify the changes
        self.product.price = 150.00
        self.product.save()
        updated_product = Product.objects.get(name="Test Product")
        self.assertEqual(updated_product.price, 150.00)

    def test_product_deletion(self):
        # Delete a product and check if it no longer exists
        self.product.delete()
        product_exists = Product.objects.filter(name="Test Product").exists()
        self.assertFalse(product_exists)
