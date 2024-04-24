from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.conf import settings
from .models import diagnosis
from rest_framework.response import Response
from rest_framework import status
import os
import boto3
import tensorflow as tf
import numpy as np



def S3ImageDownloadView(request, image_key):
    try:
        image = diagnosis.objects.get(pk=image_key)
        print(image)
        # AWS 클라이언트 생성
        s3_client = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
        )
        image_name = image.image_name
        print("------", image_name, type(image_name))
        # S3 버킷에서 이미지 다운로드
        response = s3_client.get_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=image_name)
        print("------")
        print(response)
        image_data = response['Body'].read()
        # 이미지를 로컬 파일 시스템에 저장
        image_path = os.path.join(settings.MEDIA_ROOT, image_name)
        print(image_path)
        
        with open(image_path, 'wb') as f:
            f.write(image_data)
        render(request, 'diagnosis/index.html')
    
    
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return render(request, 'diagnosis/index.html')


def index(request):
    if request.method == 'POST':
        file = request.FILES['image']
        filename = default_storage.save(file.name, file)
        file_url = default_storage.url(filename)
        print(filename, file_url)
        diag = diagnosis.objects.create(image_name=filename, img_url=file_url)
        return redirect('diagnosis:img_detail', pk=diag.pk)
    return render(request, 'diagnosis/index.html')


def img_detail(request, pk):
    diagnosis_img = diagnosis.objects.get(pk=pk)
    context = {
        'diagnosis_img': diagnosis_img,
        'diagnosis_img_pk': pk
    }
    return render(request, 'diagnosis/detail.html', context)