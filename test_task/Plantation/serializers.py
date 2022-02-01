from rest_framework import serializers
from .models import *

"""


"""





class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields  = "__all__"


class PlantCreateSerializer(serializers.ModelSerializer):
    """Plant creation"""

    class Meta:
        model = Plant
        fields = "__all__"


class PlantListSerializer(serializers.ModelSerializer):
    """ Plant List"""

    class Meta:
        model = Plant
        fields  = ("name","description")


class PlantDetailSerializer(serializers.ModelSerializer):
    """ Plant detail card"""

    class Meta:
        model = Plant
        fields  = "__all__"


class PlantationCreateSerializer(serializers.ModelSerializer):
    """Plantation creation"""
    class Meta:
        model = Plantation
        fields = "__all__"

class PlantationListSerializer(serializers.ModelSerializer):
    """ Plantation List"""
    country = serializers.SlugRelatedField(slug_field="name", read_only=True)
    class Meta:
        model = Plant
        fields  = ("name","country")

class PlantationDetailSerializer(serializers.ModelSerializer):
    """Plantation detail card """
    plants = serializers.SlugRelatedField(slug_field="name", read_only=True,many=True)
    country = serializers.SlugRelatedField(slug_field="name", read_only=True)
    class Meta:
        model = Plantation
        fields = "__all__"