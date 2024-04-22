from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm



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

from django.shortcuts import redirect

def dog_info_submit(request):
    if request.method == 'POST':
        form = DogForm(request.POST)
        if form.is_valid():
            dog = form.save(commit=False)
            dog.owner = request.user  # 현재 로그인한 사용자를 owner로 설정
            dog.save()
            # 사용자의 마이페이지로 리디렉션
            return redirect('mypage:mypage_view', username=request.user.username)
        else:
            # 폼 유효성 검사에 실패했을 경우 처리
            return render(request, 'mypage/dog_form.html', {'form': form})
    else:
        form = DogForm()
        return render(request, 'mypage/dog_form.html', {'form': form})


from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser

@login_required
def mypage_view(request, username):  # username 매개변수 추가
    user = get_object_or_404(CustomUser, username=username)  # get_object_or_404를 사용하여 사용자를 가져옴
    return render(request, 'mypage/index.html', {'user': user})

from .models import Dog
def dog_info(reuest):
    dog = get_object_or_404(CustomUser, username=username)  # get_object_or_404를 사용하여 사용자를 가져옴
    return render(request, 'mypage/index.html', {'dog': dog})