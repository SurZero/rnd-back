from rest_framework import serializers

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


class PatientFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientRegistrationForm
        fields = '__all__'


class DefaultPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefaultPositions
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Positions
        fields = '__all__'


class NamePositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NamePositions
        fields = '__all__'


class HousePositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousePositions
        fields = '__all__'


class StreetPositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreetPositions
        fields = '__all__'


class PostcodePositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostcodePositions
        fields = '__all__'


class CountryPositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryPositons
        fields = '__all__'


class AddressPositionsSerializer(serializers.ModelSerializer):
    house_no = HousePositionsSerializer()
    street_no = StreetPositionsSerializer()
    postcode = PostcodePositionsSerializer()
    country = CountryPositionsSerializer()

    class Meta:
        model = AddressPositions
        fields = '__all__'


class DobPositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DobPositions
        fields = '__all__'


class FormFieldPositionsSerializer(serializers.ModelSerializer):
    name = NamePositionsSerializer()
    address = AddressPositionsSerializer()
    dob = DobPositionsSerializer()

    class Meta:
        model = FormFieldPositions
        fields = ['form_name', 'name', 'address', 'dob']
