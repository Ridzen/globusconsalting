from django.urls import reverse
from rest_framework.test import APITestCase

from apps.posts.models import Post


class PostsAPITestCase(APITestCase):

    def test_post_view_with_no_exists_posts(self):
        url = reverse('posts-url')  # url = "/api/v1/posts/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 0)

    def test_products_view_with_product(self):
        new_post = Post.objects.create(name='Набор на вакансию в польшу',
                                       description='Проживание и питание за счет работодателя',
                                       tag='Poland')
        url = reverse('post-url')  # url = "/api/v1/posts/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], new_post.id)
        self.assertEqual(response.data[0]['name'], new_post.name)
        self.assertEqual(response.data[0]['description'], new_post.description)
        # self.assertEqual(response.data[0]['image'], new_post.image)
        self.assertEqual(response.date[0]['tag'], new_post.tag)
