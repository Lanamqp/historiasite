# Generated by Django 5.1.4 on 2024-12-16 20:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Pagina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('descricao', models.TextField(default='')),
                ('texto', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Conteudo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('data_publicacao', models.DateField()),
                ('descricao', models.TextField(blank=True, null=True)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='conteudos_imagens/')),
                ('link', models.URLField(blank=True, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.categoria')),
                ('pagina', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='conteudos', to='app.pagina')),
            ],
            options={
                'verbose_name_plural': 'Conteúdos',
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pergunta', models.CharField(max_length=300)),
                ('alternativa_a', models.CharField(default='Alternativa A padrão', max_length=200)),
                ('alternativa_b', models.CharField(default='Alternativa B padrão', max_length=200)),
                ('alternativa_c', models.CharField(default='Alternativa C padrão', max_length=200)),
                ('alternativa_d', models.CharField(default='Alternativa D padrão', max_length=200)),
                ('resposta_correta', models.CharField(choices=[('A', 'Alternativa A'), ('B', 'Alternativa B'), ('C', 'Alternativa C'), ('D', 'Alternativa D')], max_length=1)),
                ('conteudo', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.conteudo')),
            ],
            options={
                'verbose_name_plural': 'Quizzes',
            },
        ),
        migrations.CreateModel(
            name='Subcategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.categoria')),
            ],
            options={
                'verbose_name_plural': 'Subcategorias',
            },
        ),
        migrations.AddField(
            model_name='conteudo',
            name='subcategoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='app.subcategoria'),
        ),
        migrations.CreateModel(
            name='Topico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('texto', models.TextField()),
                ('conteudo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topicos', to='app.conteudo')),
            ],
        ),
    ]
