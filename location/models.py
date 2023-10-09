# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TblLocation(models.Model):
    user_type = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=64, blank=True, null=True)
    name = models.CharField(max_length=64)
    parent_id = models.IntegerField(blank=True, null=True)
    location_type_id = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=128, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    delete_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_location'


class TblLine(models.Model):
    id = models.IntegerField(primary_key=True)
    user_type = models.IntegerField(blank=True, null=True)
    code = models.CharField(unique=True, max_length=32, blank=True, null=True)
    name = models.CharField(unique=True, max_length=32, blank=True, null=True)
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


class TblStation(models.Model):
    id = models.IntegerField(primary_key=True)
    user_type = models.IntegerField(blank=True, null=True)
    code = models.CharField(unique=True, max_length=32)
    name = models.CharField(max_length=32)
    name_en = models.CharField(max_length=32, blank=True, null=True)
    diagram = models.CharField(max_length=32, blank=True, null=True)
    description = models.CharField(max_length=128, blank=True, null=True)
    line_id = models.IntegerField(blank=True, null=True)
    position = models.CharField(max_length=10, blank=True, null=True)
    cross_station_ids = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    delete_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_station'


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
