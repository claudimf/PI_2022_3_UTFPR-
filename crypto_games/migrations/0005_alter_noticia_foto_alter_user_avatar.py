# Generated by Django 4.0.3 on 2022-03-12 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto_games', '0004_noticia_foto_alter_user_email_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='foto',
            field=models.ImageField(blank=True, upload_to='noticia/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='atavar/'),
        ),
    ]