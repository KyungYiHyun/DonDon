# Generated by Django 4.2.16 on 2024-11-27 07:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SavingProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_co_no', models.TextField()),
                ('kor_co_nm', models.TextField()),
                ('fin_prdt_cd', models.TextField()),
                ('fin_prdt_nm', models.TextField()),
                ('join_way', models.TextField(null=True)),
                ('mtrt_int', models.TextField()),
                ('spcl_cnd', models.TextField()),
                ('join_deny', models.TextField()),
                ('join_member', models.TextField()),
                ('etc_note', models.TextField()),
                ('max_limit', models.TextField(null=True)),
                ('fin_grp_cd', models.TextField()),
                ('intr_rate_type', models.TextField()),
                ('intr_rate_type_nm', models.TextField()),
                ('rsrv_type', models.TextField()),
                ('rsrv_type_nm', models.TextField()),
                ('save_trm', models.TextField()),
                ('intr_rate', models.TextField()),
                ('intr_rate2', models.TextField()),
                ('like_users', models.ManyToManyField(related_name='like_savingproducts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DepositProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_co_no', models.TextField()),
                ('fin_prdt_cd', models.TextField()),
                ('kor_co_nm', models.TextField()),
                ('fin_prdt_nm', models.TextField()),
                ('mtrt_int', models.TextField()),
                ('etc_note', models.TextField()),
                ('join_deny', models.TextField()),
                ('join_member', models.TextField()),
                ('join_way', models.TextField()),
                ('spcl_cnd', models.TextField()),
                ('max_limit', models.TextField(null=True)),
                ('fin_grp_cd', models.TextField()),
                ('intr_rate', models.FloatField()),
                ('intr_rate_type', models.TextField()),
                ('intr_rate_type_nm', models.TextField()),
                ('intr_rate2', models.FloatField(null=True)),
                ('save_trm', models.IntegerField()),
                ('like_users', models.ManyToManyField(related_name='like_depositproducts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='savingproducts',
            constraint=models.UniqueConstraint(fields=('fin_co_no', 'fin_prdt_cd', 'save_trm', 'intr_rate_type_nm', 'intr_rate', 'intr_rate2'), name='unique_product_term_rate_type2'),
        ),
        migrations.AddConstraint(
            model_name='depositproducts',
            constraint=models.UniqueConstraint(fields=('fin_co_no', 'fin_prdt_cd', 'save_trm', 'intr_rate_type_nm', 'intr_rate', 'intr_rate2'), name='unique_product_term_rate_type'),
        ),
    ]
