# Generated by Django 3.2.4 on 2021-06-15 04:54

from django.db import migrations, models




class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PSM25Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField(max_length=5000, verbose_name='Текст вопроса')),
            ],
        ),
    ]