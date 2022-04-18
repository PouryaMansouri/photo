from django.core.validators import RegexValidator
from django.db import models

from core.models import SingletonBaseModel
from django.utils.translation import gettext_lazy as _


class SiteSetting(SingletonBaseModel):
    class Meta:
        verbose_name = _('تنظیمات سایت')
        verbose_name_plural = _('تنظیمات سایت')

    site_name = models.CharField(
        max_length=150,
        verbose_name=_('نام سایت'),
    )

    phone = models.CharField(
        max_length=11,
        null=True,
        blank=True,
        verbose_name=_('تلفن ثایت ارتباطی'),
        help_text=_('این شماره تلفن ثابت شماست. لطفا آن را با پیش شماره شهر خود وارد نمایید.'),
        validators=[RegexValidator(
            regex='^0\d{2,3}\d{8}$',
            message=_('شماره تلفن ثابت معتبر نیست!')
        )]
    )

    mobile_phone = models.CharField(
        max_length=14,
        null=True,
        blank=True,
        verbose_name=_('تلفن همراه ارتباطی'),
        validators=[RegexValidator(
            regex='^(0)?9\d{9}$',
            message=_('شماره موبایل معتبر نیست!')
        )]
    )

    email = models.EmailField(
        verbose_name=_('آدرس ایمیل ارتباطی'),
        null=True,
        blank=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('توضیحات سایت'),
        help_text=_('این توضیحات در بخش پاورقی وبسایت نمایش داده خواهند شد.'),
    )

    def __str__(self):
        return self.site_name
