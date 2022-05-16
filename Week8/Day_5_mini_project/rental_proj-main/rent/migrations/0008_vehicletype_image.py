
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0007_customer_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicletype',
            name='image',
            field=models.ImageField(default='vehicle_types/default.jpg', upload_to='vehicle_types/'),
        ),
    ]
