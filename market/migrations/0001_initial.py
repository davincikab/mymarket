# Generated by Django 3.0.2 on 2020-02-28 07:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('project_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField()),
                ('title', models.CharField(max_length=100)),
                ('timeframe', models.IntegerField(verbose_name='Number of Days')),
                ('created_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('orderid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('awarded_on', models.DateTimeField(auto_now=True)),
                ('delivery_date', models.DateTimeField()),
                ('isdone', models.BooleanField(default=False, verbose_name='Work Completed')),
                ('isclosed', models.BooleanField(default=False, verbose_name='Closed Order')),
                ('iscanceled', models.BooleanField(default=False, verbose_name='Cancel Order')),
                ('cost', models.IntegerField(verbose_name='Order Cost')),
                ('awarded_to', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='market.Projects')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='market.Projects')),
                ('reciever', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_reciever', to=settings.AUTH_USER_MODEL)),
                ('sender', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_sender', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
    ]
