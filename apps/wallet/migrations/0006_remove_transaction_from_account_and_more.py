# Generated by Django 4.1.7 on 2023-03-15 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0005_remove_category_is_transfer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='from_account',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='to_account',
        ),
        migrations.AddField(
            model_name='transaction',
            name='account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='wallet.account', verbose_name='Счет'),
            preserve_default=False,
        ),
    ]
