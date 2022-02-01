from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from .models import *
from .serializers import *






class CountryCreateView(generics.CreateAPIView):
    serializer_class = CountrySerializer
    """Добавление Страны"""
    """
        def post(self, request):
        country = CountryCreateSerializer(data=request.data)
        if country.is_valid():
            country.save()
        return Response(country.data)
    """





class CountryListView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    """
        def get(self,request):
        countries = Country.objects.all()
        serializer = CountryListSerializer(countries, many = True)
        return  Response(serializer.data)
    """


class CountryDetailView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = CountrySerializer
    queryset =  Country.objects.all()
    """
        def get(self,request,pk):
        country = Country.objects.get(id = pk)
        serializer = CountryDetailSerializer(country)
        return  Response(serializer.data)
    """


class PlantCreateView(generics.CreateAPIView):
    """Добавление Растения"""
    serializer_class = PlantCreateSerializer

    """def post(self, request):
        plant = PlantCreateSerializer(data=request.data)
        if plant.is_valid():
            plant.save()
        return Response(plant.data)"""

class PlantListView(generics.ListAPIView):
    serializer_class = PlantListSerializer
    queryset = Plant.objects.all()
    """
     def get(self,request):
        plants = Plant.objects.all()
        serializer = PlantListSerializer(plants, many = True)
        return  Response(serializer.data)
    """



class PlantDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PlantDetailSerializer
    queryset = Plant.objects.all()
    """
        def get(self,request,pk):
            plant = Plant.objects.get(id = pk)
            serializer = PlantDetailSerializer(plant)
            return  Response(serializer.data)
    """


class PlantationCreateView(generics.CreateAPIView):
    """Добавление Растения"""
    serializer_class = PlantationCreateSerializer

class PlantationListView(generics.ListAPIView):
    queryset = Plantation.objects.all()
    serializer_class = PlantationListSerializer

    """
     def get(self,request):
        plantations = Plantation.objects.all()
        serializer = PlantationListSerializer(plantations, many = True)
        return  Response(serializer.data)
    """


class PlantationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plantation.objects.all()
    serializer_class = PlantationDetailSerializer
    """
            def get(self,request,pk):
                plantation = Plantation.objects.get(id = pk)
                serializer = PlantationDetailSerializer(plantation)
                return  Response(serializer.data)


        def patch(self, request, pk=None):
            plantation = Plantation.objects.get(id=pk)
            serializer = PlantationDetailSerializer(plantation, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({ serializer.data})
            else:
                return Response({ serializer.errors})
    """






