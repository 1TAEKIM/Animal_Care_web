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

    
    


def management(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        summary = request.POST.get('summary')
        content = request.POST.get('content')
        price = request.POST.get('price')
        
        file = request.FILES['image']
        filename = default_storage.save(file.name, file)
        file_url = default_storage.url(filename)
        img_url = file_url
        print(filename , file_url)
        user_grade = request.POST.get('user_grade')
        print(user_grade)
        # img_url = request.POST.get('img_url')
        # img_dir = request.FILES.get('img_dir')
        category_ids = request.POST.getlist('categories')
        
        product = Products.objects.create(
            name=name,
            summary=summary,
            content=content,
            price=price,
            img_url=img_url,
            # img_dir=img_dir
            user_id = user_grade
        )
        product.detail_category.add(*category_ids)
        
        return redirect('products:detail', pk=product.pk)
    else:
        categories = Categories.objects.all()
        
        context = {
            'categories' : categories
        }
        return render(request, 'products/management.html', context)
