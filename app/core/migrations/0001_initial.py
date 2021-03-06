# Generated by Django 2.2 on 2020-12-15 17:34

import core.utils
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CharityModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Charity', max_length=254)),
                ('description', models.TextField()),
                ('donation', models.DecimalField(decimal_places=0, default=5, max_digits=1)),
                ('image', models.ImageField(default='charity/default.jpg', upload_to=core.utils.image_file_name)),
            ],
            options={
                'verbose_name': 'Charity Action',
                'verbose_name_plural': 'Charity Actions',
            },
        ),
        migrations.CreateModel(
            name='ProjectModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=254)),
                ('description', models.TextField()),
                ('phase', models.CharField(choices=[('proposed', 'proposed'), ('analysis', 'analysis'), ('development', 'development'), ('testing', 'testing'), ('deployment', 'deployment')], default='proposed', max_length=254)),
                ('budget', models.IntegerField(default=450, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(450)])),
                ('image_schedule', models.ImageField(default='schedules/default.png', upload_to=core.utils.schedule_file_name)),
                ('proposed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='TeamRequirementsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('python', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('html', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('js', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('css', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('db', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ProjectModel')),
            ],
            options={
                'verbose_name': 'Team Requirements',
                'verbose_name_plural': 'Team Requirements',
            },
        ),
        migrations.CreateModel(
            name='TeamMembershipModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('committed_skill', models.CharField(choices=[('html', 'html'), ('css', 'css'), ('js', 'js'), ('db', 'db'), ('python', 'python')], default='html', max_length=254)),
                ('member_name', models.CharField(default='none', max_length=254)),
                ('member_portrait', models.CharField(default='none', max_length=254)),
                ('member_personality', models.CharField(default='none', max_length=254)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ProjectModel')),
            ],
            options={
                'verbose_name': 'Team Membership',
                'verbose_name_plural': 'Team Memberships',
            },
        ),
        migrations.CreateModel(
            name='ProjectMessageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('message_date', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ProjectModel')),
            ],
            options={
                'verbose_name': 'Project Message',
                'verbose_name_plural': 'Projects Messages',
            },
        ),
        migrations.CreateModel(
            name='MyProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(blank=True, default='guest', max_length=254)),
                ('personality', models.CharField(blank=True, default='', max_length=254)),
                ('image', models.ImageField(default='portraits/default.jpg', upload_to=core.utils.content_file_name)),
                ('my_wallet', models.DecimalField(decimal_places=0, default=0, max_digits=6)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'User Profiles',
            },
        ),
        migrations.CreateModel(
            name='IssueModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=254)),
                ('description', models.TextField()),
                ('cost', models.IntegerField(default=10, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(450)])),
                ('assignee', models.CharField(default='none', max_length=254)),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ProjectModel')),
            ],
            options={
                'verbose_name': 'Project Issue',
                'verbose_name_plural': 'Projects Issues',
            },
        ),
        migrations.CreateModel(
            name='DonationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donor', models.CharField(default='Donor', max_length=50)),
                ('date', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField(default=5)),
                ('charity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.CharityModel')),
            ],
            options={
                'verbose_name': 'Charity Donation',
                'verbose_name_plural': 'Charity Donations',
            },
        ),
    ]
