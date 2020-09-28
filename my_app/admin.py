from django.contrib import admin
from .models import (PatientRegistrationForm,
                     Positions,
                     DefaultPositions,
                     AddressPositions,
                     FormFieldPositions,
                     NamePositions,
                     DobPositions,
                     HousePositions,
                     StreetPositions,
                     PostcodePositions,
                     CountryPositons)


class PatientFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'house_no', 'street_no', 'postcode', 'country']
    search_fields = ['name']


admin.site.register(PatientRegistrationForm, PatientFormAdmin)
admin.site.register(Positions)


# class PositionsAdmin(admin.ModelAdmin):
#     list_display = ['field_id', 'field_name',
#                     'x_offset', 'y_offset', 'height', 'width']


class DefaultPositionsAdmin(admin.ModelAdmin):
    list_display = ['form_name', 'field_name',
                    'x_offset', 'y_offset', 'width', 'height']
    # search_fields = ["form_name", "field_name"]
    list_filter = ["form_name", "field_name"]


admin.site.register(DefaultPositions, DefaultPositionsAdmin)


class FormFieldAdmin(admin.ModelAdmin):
    list_display = ["form_name", "name", "address", "dob"]


admin.site.register(FormFieldPositions, FormFieldAdmin)
admin.site.register(AddressPositions)
admin.site.register(NamePositions)
admin.site.register(DobPositions)
admin.site.register(HousePositions)
admin.site.register(StreetPositions)
admin.site.register(PostcodePositions)
admin.site.register(CountryPositons)
