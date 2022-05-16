from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0005_auto_20210531_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='image_link',
            field=models.URLField(null=True),
        ),
    ]
