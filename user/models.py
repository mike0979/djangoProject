# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TblUser(models.Model):
    type = models.IntegerField(blank=True, null=True)
    account = models.CharField(unique=True, max_length=64, blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    department = models.CharField(max_length=128, blank=True, null=True)
    phone = models.CharField(max_length=16, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    address = models.CharField(max_length=128, blank=True, null=True)
    bk_phone = models.CharField(max_length=16, blank=True, null=True)
    description = models.CharField(max_length=128, blank=True, null=True)
    password = models.CharField(max_length=64, blank=True, null=True)
    op_level = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    login_ip = models.CharField(max_length=32, blank=True, null=True)
    heartbeat = models.DateTimeField(blank=True, null=True)
    login_status = models.IntegerField(blank=True, null=True)
    last_login_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    delete_time = models.DateTimeField(blank=True, null=True)
    password_wrong_num = models.IntegerField(blank=True, null=True)
    flag = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_user'


class TblRole(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    user_type = models.PositiveIntegerField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=32, blank=True, null=True)
    type = models.IntegerField()
    flag = models.IntegerField()
    description = models.CharField(max_length=128, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    delete_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_role'


class TblUserRoleRel(models.Model):
    user = models.OneToOneField(TblUser, models.DO_NOTHING, primary_key=True)
    role = models.ForeignKey(TblRole, models.DO_NOTHING)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    delete_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_user_role_rel'
        unique_together = (('user', 'role'),)


class TblRoleFunctionRel(models.Model):
    function = models.OneToOneField('TblFunctionPermission', models.DO_NOTHING, primary_key=True)
    role = models.ForeignKey(TblRole, models.DO_NOTHING)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    delete_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_role_function_rel'
        unique_together = (('function', 'role'),)


class TblRoleLocationRel(models.Model):
    role = models.OneToOneField(TblRole, models.DO_NOTHING, primary_key=True)
    location = models.ForeignKey('TblLocation', models.DO_NOTHING)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    delete_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_role_location_rel'
        unique_together = (('role', 'location'),)


class TblFunctionPermission(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    user_type = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=64, blank=True, null=True)
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    sort = models.IntegerField()
    url = models.CharField(max_length=64, blank=True, null=True)
    icon = models.CharField(max_length=64, blank=True, null=True)
    func_type = models.IntegerField(blank=True, null=True)
    component = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    delete_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_function_permission'


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
