# Generated by Django 5.1.4 on 2024-12-22 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0004_alter_marketingpreference_mailchimp_subscribed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketingpreference',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
