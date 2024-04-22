from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mypage/index.html')



from django.shortcuts import render, redirect
from .forms import DogForm 
from .models import Dog  

# 강아지 정보 입력 폼 페이지를 보여주는 뷰
def add_dog(request):
    if request.method == 'POST':
        form = DogForm(request.POST)
        if form.is_valid():
            # 폼의 데이터가 유효하면, 모델 인스턴스를 생성하고 저장
            new_dog = form.save(commit=False)
            new_dog.owner = request.user  # 강아지 모델에 소유자 필드가 있다고 가정
            new_dog.save()
            return redirect('some_view_to_redirect')  # 성공 시 리다이렉트할 뷰 이름
    else:
        form = DogForm()  # GET 요청시 빈 폼을 생성
    return render(request, 'mypage/add_dog_info.html', {'form': form})

# views.py

from django.shortcuts import render
from .forms import DogForm  # 폼이 정의된 곳으로부터 DogForm을 임포트

def dog_info_submit(request):
    if request.method == 'POST':
        form = DogForm(request.POST)
        if form.is_valid():
            form.save()
            # 성공적으로 저장 후 리다이렉션
            return redirect('some_success_url')
    else:
        form = DogForm()

    # DogForm 인스턴스를 컨텍스트에 추가
    return render(request, 'mypage/add_dog_info.html', {'form': form})

