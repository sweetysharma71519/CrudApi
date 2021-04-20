from rest_framework.serializers import *
from ..models import StuRecord
class StudentRecordSerializer(ModelSerializer):
    class Meta:
        model=StuRecord
        fields="__all__"