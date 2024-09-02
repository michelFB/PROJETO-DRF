from rest_framework import serializers
from toys.models import Toy

#ToySerializer herda da superclasse rest_framework.serializers.ModelSerializer
class ToySerializer(serializers.ModelSerializer):
    class Meta:
        model = Toy
        fields = (
            "id",
            "name",
            "description",
            "release_date",
            "toy_category",
            "was_included_in_home",
        )
