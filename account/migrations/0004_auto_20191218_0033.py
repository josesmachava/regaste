# Generated by Django 2.2.2 on 2019-12-18 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20191218_0018'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Link',
            new_name='ReferralLink',
        ),
        migrations.AlterField(
            model_name='referral',
            name='referral_token',
            field=models.CharField(default='hDwfPllVHbGBspxAqw6teNu4rJPAjl3s', editable=False, max_length=4),
        ),
    ]