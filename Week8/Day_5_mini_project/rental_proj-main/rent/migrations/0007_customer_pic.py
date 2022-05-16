
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0006_vehicle_image_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='pic',
            field=models.ImageField(null=True, upload_to='customers/'),
        ),
    ]
