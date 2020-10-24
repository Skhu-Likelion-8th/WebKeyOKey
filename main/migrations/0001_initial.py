# Generated by Django 3.1 on 2020-10-24 21:50

from django.conf import settings
import django.contrib.auth.models
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
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('u_id', models.IntegerField(null=True, unique=True)),
                ('username', models.TextField(null=True)),
                ('phone', models.TextField(default='010')),
                ('answer', models.TextField(blank=True, max_length=200)),
                ('question_id', models.IntegerField(choices=[(1, '나의 보물 1호는?'), (2, '나의 고향은?'), (3, '붕어빵 먹을 때 가장 먼저 먹는 부위는?'), (4, '나의 MBTI는?'), (5, '돌잡이 때 잡은 것은?')], default=1)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
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
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ototal_price', models.IntegerField()),
                ('takeout', models.BooleanField(default=False)),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_name', models.CharField(max_length=200)),
                ('option_price', models.IntegerField()),
                ('checked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('total', models.IntegerField()),
                ('order_num', models.IntegerField()),
                ('baskets', models.ManyToManyField(blank=True, to='main.Basket')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('or_name', models.CharField(max_length=200)),
                ('or_num', models.IntegerField()),
                ('or_count', models.IntegerField()),
                ('or_takeout', models.BooleanField(default=False)),
                ('or_options', models.ManyToManyField(blank=True, to='main.Option')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_id', models.IntegerField(choices=[(1, '커피'), (2, '주스'), (3, '티'), (4, '스무디/프라푸치노'), (5, '논커피'), (6, '디저트')], default=1)),
                ('m_name', models.CharField(max_length=200)),
                ('m_info', models.TextField()),
                ('m_price', models.IntegerField()),
                ('m_img', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('m_takeout', models.BooleanField(default=False)),
                ('options', models.ManyToManyField(blank=True, to='main.Option')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='basket',
            name='b_options',
            field=models.ManyToManyField(blank=True, to='main.Option'),
        ),
        migrations.AddField(
            model_name='basket',
            name='menu_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selected_menu', to='main.menu'),
        ),
    ]
