# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AdminUser(models.Model):
    admin_id = models.AutoField(primary_key=True)
    role = models.ForeignKey('Role', models.DO_NOTHING, blank=True, null=True)
    admin_name = models.CharField(max_length=32)
    admin_pwd = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'admin_user'


class ApplicatAddressList(models.Model):
    address_id = models.AutoField(primary_key=True)
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid')
    address_name = models.CharField(max_length=20, blank=True, null=True)
    tel = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'applicat_address_list'


class ApplicatUserSocial(models.Model):
    social_id = models.AutoField(primary_key=True)
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid')
    rela_name = models.CharField(max_length=20, blank=True, null=True)
    tel = models.CharField(max_length=13, blank=True, null=True)
    tag = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'applicat_user_social'


class ApplicationTelLog(models.Model):
    log_id = models.AutoField(primary_key=True)
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid')
    inter_tag = models.CharField(max_length=20, blank=True, null=True)
    address_tag = models.CharField(max_length=22, blank=True, null=True)
    talk_date = models.DateTimeField(blank=True, null=True)
    talk_duration = models.CharField(max_length=30, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    phone_address = models.CharField(max_length=22, blank=True, null=True)
    sur_te_charge = models.CharField(max_length=22, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'application_tel_log'


class AuthRole(models.Model):
    authority = models.ForeignKey('Authority', models.DO_NOTHING, primary_key=True)
    role = models.ForeignKey('Role', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_role'
        unique_together = (('authority', 'role'),)


class Authority(models.Model):
    authority_id = models.AutoField(primary_key=True)
    auth_name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'authority'


class BankcType(models.Model):
    bankt_id = models.AutoField(primary_key=True)
    bankt_nm = models.CharField(max_length=32, blank=True, null=True)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bankc_type'


class CaseStatus(models.Model):
    cstatus_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'case_status'


class Caseform(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    admin = models.ForeignKey(AdminUser, models.DO_NOTHING, blank=True, null=True)
    case_id = models.AutoField(primary_key=True)
    caot_id = models.IntegerField(blank=True, null=True)
    cstatus = models.ForeignKey(CaseStatus, models.DO_NOTHING, blank=True, null=True)
    exa_admin = models.ForeignKey('ExaminRefuseReason', models.DO_NOTHING, blank=True, null=True)
    payment_amount = models.FloatField()
    will_pay = models.FloatField()
    after_day_pay = models.IntegerField()
    create_time = models.DateTimeField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    overdua_day = models.IntegerField(blank=True, null=True)
    examin_result = models.TextField(blank=True, null=True)
    loan_time = models.DateTimeField(blank=True, null=True)
    column_16 = models.CharField(db_column='Column_16', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'caseform'


class CuikuanTel(models.Model):
    admin = models.ForeignKey(AdminUser, models.DO_NOTHING, primary_key=True)
    case = models.ForeignKey(Caseform, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuikuan_tel'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class ExaminRefuseReason(models.Model):
    admin = models.ForeignKey(AdminUser, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'examin_refuse_reason'


class Goods(models.Model):
    good_id = models.CharField(primary_key=True, max_length=64)
    good_name = models.CharField(max_length=32, blank=True, null=True)
    category = models.ForeignKey('GoodsCategory', models.DO_NOTHING, blank=True, null=True)
    brand = models.ForeignKey('GoodsBrand', models.DO_NOTHING, blank=True, null=True)
    product_name = models.CharField(max_length=50, blank=True, null=True)
    short_product_name = models.CharField(max_length=32, blank=True, null=True)
    sku_key_1 = models.CharField(max_length=32, blank=True, null=True)
    sku_key_2 = models.CharField(max_length=32, blank=True, null=True)
    sku_key_3 = models.CharField(max_length=32, blank=True, null=True)
    product_flag = models.IntegerField(blank=True, null=True)
    min_firstpay = models.IntegerField(blank=True, null=True)
    is_product_up_down = models.IntegerField(blank=True, null=True)
    real_amount = models.IntegerField(blank=True, null=True)
    mart_amount = models.IntegerField(blank=True, null=True)
    fq_num = models.IntegerField(blank=True, null=True)
    product_info = models.CharField(max_length=100, blank=True, null=True)
    delivery_time = models.CharField(max_length=64, blank=True, null=True)
    gift_list = models.CharField(max_length=200, blank=True, null=True)
    fe_params = models.TextField(blank=True, null=True)
    slider_imgs = models.TextField(blank=True, null=True)
    detail_imgs = models.TextField(blank=True, null=True)
    create_time = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods'


class GoodsBrand(models.Model):
    brand_id = models.IntegerField(primary_key=True)
    create_time = models.CharField(max_length=64, blank=True, null=True)
    brand_name = models.CharField(max_length=32, blank=True, null=True)
    brand_name_ch = models.CharField(max_length=32, blank=True, null=True)
    brand_name_en = models.CharField(max_length=32, blank=True, null=True)
    category = models.ForeignKey('GoodsCategory', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods_brand'


class GoodsCategory(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=32, blank=True, null=True)
    create_time = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods_category'


class InternetTagList(models.Model):
    tag_id = models.AutoField(primary_key=True)
    tel = models.CharField(max_length=13, blank=True, null=True)
    tag = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'internet_tag_list'


class MyIntegral(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    integral_id = models.AutoField(primary_key=True)
    in_nums = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'my_integral'


class MyWallet(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    wallet_id = models.AutoField(primary_key=True)
    w_money = models.FloatField()

    class Meta:
        managed = False
        db_table = 'my_wallet'


class OrderStatus(models.Model):
    orderst_id = models.AutoField(primary_key=True)
    orderst_tname = models.CharField(max_length=64)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'order_status'


class Orderform(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    orderst = models.ForeignKey(OrderStatus, models.DO_NOTHING, blank=True, null=True)
    caot_id = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField()
    will_pay_money = models.FloatField()
    order_id = models.AutoField(primary_key=True)
    good = models.ForeignKey('Products', models.DO_NOTHING, blank=True, null=True)
    per_month_pay = models.FloatField(blank=True, null=True)
    is_continue_borrow = models.IntegerField(blank=True, null=True)
    per_month_overdua_day = models.IntegerField(blank=True, null=True)
    all_overdua_days = models.IntegerField(blank=True, null=True)
    per_month_interest = models.FloatField(blank=True, null=True)
    all_refunds = models.FloatField(blank=True, null=True)
    true_refunds = models.FloatField(blank=True, null=True)
    start_time = models.DateTimeField()
    lend_money = models.FloatField(blank=True, null=True)
    examin_reason = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orderform'


class OverduaRule(models.Model):
    or_id = models.AutoField(primary_key=True)
    or_day = models.IntegerField()
    or_money = models.FloatField()

    class Meta:
        managed = False
        db_table = 'overdua_rule'


class Products(models.Model):
    good_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=64, blank=True, null=True)
    short_product = models.TextField(blank=True, null=True)
    product_desc = models.TextField(blank=True, null=True)
    key1 = models.CharField(max_length=32, blank=True, null=True)
    key2 = models.CharField(max_length=32, blank=True, null=True)
    key3 = models.CharField(max_length=32, blank=True, null=True)
    product_flag = models.IntegerField(blank=True, null=True)
    min_firstpay = models.FloatField(blank=True, null=True)
    is_prduct_up_down = models.IntegerField(blank=True, null=True)
    real_amount = models.FloatField(blank=True, null=True)
    mart_amount = models.FloatField(blank=True, null=True)
    fq_num = models.IntegerField(blank=True, null=True)
    delivery_time = models.DateTimeField()
    gift_list = models.TextField(blank=True, null=True)
    fe_params = models.TextField(blank=True, null=True)
    slider_imgs = models.CharField(max_length=64, blank=True, null=True)
    detail_imgs = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'


class ProductsChildType(models.Model):
    productcht_id = models.AutoField(primary_key=True)
    producttp = models.ForeignKey('ProductsType', models.DO_NOTHING, blank=True, null=True)
    good = models.ForeignKey(Products, models.DO_NOTHING, blank=True, null=True)
    productcht_name = models.CharField(max_length=64)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'products_child_type'


class ProductsType(models.Model):
    producttp_id = models.AutoField(primary_key=True)
    producttp_name = models.CharField(max_length=64)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'products_type'


class RepayHistory(models.Model):
    case = models.ForeignKey(Caseform, models.DO_NOTHING, primary_key=True)
    repay_type = models.ForeignKey('RepayType', models.DO_NOTHING, db_column='repay_type', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'repay_history'


class RepayType(models.Model):
    repay_type = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'repay_type'


class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=32)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'role'


class UserinfoBankCard(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    bankc_id = models.AutoField(primary_key=True)
    bankt = models.ForeignKey(BankcType, models.DO_NOTHING, blank=True, null=True)
    bankc_num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'userinfo_bank_card'


class UserinfoJob(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    job_id = models.AutoField(primary_key=True)
    company_name = models.TextField()
    plc = models.CharField(max_length=32)
    position = models.CharField(max_length=32)
    company_address = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userinfo_job'


class UserinfoMyIdcard(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    fujian_id = models.AutoField(primary_key=True)
    img1 = models.CharField(max_length=64, blank=True, null=True)
    img2 = models.CharField(max_length=64, blank=True, null=True)
    img3 = models.CharField(max_length=64, blank=True, null=True)
    img4 = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userinfo_my_IDcard'


class UserinfoSocialRel(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    social_id = models.AutoField(primary_key=True)
    rel_phone1 = models.CharField(max_length=10, blank=True, null=True)
    mail_tags = models.CharField(max_length=10, blank=True, null=True)
    lastest_one_month_tel = models.CharField(max_length=10, blank=True, null=True)
    lastest_three_tel = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userinfo_social_rel'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=32)
    password = models.CharField(max_length=256)
    true_name = models.CharField(max_length=32, blank=True, null=True)
    id_card = models.CharField(max_length=32, blank=True, null=True)
    avatar = models.FileField(upload_to='avatar', max_length=64, blank=True, null=True)
    true_avatar = models.FileField(upload_to='true_avatar', max_length=64, blank=True, null=True)
    nickname = models.CharField(max_length=32, blank=True, null=True)
    tel = models.IntegerField(blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=32, blank=True, null=True)
    more_address = models.CharField(max_length=32, blank=True, null=True)
    email = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
