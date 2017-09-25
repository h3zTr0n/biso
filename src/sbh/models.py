from django.db import models

from django.utils.translation import ugettext_lazy as _

class Facility(models.Model):
    name = models.CharField(_("Facility Name"), max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name = "FACILITY"
        verbose_name_plural = "FACILITIES"

    def __unicode__(self):
        return self.name

class Hcc(models.Model):
    representative = models.CharField(_("Member Name"), max_length=255, null=True, blank=True)
    position = models.CharField(_("Position"), max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name = "HCC"
        verbose_name_plural = "HCCs"

    def __unicode__(self):
        return self.representative


class Nhcs(models.Model):
    representative = models.CharField(_("Member Name"), max_length=255, null=True, blank=True)
    position = models.CharField(_("Position"), max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name = "NHCS"
        verbose_name_plural = "NHCSs"

    def __unicode__(self):
        return self.representative
