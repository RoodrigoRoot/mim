from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
import uuid
from django.utils.text import slugify
# Create your models here.

class Banks(models.Model):
    name = models.CharField(verbose_name="Bank", max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Bank"
        verbose_name_plural = "Banks"


class Countries(models.Model):
    COUNTRIES = (
        ("mx", "México"),
    )
    name = models.CharField(verbose_name="Country", max_length=50, choices=COUNTRIES)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"



class StatusUser(models.Model):
    status = models.BooleanField(verbose_name="Status User", default=False, blank=True, null=True)

    def __str__(self):
        return str(self.status)
    
    class Meta:
        verbose_name = "Status User"
        verbose_name_plural = "Status Users"


class Accounts(models.Model):
    user = models.OneToOneField(User, verbose_name="User", on_delete=models.CASCADE)
    bank = models.ForeignKey(Banks, verbose_name="Bank", on_delete=models.CASCADE, blank=True, null=True)
    birthday = models.DateField(verbose_name="Datebirth", auto_now=False, auto_now_add=False)
    create_at = models.DateTimeField(verbose_name="Created", auto_now=True, auto_now_add=False)
    phone = models.CharField(verbose_name="Phone", max_length=15)
    country = models.ForeignKey(Countries, verbose_name="Country", on_delete=models.CASCADE)
    clabe = models.CharField(verbose_name="Clabe", max_length=50)
    slug = models.SlugField(verbose_name="Slug")
    status = models.ForeignKey(StatusUser, verbose_name="Status User", on_delete=models.CASCADE)
    #address = models.ForeignKey(, verbose_name=_(""), on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"

def create_slug_profile(sender, instance, **kwargs):
    slug = "{}-{}".format(instance.user.username,str(uuid.uuid4())[:4])
    instance.slug = slug
    print(instance.slug)

pre_save.connect(create_slug_profile, sender=Accounts)

class Codes(models.Model):
    user = models.OneToOneField(Accounts, verbose_name="Account", on_delete=models.CASCADE)
    code = models.CharField(verbose_name="Code", max_length=10, blank=True, null=True)


    def __str__(self):
        return str(self.code).upper()

    class Meta:
        verbose_name = "Code"
        verbose_name_plural = "Codes"


def create_code_accoumt(sender, instance, **kwargs):
    code = str(uuid.uuid4())[:6]
    Codes.objects.create(
        user=instance,
        code=code
    )
post_save.connect(create_code_accoumt, sender=Accounts)


class Benefits(models.Model):
    user = models.OneToOneField(Accounts, verbose_name="User", on_delete=models.CASCADE)
    fullname = models.CharField(verbose_name="Full Name", max_length=200)
    created_at = models.DateTimeField(verbose_name="Created", auto_now=True, auto_now_add=False)
    updated_at = models.DateTimeField(verbose_name="Updated", auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = "Benefit"
        verbose_name_plural = "Benefits"

