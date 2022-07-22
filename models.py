# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
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


class BuyerBuyer(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    created_by = models.OneToOneField(AuthUser, models.DO_NOTHING)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    complete_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'buyer_buyer'


class CoreContact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=254)
    message = models.TextField()

    class Meta:
        managed = False
        db_table = 'core_contact'


class CoreFeedback(models.Model):
    name = models.CharField(max_length=40)
    feedback = models.CharField(max_length=500)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_feedback'


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


class LuckydrawDrawables(models.Model):
    draws_given = models.IntegerField()
    draws_done = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(BuyerBuyer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'luckydraw_drawables'


class LuckydrawLuckydrawproducts(models.Model):
    product_name = models.CharField(max_length=255)
    image = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'luckydraw_luckydrawproducts'


class LuckydrawLuckydraws(models.Model):
    draw = models.PositiveBigIntegerField()
    user = models.ForeignKey(BuyerBuyer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'luckydraw_luckydraws'


class LuckydrawWinners(models.Model):
    luckydraw = models.ForeignKey(LuckydrawLuckydrawproducts, models.DO_NOTHING)
    user = models.ForeignKey(BuyerBuyer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'luckydraw_winners'


class OrderOrder(models.Model):
    created_at = models.DateTimeField()
    paid_amount = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    buyer = models.ForeignKey(BuyerBuyer, models.DO_NOTHING, blank=True, null=True)
    order_status = models.SmallIntegerField()
    paid_slip = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'order_order'


class OrderOrderitem(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    quantity = models.IntegerField()
    order = models.ForeignKey(OrderOrder, models.DO_NOTHING)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING)
    buyer = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'order_orderitem'


class ProductCategory(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    ordering = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_category'


class ProductOrder(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    status = models.SmallIntegerField()
    order_at = models.DateTimeField()
    phone = models.CharField(max_length=21)
    address = models.CharField(max_length=256)
    town = models.CharField(max_length=56)
    postalcode = models.CharField(max_length=11)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_order'


class ProductOrderitem(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    quantity = models.IntegerField()
    order = models.ForeignKey(ProductOrder, models.DO_NOTHING)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_orderitem'


class ProductProduct(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    date_added = models.DateTimeField()
    image = models.CharField(max_length=100, blank=True, null=True)
    thumbnail = models.CharField(max_length=100, blank=True, null=True)
    category = models.ForeignKey(ProductCategory, models.DO_NOTHING)
    available_quantity = models.IntegerField()
    product_status = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'product_product'


class ProductProductimage(models.Model):
    image = models.CharField(max_length=100, blank=True, null=True)
    thumbnail = models.CharField(max_length=100, blank=True, null=True)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_productimage'


class VendorVendor(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    created_by = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'vendor_vendor'
