# from rest_framework.test import APITestCase
# from django.urls import reverse
# from rest_framework import status

# class ProductsTestCase(APITestCase):

#     def test_get_products(self):
#         response = self.client.get(reverse("products"))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)


from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from base.models import Product, User, Review

class ProductAPITests(APITestCase):
    
    def setUp(self):
        self.client = APIClient()
        
        # Create a user and admin user
        self.user = User.objects.create_user(username="testuser", password="password")
        self.admin_user = User.objects.create_superuser(username="admin", password="password")

        # Create sample products
        self.product1 = Product.objects.create(
            name="Product 1",
            price=10,
            brand="Brand 1",
            countInStock=5,
            category="Category 1",
            description="Description 1",
            rating=4.5,
        )

        self.product2 = Product.objects.create(
            name="Product 2",
            price=20,
            brand="Brand 2",
            countInStock=3,
            category="Category 2",
            description="Description 2",
            rating=3.0,
        )

    # def test_get_products(self):
    #     url = reverse('products')
    #     response = self.client.get(url)
        
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(response.data['products']), 2)
    
    # def test_get_top_products(self):
    #     url = reverse('top-products')
    #     response = self.client.get(url)
        
    #     # self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(response.data['products']), 1)
    # def test_get_single_product(self):
    #     url = reverse('product', args=[self.product1._id])
    #     response = self.client.get(url)
        
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data['name'], self.product1.name)

    # def test_create_product_as_admin(self):
    #     self.client.force_authenticate(user=self.admin_user)
    #     url = reverse('create_product')
    #     response = self.client.post(url)

    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(Product.objects.count(), 3)

    # def test_update_product(self):
    #     self.client.force_authenticate(user=self.admin_user)
    #     url = reverse('update_product', args=[self.product1._id])
    #     data = {
    #         "name": "Updated Product",
    #         "price": 30,
    #         "brand": "Updated Brand",
    #         "countInStock": 10,
    #         "category": "Updated Category",
    #         "description": "Updated Description",
    #     }
    #     response = self.client.put(url, data)

    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.product1.refresh_from_db()
    #     self.assertEqual(self.product1.name, "Updated Product")

    # def test_delete_product(self):
    #     self.client.force_authenticate(user=self.admin_user)
    #     url = reverse('delete_product', args=[self.product1._id])
    #     response = self.client.delete(url)

    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(Product.objects.count(), 1)



    # def test_create_review(self):
    #     self.client.force_authenticate(user=self.user)
    #     url = reverse('createProductReview', args=[self.product1._id])
    #     data = {
    #         "rating": 5,
    #         "comment": "Excellent product!",
    #     }
    #     response = self.client.post(url, data)

    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(self.product1.review_set.count(), 1)
    #     self.assertEqual(self.product1.review_set.first().rating, 5)

    # def test_create_duplicate_review(self):
    #     self.client.force_authenticate(user=self.user)
    #     Review.objects.create(
    #         user=self.user,
    #         product=self.product1,
    #         name=self.user.first_name,
    #         rating=5,
    #         comment="Great product!",
    #     )
    #     url = reverse('createProductReview', args=[self.product1._id])
    #     data = {
    #         "rating": 4,
    #         "comment": "Updated comment!",
    #     }
    #     response = self.client.post(url, data)

    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #     self.assertEqual(response.data['detail'], "Product already reviewed")

