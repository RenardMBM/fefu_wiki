# Generated by Django 4.0.5 on 2022-07-01 21:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='StoryComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.BooleanField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comment.commentrating')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='content')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('dislike', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='comment.commentrating')),
                ('like', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='comment.commentrating')),
                ('teacher_article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='article.teacherarticle')),
            ],
        ),
    ]
