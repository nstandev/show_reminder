# Generated by Django 2.2 on 2019-04-25 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('oap_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='RadioStation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('freq', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('schedule', models.DateField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reminder.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ShowTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reminder.Show')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reminder.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='ShowHost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reminder.Host')),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reminder.Show')),
            ],
        ),
        migrations.AddField(
            model_name='show',
            name='host',
            field=models.ManyToManyField(through='reminder.ShowHost', to='reminder.Host'),
        ),
        migrations.AddField(
            model_name='show',
            name='radio_station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reminder.RadioStation'),
        ),
        migrations.AddField(
            model_name='show',
            name='tag',
            field=models.ManyToManyField(through='reminder.ShowTag', to='reminder.Tag'),
        ),
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateField()),
                ('listener', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Listener')),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reminder.Show')),
            ],
        ),
        migrations.AddField(
            model_name='host',
            name='radio_station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reminder.RadioStation'),
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('occupation', models.CharField(max_length=30)),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reminder.Show')),
            ],
        ),
    ]
