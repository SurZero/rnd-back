from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator


class PatientRegistrationForm(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    country = models.CharField(_("Country"), max_length=50)
    postcode = models.CharField(_("Postcode"), max_length=50)
    street_no = models.CharField(_("Street Number"), max_length=50)
    house_no = models.CharField(_("House Number"), max_length=50)
    dob = models.DateField(_("Date of Birth"))

    class Meta:
        verbose_name_plural = _("Patient Registration Form")

    def __str__(self):
        return self.name


class Positions(models.Model):
    form_name = models.CharField(_("Form Name"), max_length=100)
    field_name = models.CharField(max_length=50)
    x_offset = models.IntegerField()
    y_offset = models.IntegerField()
    height = models.CharField(max_length=255)
    width = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = _("Positions")

    def __str__(self):
        return f"{self.form_name} --> {self.field_name}"


class DefaultPositions(models.Model):
    form_name = models.CharField(_("Form Name"), max_length=100)
    field_name = models.CharField(max_length=50)
    x_offset = models.IntegerField()
    y_offset = models.IntegerField()
    height = models.CharField(max_length=255)
    width = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = _("Default Positions")

    def __str__(self):
        return f"{self.form_name} --> {self.field_name}"


class FieldPositions(models.Model):
    x_offset = models.IntegerField(_("X Offset"))
    y_offset = models.IntegerField(_("Y Offset"))
    width = models.CharField(_("Width"), max_length=30)
    height = models.CharField(_("Height"), max_length=30)

    class Meta:
        abstract = True


class NamePositions(FieldPositions):
    pass


class DobPositions(FieldPositions):
    pass


class HousePositions(FieldPositions):
    pass


class StreetPositions(FieldPositions):
    pass


class PostcodePositions(FieldPositions):
    pass


class CountryPositons(FieldPositions):
    pass


class AddressPositions(models.Model):
    house_no = models.ForeignKey(
        "HousePositions", related_name="house_positions", on_delete=models.CASCADE)
    street_no = models.ForeignKey(
        "StreetPositions", related_name="street_posirions", on_delete=models.CASCADE)
    postcode = models.ForeignKey(
        "PostcodePositions", related_name="postcode_positions", on_delete=models.CASCADE)
    country = models.ForeignKey(
        "CountryPositons", related_name="country_positions", on_delete=models.CASCADE)


class FormFieldPositions(models.Model):
    form_name = models.CharField(_("Form Name"), max_length=200)
    name = models.ForeignKey(
        "NamePositions", related_name="name_positions", on_delete=models.CASCADE)
    address = models.ForeignKey(
        "AddressPositions", related_name="dob_positions", on_delete=models.CASCADE)
    dob = models.ForeignKey(
        "DobPositions", related_name="address_positions", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = _("Form Field Posiotions")

    def __str__(self):
        return self.form_name
