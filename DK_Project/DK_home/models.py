# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
import datetime
from django.db import models


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class EmpTable(models.Model):
    role = models.ForeignKey('RoleTable', models.DO_NOTHING, blank=True, null=True)
    emp_id = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emp_table'


class LoantypeTable(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_name = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loantype_table'


class PaymentTable(models.Model):
    payment_id = models.AutoField(primary_key=True)
    pay_type = models.CharField(max_length=256, blank=True, null=True)
    pay_money = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_table'


class PerRoleTable(models.Model):
    per = models.ForeignKey('PerTable', models.DO_NOTHING, primary_key=True)
    role = models.ForeignKey('RoleTable', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'per_role_table'
        unique_together = (('per', 'role'),)


class PerTable(models.Model):
    per_id = models.AutoField(primary_key=True)
    per_name = models.CharField(max_length=256)
    class Meta:
        managed = False
        db_table = 'per_table'


class RoleTable(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=128, blank=True, null=True)
    pers = models.ManyToManyField(PerTable,through='PerRoleTable')
    class Meta:
        managed = False
        db_table = 'role_table'


class StatuTable(models.Model):
    statu_id = models.AutoField(primary_key=True)
    statu_name = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statu_table'


class UserTable(models.Model):
    user_id = models.AutoField(primary_key=True)
    payment = models.ForeignKey(PaymentTable, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=256)
    loa_loan = models.ForeignKey(LoantypeTable, models.DO_NOTHING, blank=True, null=True)
    statu = models.ForeignKey(StatuTable, models.DO_NOTHING, blank=True, null=True)
    user_card = models.CharField(max_length=256, blank=True, null=True)
    loan_id = models.CharField(max_length=256, blank=True, null=True)
    user_phone = models.CharField(max_length=256, blank=True, null=True)
    principal = models.CharField(max_length=256, blank=True, null=True)  # 逾期金额
    pri_date = models.DateField(blank=True, null=True) # 贷款日期
    emp = models.ForeignKey(EmpTable, models.DO_NOTHING, blank=True, null=True)
    wallet = models.CharField(max_length=256, blank=True, null=True)
    operating_time = models.DateField(auto_now=True)

    def to_dict(self):
        return {
            'user_id' : self.user_id,
            'loan_id' : self.loan_id,
            'name' : self.name,
            'phone' : self.user_phone,
            'card' : self.user_card,
            'date' : self.pri_date.strftime('%Y-%m-%d'),
            'deal_peo' : self.emp.emp_name,
            'status' : self.statu.statu_name,
            'deal_time' : datetime.datetime.now().strftime('%Y-%m-%d')
        }

    class Meta:
        managed = False
        db_table = 'user_table'


class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_image = models.TextField(blank=True, null=True)
    product_name = models.TextField(blank=True, null=True)
    product_months = models.CharField(max_length=5, blank=True, null=True)
    month_pay = models.CharField(max_length=20, blank=True, null=True)
    surplus_pay = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'

    def to_dict(self):
        return {
            'product_image': self.product_image,
            'product_name': self.product_name,
            'product_months': self.product_months,
            'month_pay': self.month_pay,
            'surplus_pay': self.surplus_pay
        }
