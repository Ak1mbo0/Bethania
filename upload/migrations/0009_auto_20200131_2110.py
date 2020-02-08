# Generated by Django 2.2.7 on 2020-01-31 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0008_auto_20200107_1837'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=40)),
                ('Tema', models.CharField(max_length=40, null=True)),
                ('Documento', models.FileField(upload_to='pdf/')),
                ('Status', models.CharField(choices=[('p', 'Published'), ('h', 'Hidden')], default='h', max_length=1)),
                ('Tipo', models.CharField(default='Aula', max_length=40)),
                ('Periodo', models.CharField(default=1, max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='ficha',
            name='Periodo',
            field=models.CharField(default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='video',
            name='Periodo',
            field=models.CharField(default=1, max_length=1),
        ),
    ]