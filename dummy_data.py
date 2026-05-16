import os

import django
from django.contrib.auth import get_user_model
from faker import Faker
from django.utils.text import slugify


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from blog.models import Post


def create_posts(num_posts=10):
    fake = Faker()
    User = get_user_model()
    user = User.objects.first()  

    for _ in range(num_posts):
        title = fake.sentence()
        body = fake.paragraph()
        slug = slugify(title)
        
        Post.objects.create(
            title=title,
            body=body,
            author=user,
            slug=slug
        )

if __name__ == '__main__':
    create_posts()
