from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

from core.manager import MyUserManager


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_('زمان ساخت'),
    )

    last_updated = models.DateTimeField(
        auto_now=True,
        editable=False,
        verbose_name=_('زمان بروزرسانی'),
    )


class User(AbstractUser):
    objects = MyUserManager()

    phone = models.CharField(
        max_length=14,
        verbose_name=_('تلفن همراه'),
        unique=True,
        validators=[RegexValidator(
            regex='^(0)?9\d{9}$',
            message=_('شماره موبایل معتبر نیست!')
        )]
    )

    USERNAME_FIELD = 'phone'

    def save(self, *args, **kwargs):
        self.username = self.phone
        super().save(*args, **kwargs)


class SingletonBaseModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
