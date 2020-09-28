from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView
from rest_framework.response import Response

from .models import PatientRegistrationForm, Positions, DefaultPositions, FormFieldPositions
from .serializers import PatientFormSerializer, PositionSerializer, DefaultPositionSerializer, FormFieldPositionsSerializer

import json


class PatientFormCreateApiView(CreateAPIView):
    queryset = PatientRegistrationForm.objects.all()
    serializer_class = PatientFormSerializer

    def get(self, request, *args, **kwargs):
        data = ''
        positions = Positions.objects.filter(
            form_name="Patient Registration Form")
        if positions:
            serializer = PositionSerializer(positions, many=True)
            # if serializer.is_valid():
            # print(serializer.data)
            data = serializer.data

        else:
            positions = DefaultPositions.objects.filter(
                form_name="Patient Registration Form")
            serializer = DefaultPositionSerializer(positions, many=True)
            # serializer.is_valid(raise_exception=True)
            # print(serializer.data)
            data = serializer.data
        return Response(data=data)


class UpdatePsitionsAPIView(UpdateAPIView):
    # queryset = DefaultPositions.objects.all()
    serializer_class = DefaultPositionSerializer
    # lookup_field = "pk"

    def patch(self, request, *args, **kwargs):
        data = json.loads(request.body)
        # q = self.queryset.filter(form_name=data[0]["form_name"])
        form_name = data[0]["form_name"]
        for field in data:
            try:
                DefaultPositions.objects.filter(
                    form_name=form_name, id=field["id"]).update(**field)
            except:
                return Response(data={"data": "Error"})

        return Response(data={"data": "Okayy"})


class PatientFormCreateApiView(ListAPIView):
    queryset = FormFieldPositions.objects.all()
    serializer_class = FormFieldPositionsSerializer

    # def get(self, request, *args, **kwargs):
    #     data = ''
    #     positions = Positions.objects.filter(
    #         form_name="Patient Registration Form")
    #     if positions:
    #         serializer = PositionSerializer(positions, many=True)
    #         # if serializer.is_valid():
    #         # print(serializer.data)
    #         data = serializer.data
