from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import DogForm 
from .models import Dog  
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser
from django.core.files.storage import default_storage
from django.utils.datastructures import MultiValueDictKeyError


# # Create your views here.
# def index(request):
#     return render(request, 'mypage/index.html')


# # 강아지 정보 입력 폼 페이지를 보여주는 뷰
# @login_required
# def add_dog(request):

#     if request.method == 'POST':
#         form = DogForm(request.POST, request.FILES)
#         if form.is_valid():
#             # 폼의 데이터가 유효하면, 모델 인스턴스를 생성하고 저장
#             new_dog = form.save(commit=False)
#             new_dog.owner = request.user  # 강아지 모델에 소유자 필드가 있다고 가정
#             new_dog.save()
#             return redirect('some_view_to_redirect')  # 성공 시 리다이렉트할 뷰 이름
#     else:
#           # GET 요청시 빈 폼을 생성
#         return render(request, 'mypage/add_dog_info.html')



from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.contrib.auth.decorators import login_required
from .models import Dog

@login_required
def add_dog(request):
    dog = None  # GET 요청일 때 dog 변수를 초기화

    if request.method == 'POST':
        name = request.POST.get('name')
        breed = request.POST.get('breed')
        age = request.POST.get('age')
        img_url = None  # 이미지 URL 초기화

        # 이미지 파일 확인
        file = request.FILES.get('image')  # .get()을 사용하여 파일 존재 여부 확인
        if file:
            filename = default_storage.save(file.name, file)
            file_url = default_storage.url(filename)
            print(filename, file_url)
            img_url = file_url

        # 강아지 정보를 데이터베이스에 저장
        dog = Dog.objects.create(
            owner=request.user,
            name=name,
            breed=breed,
            age=age,
            img_url=img_url  # 이미지가 없으면 None으로 저장
        )
            
        # 수정 후 리다이렉트할 URL을 지정해주세요.
        return redirect('mypage:mypage_view', username=request.user.username)
    
    # 폼을 렌더링할 때 기존의 개 정보를 전달
    return render(request, 'mypage/add_dog_info.html', {'dog': dog})











# @login_required
# def dog_info_submit(request):

#     if request.method == 'POST':
#         form = DogForm(request.POST)
#         if form.is_valid():
#             dog = form.save(commit=False)
#             dog.owner = request.user  # 현재 로그인한 사용자를 owner로 설정
#             dog.save()
#             # 사용자의 마이페이지로 리디렉션
#             return redirect('mypage:mypage_view', username=request.user.username)
#         else:
#             # 폼 유효성 검사에 실패했을 경우 처리
#             return render(request, 'mypage/dog_form.html', {'form': form})
#     else:
#         form = DogForm()
#         return render(request, 'mypage/dog_form.html', {'form': form})




@login_required
def mypage_view(request, username):  # username 매개변수 추가

    # 마이페이지에 접근하는 사람이 본인의 계정이 아닌 경우에 메인페이지로 이동
    if request.user.username != username:
        return render(request, 'accounts/login.html')
    user = get_object_or_404(CustomUser, username=username)  # get_object_or_404를 사용하여 사용자를 가져옴
    # 강아지 객체를 못찾으면 404 페이지로 리다이렉트 시키는 코드 
    # 내 프로필 페이지에 왔는데, 이 친구가 강아지를 안키운다? 그러면 404가 열리는거에요
    # 강아지가 없어도 프로필은 열려야하기 때문에 아래 코드는 사용할 수 없음 
    # dogs = get_object_or_404(Dog, owner=request.user)

    dogs = Dog.objects.filter(owner_id=request.user.id)
    return render(request, 'mypage/index.html', {'user': user, 'dogs': dogs})






# @login_required
# def dog_edit(request, pk):
#     dog = get_object_or_404(Dog, pk=pk)
    
#     if request.method == 'POST':
#         form = DogForm(request.POST, instance=dog)
#         if form.is_valid():
#             form.save()
#             return redirect('mypage:mypage_view', username=request.user.username)
#     else:
#         form = DogForm(instance=dog)
    
#     return render(request, 'mypage/dog_edit.html', {'form': form, 'dog': dog})



@login_required
def dog_edit(request, pk):
    dog = get_object_or_404(Dog, pk=pk, owner=request.user)
    
    if request.method == 'POST':
        owner = request.POST.get('owner')
        name = request.POST.get('name')
        breed = request.POST.get('breed')
        age = request.POST.get('age')

        try:
            file = request.FILES['image']
            filename = default_storage.save(file.name, file)
            file_url = default_storage.url(filename)
            print(filename, file_url)

            img_url = file_url
        except MultiValueDictKeyError:
            img_url = dog.img_url  # 기존 이미지 URL 사용

        dog.name = name
        dog.breed = breed
        dog.age = age
        dog.img_url = img_url
        dog.save()
        
        return redirect('mypage:mypage_view', username=request.user.username)
    
    context = {
        'dog': dog,
    }
    
    return render(request, 'mypage/dog_edit.html', context)




# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from .models import Dog


# @login_required
# def dog_edit(request, pk):
#     dog = get_object_or_404(Dog, pk=pk, owner=request.user)
    
#     if request.method == 'POST':
#         owner = request.POST.get('owner')
#         name = request.POST.get('name')
#         breed = request.POST.get('breed')
#         age = request.POST.get('age')

#         file = request.FILES['image']
#         filename = default_storage.save(file.name, file)
#         file_url = default_storage.url(filename)
#         print(filename, file_url)

#         img_url = file_url
        

#         dog.name = name
#         dog.breed = breed
#         dog.age = age
#         dog.img_url = img_url
#         dog.save()
        
#         return redirect('mypage:mypage_view', username=request.user.username)  # 수정 후 리다이렉트할 URL을 지정해주세요.
    
#     context = {
#         'dog': dog,
#     }
    
#     return render(request, 'mypage/dog_edit.html', context)







@login_required
def dog_delete(request, pk):
    dog = get_object_or_404(Dog, pk=pk)
    if request.method == 'POST':
        dog.delete()
        return redirect('mypage:mypage_view', username=request.user.username)
    return render(request, 'mypage/dog_delete_confirm.html', {'dog': dog})



# @login_required
# def add_dog(request):
#     if request.method == 'POST':
#         form = DogForm(request.POST)
#         if form.is_valid():
#             dog = form.save(commit=False)
#             dog.owner = request.user
#             dog.save()
#             return redirect('mypage:mypage_view', username=request.user.username)
#     else:
#         form = DogForm()
#     return render(request, 'mypage/add_dog.html', {'form': form})    


# @login_required
# def dog_info(request):
#     # 현재 로그인한 사용자의 강아지 정보를 조회
#     dog = Dog.objects.filter(owner_id=user_id).first()

#     return render(request, 'mypage/index.html', {'dog': dog})



