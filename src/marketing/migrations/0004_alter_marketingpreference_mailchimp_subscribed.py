# Generated by Django 5.1.4 on 2024-12-21 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0003_auto_20171018_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketingpreference',
            name='mailchimp_subscribed',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]