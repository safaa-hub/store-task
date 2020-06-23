from django.core.files.storage import default_storage
from ..common_file import Session
from ..models.image import Image
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets


class UploadImage(viewsets.ViewSet):

    def create(self, request):
        if request.data:
            filename = "lipstick.jpg"
            file_obj = request.data['image']

            with default_storage.open('C:\\Users\\hmds-\\PycharmProjects\\storetask\\myproject\\' + filename, 'wb+') as destination:
                for chunk in file_obj.chunks():
                    destination.write(chunk)

            #  my_image = Image(path='C:\\Users\\hmds-\\PycharmProjects\\storetask\\myproject\\' + filename, product_id=16, id=1) Session.add(my_image)
            #  Session.commit()
            return Response('image added successfully', status=status.HTTP_200_OK)
        else:
            return Response('No content', status=status.HTTP_204_NO_CONTENT)
