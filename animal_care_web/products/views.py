from django.shortcuts import render, redirect
from .models import Products, Categories
from django.core.files.storage import default_storage


def index(request):
    # products = Products.objects.all()  # 모든 상품을 쿼리합니다.
    products = Products.objects.exclude(name='광고')
    ad = Products.objects.filter(name = '광고')
    user = request.user
    context = {
        'products': products,
        'ads' : ad,
        'user' : user
        
    }   # 쿼리한 상품을 컨텍스트에 담습니다.
    return render(request, 'products/index.html', context)


def store(request):
    
    return render(request, 'products/store.html')


def product_detail(request, pk):
    product = Products.objects.get(pk=pk)
    context = {
        'product' : product
    }
    return render(request, 'products/product_detail.html', context)
    
def detail(request, pk):
    
    try:
        product = Products.objects.get(pk=pk)
        
        context = {
            'product' : product
        }
        
    except Products.DoesNotExist:
        return render(request, 'products/detail.html', {'error_message': 'Product does not exist'})
    
    return render(request, 'products/detail.html', context)

    
    


# def management(request):
    
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         summary = request.POST.get('summary')
#         content = request.POST.get('content')
#         price = request.POST.get('price')
        
#         file = request.FILES['image']
#         filename = default_storage.save(file.name, file)
#         file_url = default_storage.url(filename)
#         img_url = file_url
#         print(filename , file_url)
#         user_grade = request.POST.get('user_grade')
#         print(user_grade)
#         # img_url = request.POST.get('img_url')
#         # img_dir = request.FILES.get('img_dir')
#         category_ids = request.POST.getlist('categories')
        
#         product = Products.objects.create(
#             name=name,
#             summary=summary,
#             content=content,
#             price=price,
#             img_url=img_url,
#             # img_dir=img_dir
#             user_id = user_grade
#         )
#         product.detail_category.add(*category_ids)
        
#         return redirect('products:detail', pk=product.pk)
#     else:
#         categories = Categories.objects.all()
#         product = Products.objects.filter()
#         context = {
#             'categories' : categories,
#             'product' : product
#         }
#         return render(request, 'products/management.html', context)


def management(request):
    
    if request.method == 'POST':
        # POST 요청이 들어왔을 때
        name = request.POST.get('name')
        summary = request.POST.get('summary')
        content = request.POST.get('content')
        price = request.POST.get('price')
        
        file = request.FILES['image']
        filename = default_storage.save(file.name, file)
        file_url = default_storage.url(filename)
        img_url = file_url

        user_grade = request.POST.get('user_grade')

        category_ids = request.POST.getlist('categories')
        
        product = Products.objects.create(
            name=name,
            summary=summary,
            content=content,
            price=price,
            img_url=img_url,
            user_id=user_grade
        )
        product.detail_category.add(*category_ids)
        
        return redirect('products:detail', pk=product.pk)  # 제품 상세 페이지로 리다이렉션
    else:
        # GET 요청이 들어왔을 때
        categories = Categories.objects.all()
        products = Products.objects.all()  # 모든 제품 가져오기
        context = {
            'categories': categories,
            'products': products  # 모든 제품을 템플릿에 전달
        }
        return render(request, 'products/management.html', context)



    
def update(request, pk):
    
    product = Products.objects.get(pk=pk)
    
    if request.method == 'POST':
        # POST 요청이 들어온 경우, 제품 정보를 업데이트합니다.
        product.name = request.POST.get('name')
        product.summary = request.POST.get('summary')
        product.content = request.POST.get('content')
        product.price = request.POST.get('price')

        # 이미지 파일이 업로드된 경우에만 이미지 업데이트
        # if 'image' in request.FILES:
        #     file = request.FILES['image']
        #     filename = default_storage.save(file.name, file)
        #     file_url = default_storage.url(filename)
        #     product.img_url = file_url

        # 카테고리 업데이트
        category_ids = request.POST.getlist('categories')
        product.detail_category.set(category_ids)

        product.save()  # 변경 사항 저장

        return redirect('products:detail', pk=product.pk)
    else:
        # GET 요청이 들어온 경우, 수정할 제품 정보를 가지고 템플릿을 렌더링합니다.
        categories = Categories.objects.all()
        context = {
            'product': product,
            'categories': categories
        }
        return render(request, 'products/edit.html', context)

        

def delete(request, pk):

    product = Products.objects.get(pk=pk)
    product.delete()
    return redirect('products:management')  # 삭제 후 상품 목록 페이지로 리다이렉트
    
