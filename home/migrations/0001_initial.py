# Generated by Django 4.2.21 on 2025-05-21 13:35

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('tipo_usuario', models.CharField(choices=[('ASISTENTE', 'Asistente'), ('ORGANIZADOR', 'Organizador')], max_length=11)),
                ('telefono', models.CharField(blank=True, max_length=15)),
                ('groups', models.ManyToManyField(related_name='home_usuario_groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(related_name='home_usuario_permissions', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('tipo', models.CharField(choices=[('VIRTUAL', 'Virtual'), ('PRESENCIAL', 'Presencial')], max_length=10)),
                ('fecha', models.DateTimeField()),
                ('imagen', models.ImageField(upload_to='eventos/')),
                ('destacado', models.BooleanField(default=False)),
                ('enlace_virtual', models.URLField(blank=True)),
                ('direccion', models.TextField(blank=True)),
                ('ciudad', models.CharField(blank=True, max_length=100)),
                ('creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.usuario')),
            ],
        ),
    ]
