# Generated by Django 3.0.2 on 2020-02-28 07:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('market', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('amount', models.IntegerField()),
                ('payment_method', models.CharField(choices=[('P', 'PAYPAL'), ('MP', 'MPESA')], max_length=15, verbose_name='Payment Method')),
                ('from_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_payer', to=settings.AUTH_USER_MODEL)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='market.Orders')),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='market.Projects')),
                ('to_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_payee', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payment',
            },
        ),
    ]
