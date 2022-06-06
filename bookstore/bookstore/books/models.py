# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Book(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    pub = models.ForeignKey('Publisher', models.DO_NOTHING)
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(max_length=30, blank=True, null=True)
    quantity = models.IntegerField()
    b_format = models.CharField(max_length=40, blank=True, null=True)
    prod_year = models.IntegerField()
    filesize = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Book'


class Checkout(models.Model):
    id = models.AutoField(primary_key=True)
    c = models.ForeignKey('Customer', models.DO_NOTHING)
    ch_type = models.CharField(max_length=15, blank=True, null=True)
    ch_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'Checkout'


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    c_name = models.CharField(max_length=20)
    c_email = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'Customer'


class Customerphone(models.Model):
    cust_phone = models.CharField(max_length=15)
    c = models.ForeignKey(Customer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'CustomerPhone'


class Media(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    pub = models.ForeignKey('Publisher', models.DO_NOTHING)
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(max_length=30, blank=True, null=True)
    quantity = models.IntegerField()
    m_link = models.CharField(max_length=40, blank=True, null=True)
    prod_year = models.IntegerField()
    filesize = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Media'


class Productcheckout(models.Model):
    id = models.AutoField(primary_key=True)
    prod = models.ForeignKey(Book, models.DO_NOTHING)
    ch = models.ForeignKey(Checkout, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ProductCheckout'


class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=40)
    city = models.CharField(max_length=20)
    zip = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'Publisher'


class Publisherphone(models.Model):
    pub_phone = models.CharField(max_length=15)
    pub = models.ForeignKey(Publisher, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'PublisherPhone'


class Source(models.Model):
    id = models.AutoField(primary_key=True)
    s_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'Source'


class Sourceproduct(models.Model):
    id = models.AutoField(primary_key=True)
    s = models.ForeignKey(Source, models.DO_NOTHING)
    prod = models.ForeignKey(Book, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'SourceProduct'


class Warehouse(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=20)
    zip = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'Warehouse'


class Warehouseproduct(models.Model):
    id = models.AutoField(primary_key=True)
    w = models.ForeignKey(Warehouse, models.DO_NOTHING)
    prod = models.ForeignKey(Book, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'WarehouseProduct'


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
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

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


class SqliteStat1(models.Model):
    tbl = models.TextField(blank=True, null=True)  # This field type is a guess.
    idx = models.TextField(blank=True, null=True)  # This field type is a guess.
    stat = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'sqlite_stat1'
