# from django.shortcuts import render, redirect
# from django.core.files.storage import default_storage
# from django.http import JsonResponse, HttpResponse
# from django.conf import settings
# import boto3
# import tensorflow as tf
# from .models import diagnosis
# from PIL import Image
# import numpy as np
# import os

# # 모델 경로 설정 및 모델 로드
# model_path = os.path.join(settings.BASE_DIR, 'fashion_mnist_model.keras')
# model = tf.keras.models.load_model(model_path)

# def S3ImageDownloadView(request, image_key):
#     try:
#         image = diagnosis.objects.get(pk=image_key)
#         print(image)
#         # AWS 클라이언트 생성
#         s3_client = boto3.client(
#             's3',
#             aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
#             aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
#         )
#         image_name = image.image_name
#         print("------", image_name, type(image_name))
#         # S3 버킷에서 이미지 다운로드
#         response = s3_client.get_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=image_name)
#         print("------")
#         print(response)
#         image_data = response['Body'].read()
#         # 이미지를 로컬 파일 시스템에 저장
#         image_path = os.path.join(settings.MEDIA_ROOT, image_name)
#         print(image_path)
#         with open(image_path, 'wb') as f:
#             f.write(image_data)
        
#         # 예측 뷰로 리다이렉트
#         return redirect('diagnosis:predict')

#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)

# def index(request):
#     if request.method == 'POST':    
#         file = request.FILES['image']
#         filename = default_storage.save(file.name, file)
#         file_url = default_storage.url(filename)
#         diag = diagnosis.objects.create(image_name=filename, img_url=file_url)
#         return redirect('diagnosis:img_detail', pk=diag.pk)
#     return render(request, 'diagnosis/index.html')

# def img_detail(request, pk):
#     diagnosis_img = diagnosis.objects.get(pk=pk)
#     context = {
#         'diagnosis_img': diagnosis_img,
#         'diagnosis_img_pk': pk
#     }
#     return render(request, 'diagnosis/detail.html', context)



# def predict(request):
#     if request.method == 'POST':
#         try:
#             # 이미지 파일 파싱
#             image_file = request.FILES['image'].file

#             # 이미지를 로컬 파일 시스템에 저장
#             image_path = os.path.join(settings.MEDIA_ROOT, 'uploaded_image.jpg')  # 임시 파일명으로 저장
#             with open(image_path, 'wb') as f:
#                 for chunk in image_file.chunks():
#                     f.write(chunk)

#             # 저장된 이미지를 열어서 예측에 사용
#             image = Image.open(image_path).convert('L').resize((28, 28))
#             image_array = np.array(image) / 255.0
#             image_array = image_array.reshape(1, 28, 28)
            
#             # 예측 수행
#             predictions = model.predict(image_array)
#             predicted_label = np.argmax(predictions, axis=1)

#             # 결과 출력
#             print("Predicted Label:", int(predicted_label))

#             # JSON 응답 반환
#             return JsonResponse({'predicted_label': int(predicted_label)})
#         except Exception as e:
#             print("Error occurred during prediction:", e)
#             return JsonResponse({'error': 'An error occurred during prediction.'}, status=500)
    
#     elif request.method == 'GET':
#         # GET 요청을 처리하여 예측 페이지로 이동
#         return render(request, 'diagnosis/predict.html')
#     else:
#         return JsonResponse({'error': 'Method Not Allowed'}, status=405)

# ------------------------------------------------------------------

from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.core.files.storage import default_storage
from django.conf import settings
import boto3
import tensorflow as tf
from .models import diagnosis
from PIL import Image
import numpy as np
import os

# 모델 경로 설정 및 모델 로드
model_path = os.path.join(settings.BASE_DIR, 'fashion_mnist_model.keras')
model = tf.keras.models.load_model(model_path)

def S3ImageDownloadView(request, image_key):
    try:
        image = diagnosis.objects.get(pk=image_key)
        
        # AWS 클라이언트 생성
        s3_client = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
        )
        image_name = image.image_name
        # print("------", image_name, type(image_name))
        
        # S3 버킷에서 이미지 다운로드
        response = s3_client.get_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=image_name)
        
        # print(response)
        image_data = response['Body'].read()
        
        # 이미지를 로컬 파일 시스템에 저장
        image_path = os.path.join(settings.MEDIA_ROOT, image_name)
        # print(image_path)
        with open(image_path, 'wb') as f:
            f.write(image_data)
    
        
        image = diagnosis.objects.get(pk=image_key)
        # 예측 뷰로 리다이렉트 (이미지 키를 전달)
        return redirect('diagnosis:predict', image_key=image_key)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)



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


def predict(request, image_key=None):
    try:
        # 이미지 정보 로드
        image = diagnosis.objects.get(pk=image_key)
        image_path = os.path.join(settings.MEDIA_ROOT, image.image_name)

        # 저장된 이미지를 열어서 예측에 사용
        image = Image.open(image_path).convert('L').resize((28, 28))
        image_array = np.array(image) / 255.0
        image_array = image_array.reshape(1, 28, 28)
        
        # 예측 수행
        predictions = model.predict(image_array)
        predicted_label = np.argmax(predictions, axis=1)

        # 결과 출력 및 페이지로 반환
        context = {'predicted_label': int(predicted_label)}
        return render(request, 'diagnosis/predict.html', context)
    except Exception as e:
        print("Error occurred during prediction:", e)
        context = {'error': str(e)}
        return render(request, 'diagnosis/predict.html', context)
    
    # else:
    #     # GET 요청 처리 (기본 정보 표시)
    #     return render(request, 'diagnosis/predict.html')
