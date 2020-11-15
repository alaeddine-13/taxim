from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .serializers import LogInSerializer, UserSerializer, ProfileSerializer
from .models import Upload, UploadPrivate




class SignUpView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class LogInView(TokenObtainPairView):
    serializer_class = LogInSerializer

class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return get_user_model().objects.filter(username=self.request.user.username)
    
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset)
        return obj
    

def image_upload(request):
    if request.method == 'POST':
        image_file = request.FILES['image_file']
        image_type = request.POST['image_type']
        if settings.USE_S3:
            if image_type == 'private':
                upload = UploadPrivate(file=image_file)
            else:
                upload = Upload(file=image_file)
            upload.save()
            image_url = upload.file.url
        else:
            fs = FileSystemStorage()
            filename = fs.save(image_file.name, image_file)
            image_url = fs.url(filename)
        return render(request, 'upload.html', {
            'image_url': image_url
        })
    return render(request, 'upload.html')
