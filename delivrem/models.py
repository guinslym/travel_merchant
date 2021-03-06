# -*- coding: utf-8 -*-
from datetime import timedelta
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinLengthValidator, RegexValidator
from django.conf import settings
from model_utils.models import TimeStampedModel
import datetime
from django.utils import timezone
from django.forms.models import model_to_dict
from django.core.validators import MaxValueValidator

from updown.fields import RatingField
# Create your models here.
'''
 ☐ User
   ☐ **Product (Image)
     ☐ **Comment#
     ☐ **Like
     ☐ **Repost
 ☐ **Follow
'''


class Product(TimeStampedModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    photo = models.ImageField(upload_to='delivrem/%Y/%m/%d',
                            help_text='Show us wadiyabi',
                            null=False, blank=False, verbose_name="pics")
    showoff = models.CharField(max_length=440, null=False, blank=False, verbose_name='shoutout')
    slug = models.CharField(max_length=220, null=True, blank=True)
    price = models.DecimalField(max_digits=16, decimal_places=2, default=0, null=True, blank=True)
    activated = models.BooleanField(default=False)
    quantity = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100),])
    #did this product have been sale
    sale = models.BooleanField(default=False)
    rating = RatingField(can_change_vote=True)

    def __str__(self):
        return str(self.id)
    def get_absolute_url(self):
        return reverse('delivrem:product-detail', args=(self.id,))
    class Meta:
        ordering = ["-created"]
    '''
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk':self.id})
    '''

class Zin(TimeStampedModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    comment = models.CharField(max_length=220, null=False, blank=False)
