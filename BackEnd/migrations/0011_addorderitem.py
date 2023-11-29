# Generated by Django 4.2.6 on 2023-10-27 06:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BackEnd', '0010_delete_addorderitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddOrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('any_sugg', models.TextField()),
                ('addressId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='BackEnd.addaddress')),
                ('itemId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='BackEnd.additems')),
                ('userId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
