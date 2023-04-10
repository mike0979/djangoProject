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
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    react = models.PositiveIntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    create_user = models.CharField(max_length=64, blank=True, null=True)
    send_user = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    delete_time = models.DateTimeField(blank=True, null=True)
    interval = models.IntegerField(blank=True, null=True)
    period = models.CharField(max_length=255, blank=True, null=True)
    begin_time = models.CharField(max_length=255, blank=True, null=True)
    stop_time = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    real_begin_time = models.DateTimeField(blank=True, null=True)
    real_end_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_operation_msg'


class TblOperationMsgDeviceRel(models.Model):
    device_id = models.IntegerField(primary_key=True)
    type = models.IntegerField(blank=True, null=True)
    operation_msg = models.ForeignKey(TblOperationMsg, models.DO_NOTHING)
    description = models.CharField(max_length=128, blank=True, null=True)
    result = models.IntegerField()
    send_time = models.DateTimeField(blank=True, null=True)
    rep_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    delete_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_operation_msg_device_rel'
        unique_together = (('device_id', 'operation_msg'),)


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


class TblOperationMsgTemplate(models.Model):
    user_type = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=1024, blank=True, null=True)
    level = models.ForeignKey(TblOperationMsgLevel, models.DO_NOTHING)
    content = models.TextField()
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    delete_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_operation_msg_template'
