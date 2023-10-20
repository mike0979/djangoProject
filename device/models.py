# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TblDevice(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    user_type = models.IntegerField(blank=True, null=True)
    code = models.CharField(unique=True, max_length=32)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=128, blank=True, null=True)
    device_type = models.IntegerField(blank=True, null=True)
    location = models.ForeignKey('TblLocation', models.DO_NOTHING, blank=True, null=True)
    host_device_id = models.IntegerField(blank=True, null=True)
    line_id = models.IntegerField(blank=True, null=True)
    station_id = models.IntegerField(blank=True, null=True)
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


class TblLocation(models.Model):
    user_type = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=32)
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
    code = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=128, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    delete_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_location_type'
