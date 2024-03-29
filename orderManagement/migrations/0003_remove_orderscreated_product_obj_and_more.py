# Generated by Django 5.0 on 2024-01-07 09:07

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderManagement', '0002_alter_orderscreated_status'),
        ('productManagement', '0002_productscustomer_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderscreated',
            name='product_obj',
        ),
        migrations.RemoveField(
            model_name='orderscreated',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='orderscreated',
            name='status',
        ),
        migrations.CreateModel(
            name='lineOrderCreated',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_unique_id', models.CharField(max_length=10, null=True)),
                ('quantity', models.IntegerField(null=True)),
                ('status', models.CharField(default='pending', max_length=15)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('product_obj', models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_obj', to='productManagement.productscustomer')),
            ],
            options={
                'db_table': 'line_order_created',
                'managed': True,
            },
        ),
    ]
