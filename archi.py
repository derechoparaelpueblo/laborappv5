# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.ForeignKey('UserProfileUserprofile', models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class Departamentos(models.Model):
    id_departamento = models.AutoField(primary_key=True)
    departamento = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'departamentos'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UserProfileUserprofile', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Municipios(models.Model):
    id_municipio = models.AutoField(primary_key=True)
    municipio = models.CharField(max_length=255)
    estado = models.PositiveIntegerField()
    departamento_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'municipios'


class UserProfileUserprofile(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    email = models.CharField(unique=True, max_length=255)
    name = models.CharField(max_length=255)
    is_active = models.IntegerField()
    is_staff = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_profile_userprofile'


class UserProfileUserprofileGroups(models.Model):
    userprofile = models.ForeignKey(UserProfileUserprofile, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_profile_userprofile_groups'
        unique_together = (('userprofile', 'group'),)


class UserProfileUserprofileUserPermissions(models.Model):
    userprofile = models.ForeignKey(UserProfileUserprofile, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_profile_userprofile_user_permissions'
        unique_together = (('userprofile', 'permission'),)
