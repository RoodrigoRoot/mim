# Generated by Django 3.1.4 on 2020-12-12 16:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField(verbose_name='Datebirth')),
                ('create_at', models.DateTimeField(auto_now=True, verbose_name='Created')),
                ('phone', models.CharField(max_length=15, verbose_name='Phone')),
                ('clabe', models.CharField(max_length=50, verbose_name='Clabe')),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
            },
        ),
        migrations.CreateModel(
            name='Banks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Bank')),
            ],
            options={
                'verbose_name': 'Bank',
                'verbose_name_plural': 'Banks',
            },
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Páis')),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='StatusUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False, verbose_name='Status User')),
            ],
            options={
                'verbose_name': 'Status User',
                'verbose_name_plural': 'Status Users',
            },
        ),
        migrations.CreateModel(
            name='Codes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, verbose_name='Code')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Accounts.accounts', verbose_name='Account')),
            ],
            options={
                'verbose_name': 'Code',
                'verbose_name_plural': 'Codes',
            },
        ),
        migrations.CreateModel(
            name='Benefits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200, verbose_name='Full Name')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Created')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Updated')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Accounts.accounts', verbose_name='User')),
            ],
            options={
                'verbose_name': 'Benefit',
                'verbose_name_plural': 'Benefits',
            },
        ),
        migrations.AddField(
            model_name='accounts',
            name='bank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.banks', verbose_name='Bank'),
        ),
        migrations.AddField(
            model_name='accounts',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.countries', verbose_name='Country'),
        ),
        migrations.AddField(
            model_name='accounts',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.statususer', verbose_name='Status User'),
        ),
        migrations.AddField(
            model_name='accounts',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]