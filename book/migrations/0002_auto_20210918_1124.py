# Generated by Django 3.2.7 on 2021-09-18 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='chapter_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='line_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='scope_depth',
            field=models.IntegerField(default=6),
        ),
        migrations.AddField(
            model_name='sentence',
            name='chapter',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='sentence',
            name='chapter_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='sentence',
            name='line_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]