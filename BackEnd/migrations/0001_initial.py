# Generated by Django 4.2.6 on 2023-10-26 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddCates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='img')),
                ('catname', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='AddItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='img')),
                ('fname', models.CharField(max_length=500)),
                ('desc', models.TextField()),
                ('price', models.IntegerField(blank=True, null=True)),
                ('cname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='BackEnd.addcates')),
            ],
        ),
        migrations.CreateModel(
            name='AddAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=300)),
                ('mobile', models.IntegerField()),
                ('state', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=300)),
                ('pincode', models.IntegerField()),
                ('address', models.TextField()),
                ('address_type', models.CharField(max_length=200)),
                ('addressId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='BackEnd.additems')),
            ],
        ),
    ]