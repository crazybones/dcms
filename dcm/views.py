from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from dcm import ContainerSerializer
from dcm import ContainerServices


class ContainerList(APIView):
    def get(self, request, format=None):
        data = ContainerServices.prepare_containers_info()
        result = ContainerSerializer(data, many=True).data
        return Response(result)

# nice but we don't need post yet
# class ContainerList(generics.ListCreateAPIView):
#     cs = ContainerServices()
#     queryset = cs.get_test_data()
#     serializer_class = ContainerSerializer
