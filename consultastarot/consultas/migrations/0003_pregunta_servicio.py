# Generated by Django 4.2.5 on 2024-03-29 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0002_alter_consulta_fecha_consulta_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='pregunta',
            name='servicio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='consultas.serviciotarot'),
            preserve_default=False,
        ),
    ]