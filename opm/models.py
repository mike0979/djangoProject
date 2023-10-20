# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TblOperationMsg(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    user_type = models.IntegerField(blank=True, null=True)
    opm_src = models.IntegerField(blank=True, null=True)
    op_level = models.IntegerField(blank=True, null=True)
    station = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    level = models.ForeignKey('TblOperationMsgLevel', models.DO_NOTHING, db_column='level', blank=True, null=True)
    display_region = models.IntegerField()
    play_mode = models.IntegerField()
    start_time = models.CharField(max_length=15, blank=True, null=True)
    end_time = models.CharField(max_length=15, blank=True, null=True)
    react = models.PositiveIntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    create_user = models.CharField(max_length=64, blank=True, null=True)
    send_user = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    delete_time = models.DateTimeField(blank=True, null=True)
    interval = models.IntegerField(blank=True, null=True)
    period = models.CharField(max_length=255, blank=True, null=True)
    begin_time = models.CharField(max_length=15, blank=True, null=True)
    stop_time = models.CharField(max_length=15, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    real_begin_time = models.CharField(max_length=15, blank=True, null=True)
    real_end_time = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_operation_msg'


class TblOperationMsgLevel(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    user_type = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=32, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    max_len = models.IntegerField(blank=True, null=True)
    param = models.CharField(max_length=1024, blank=True, null=True)
    display_region = models.IntegerField()
    play_mode = models.IntegerField()
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    delete_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_operation_msg_level'


class TblOperationMsgDeviceRel(models.Model):
    device = models.OneToOneField('TblDevice', models.DO_NOTHING, primary_key=True)
    type = models.IntegerField(blank=True, null=True)
    operation_msg = models.ForeignKey(TblOperationMsg, models.DO_NOTHING)
    description = models.CharField(max_length=128, blank=True, null=True)
    result = models.IntegerField()
    publish_status = models.IntegerField(blank=True, null=True)
    send_time = models.DateTimeField(blank=True, null=True)
    rep_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    delete_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_operation_msg_device_rel'
        unique_together = (('device', 'operation_msg'),)


class TblOperationMsgTemplate(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    user_type = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=1024, blank=True, null=True)
    level_id = models.IntegerField(blank=True, null=True)
    content = models.TextField()
    pos = models.IntegerField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    child_ids = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    delete_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_operation_msg_template'


class TblDevice(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    user_type = models.IntegerField(blank=True, null=True)
    code = models.CharField(unique=True, max_length=32)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=128, blank=True, null=True)
    device_type = models.ForeignKey('TblDeviceType', models.DO_NOTHING, db_column='device_type', blank=True, null=True)
    location = models.ForeignKey('TblLocation', models.DO_NOTHING, blank=True, null=True)
    host_device_id = models.IntegerField(blank=True, null=True)
    line = models.ForeignKey('TblLine', models.DO_NOTHING, blank=True, null=True)
    station = models.ForeignKey('TblStation', models.DO_NOTHING, blank=True, null=True)
    ip = models.CharField(max_length=64, blank=True, null=True)
    mac = models.CharField(max_length=20, blank=True, null=True)
    resolution = models.CharField(max_length=32, blank=True, null=True)
    life_cycle = models.IntegerField(blank=True, null=True)
    power_device = models.IntegerField(blank=True, null=True)
    power_num = models.IntegerField(blank=True, null=True)
    service_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    delete_time = models.DateTimeField(blank=True, null=True)
    software_version = models.CharField(max_length=255, blank=True, null=True)
    monitor_flag = models.IntegerField(blank=True, null=True)
    line_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_device'


class TblStation(models.Model):
    id = models.OneToOneField('TblLocation', models.DO_NOTHING, db_column='id', primary_key=True)
    user_type = models.IntegerField(blank=True, null=True)
    code = models.CharField(unique=True, max_length=32)
    name = models.CharField(max_length=32)
    name_en = models.CharField(max_length=32, blank=True, null=True)
    diagram = models.CharField(max_length=32, blank=True, null=True)
    description = models.CharField(max_length=128, blank=True, null=True)
    line = models.ForeignKey('TblLine', models.DO_NOTHING, blank=True, null=True)
    position = models.CharField(max_length=10, blank=True, null=True)
    cross_station_ids = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    delete_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_station'


class TblTrain(models.Model):
    id = models.IntegerField(primary_key=True)
    user_type = models.IntegerField(blank=True, null=True)
    code = models.CharField(unique=True, max_length=32)
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=True)
    head_control_ip = models.CharField(max_length=32, blank=True, null=True)
    tail_control_ip = models.CharField(max_length=32, blank=True, null=True)
    head_lcd_ip = models.CharField(max_length=32, blank=True, null=True)
    tail_lcd_ip = models.CharField(max_length=32, blank=True, null=True)
    line = models.ForeignKey('TblLine', models.DO_NOTHING, blank=True, null=True)
    cars = models.IntegerField(blank=True, null=True)
    head_camera_num = models.IntegerField(blank=True, null=True)
    body_camera_num = models.IntegerField(blank=True, null=True)
    pantograph_num = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    delete_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_train'


class TblLine(models.Model):
    id = models.OneToOneField('TblLocation', models.DO_NOTHING, db_column='id', primary_key=True)
    user_type = models.IntegerField(blank=True, null=True)
    code = models.CharField(unique=True, max_length=32)
    name = models.CharField(unique=True, max_length=32)
    name_en = models.CharField(max_length=32, blank=True, null=True)
    description = models.CharField(max_length=128, blank=True, null=True)
    monitor_mode = models.IntegerField(blank=True, null=True)
    monitor_status = models.IntegerField(blank=True, null=True)
    back_color = models.IntegerField(blank=True, null=True)
    back_image = models.CharField(max_length=256, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    delete_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_line'


class TblLocation(models.Model):
    user_type = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=64, blank=True, null=True)
    name = models.CharField(max_length=64)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    location_type = models.ForeignKey('TblLocationType', models.DO_NOTHING, blank=True, null=True)
    description = models.CharField(max_length=128, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    delete_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_location'


class TblLocationType(models.Model):
    code = models.CharField(max_length=64, blank=True, null=True)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=128, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    delete_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_location_type'


class TblDeviceType(models.Model):
    user_type = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=32, blank=True, null=True)
    description = models.CharField(max_length=128, blank=True, null=True)
    host = models.IntegerField()
    icon = models.CharField(max_length=32, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    delete_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_device_type'
