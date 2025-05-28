from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from .models import Author, Post, Tag
from django.db.utils import IntegrityError

class TagModelTest(TestCase):

    def setUp(self):
        self.tag = Tag.objects.create(tag="django")

    def test_tag_creation(self):
        self.assertEqual(self.tag.tag, "django")

    def test_tag_str_representation(self):
        self.assertEqual(str(self.tag), "django")

    def test_tag_name_unique(self):
        with self.assertRaises(IntegrityError):
            Tag.objects.create(tag="django")  # mateix nom, ha de fallar si és unique


class AuthorModelTest(TestCase):

    def setUp(self):
        self.author = Author.objects.create(first_name="John", last_name="Doe")

    def test_author_creation(self):
        self.assertEqual(self.author.first_name, "John")
        self.assertEqual(self.author.last_name, "Doe")

    def test_author_str(self):
        self.assertEqual(str(self.author), "John Doe")


class PostModelTest(TestCase):

    def setUp(self):
        self.author = Author.objects.create(first_name="John", last_name="Doe")
        self.post = Post.objects.create(
            title="Test Post",
            slug="test-post",
            content="Contingut de prova",
            author=self.author,
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.slug, "test-post")
        self.assertEqual(self.post.author.first_name, "John")

    def test_post_str(self):
        self.assertEqual(str(self.post), "Test Post")


class URLTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.author = Author.objects.create(first_name="John", last_name="Doe")
        self.post = Post.objects.create(
            title="Test Post",
            slug="test-post",
            content="Contingut de prova",
            author=self.author,
        )
        self.tag = Tag.objects.create(tag="django")

    def test_index_url(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_url(self):
        response = self.client.get(reverse('post_detail', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)

    def test_author_detail_url(self):
        response = self.client.get(reverse('author_detail', args=[self.author.id]))
        self.assertEqual(response.status_code, 200)

    def test_tag_posts_url(self):
        response = self.client.get(reverse('tag_posts', args=[self.tag.tag]))
        self.assertEqual(response.status_code, 200)
