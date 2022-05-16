
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rent', '0003_vehicle_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='created_by',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, to='auth.user'),
            preserve_default=False,
        ),
    ]
