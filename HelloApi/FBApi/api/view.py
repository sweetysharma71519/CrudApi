from rest_framework.response import Response
from rest_framework.serializers import *
from ..models import StuRecord
from .serializer import StudentRecordSerializer
from rest_framework.status import *
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view

# @api_view(['GET','POST'])
# def stu_add(request):
#     if request.method=='GET':
#         orm = StuRecord.objects.all()
#         serial = StudentRecordSerializer(orm, many=True).data
#         return Response({"msg": "All records are show below!!!!!", "data": serial}, status=HTTP_200_OK)
#     else:
#         mdata = request.data
#         #alldata = mdata.get('stu_Fnm', None)
#         ##data.append(alldata)
#         serializer = StudentRecordSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=HTTP_201_CREATED)
#         return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)







@api_view(['GET',])
def stu_view(request,):
    if request.method=='GET':
        orm = StuRecord.objects.all()
        serial = StudentRecordSerializer(orm, many=True).data
        return Response({"msg": "All records are show below!!!!!", "data": serial}, status=HTTP_200_OK)
    else:
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['GET',])
def stu_view_id(request,id):
    qs=StuRecord.objects.get(id=id)
    if request.method=='GET':
        try:
            serializer = StudentRecordSerializer(qs)
            return Response(serializer.data)
        except StuRecord.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)


@api_view(['POST',])
def stu_add(request):
    if request.method=='POST':
        mdata = request.data
        serializer = StudentRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        return Response({"msg": "Enter records in Json formate!!!!!", "data": serial}, status=HTTP_200_OK)
    

@api_view(['PUT','GET',])
def stu_update(request,id):
    qs=StuRecord.objects.get(id=id)
    if request.method=='GET':
        try:
            serializer = StudentRecordSerializer(qs)
            return Response(serializer.data)
        except StuRecord.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)
    if request.method=='PUT':
        #mdata = request.data
        serializer = StudentRecordSerializer(qs,data=request.data)
        data={}
        if serializer.is_valid():
            serializer.save()
            data["update"]="Update successful"
            return Response(data=data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@api_view(['DELETE','GET',])
def stu_delete(request,id):
    qs=StuRecord.objects.get(id=id)
    if request.method=='GET':
        try:
            serializer = StudentRecordSerializer(qs)
            return Response(serializer.data)
        except StuRecord.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)
    if request.method=='DELETE':
        del_opt = qs.delete()
        data={}
        data["update"]="Delete successful"
        return Response(data=data)
    else:
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['PATCH','GET',])
def stu_update_patch(request,id):
    qs=StuRecord.objects.get(id=id)
    if request.method=='GET':
        try:
            serializer = StudentRecordSerializer(qs)
            return Response(serializer.data)
        except StuRecord.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)
    if request.method=='PATCH':
        #mdata = request.data
        serializer = StudentRecordSerializer(qs,data=request.data)
        data={}
        if serializer.is_valid():
            serializer.save()
            data["update"]="Update successful"
            return Response(data=data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)





