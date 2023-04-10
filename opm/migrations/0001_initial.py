# Generated by Django 4.1.7 on 2023-03-09 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TblOperationMsg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('user_type', models.IntegerField(blank=True, null=True)),
                ('opm_src', models.IntegerField(blank=True, null=True)),
                ('op_level', models.IntegerField(blank=True, null=True)),
                ('station', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('display_region', models.IntegerField()),
                ('play_mode', models.IntegerField()),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('react', models.PositiveIntegerField(blank=True, null=True)),
                ('count', models.IntegerField(blank=True, null=True)),
                ('create_user', models.CharField(blank=True, max_length=64, null=True)),
                ('send_user', models.CharField(blank=True, max_length=64, null=True)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('update_time', models.DateTimeField(blank=True, null=True)),
                ('delete_time', models.DateTimeField(blank=True, null=True)),
                ('interval', models.IntegerField(blank=True, null=True)),
                ('period', models.CharField(blank=True, max_length=255, null=True)),
                ('begin_time', models.CharField(blank=True, max_length=255, null=True)),
                ('stop_time', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('real_begin_time', models.DateTimeField(blank=True, null=True)),
                ('real_end_time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tbl_operation_msg',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblOperationMsgDeviceRel',
            fields=[
                ('device_id', models.IntegerField(primary_key=True, serialize=False)),
                ('type', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=128, null=True)),
                ('result', models.IntegerField()),
                ('send_time', models.DateTimeField(blank=True, null=True)),
                ('rep_time', models.DateTimeField(blank=True, null=True)),
                ('update_time', models.DateTimeField(blank=True, null=True)),
                ('delete_time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tbl_operation_msg_device_rel',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblOperationMsgLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('user_type', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=32, null=True)),
                ('level', models.IntegerField(blank=True, null=True)),
                ('max_len', models.IntegerField(blank=True, null=True)),
                ('param', models.CharField(blank=True, max_length=1024, null=True)),
                ('display_region', models.IntegerField()),
                ('play_mode', models.IntegerField()),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('update_time', models.DateTimeField(blank=True, null=True)),
                ('delete_time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tbl_operation_msg_level',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblOperationMsgTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.IntegerField(blank=True, null=True)),
                ('title', models.CharField(max_length=32)),
                ('description', models.CharField(blank=True, max_length=1024, null=True)),
                ('content', models.TextField()),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('update_time', models.DateTimeField(blank=True, null=True)),
                ('delete_time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tbl_operation_msg_template',
                'managed': False,
            },
        ),
    ]