from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog

# READ
def home(request):
    blogs = Blog.objects.all() ## Blog(냉장고 매니저)에 부탁해 모든 객체가져와서 blogs에 저장 
    return render(request, 'home.html', {'blogs': blogs}) ## 가져온 결과 blogs를  blogs라는 이름으로 home.html에 담아줄거야 , render: httpresponse객체로 값 반환

# DETAIL READ
def detail(request, blog_id): # url에서 보낸 blog_id도 매개변수로 받음
    blog = get_object_or_404(Blog, pk=blog_id) #pk=blog_id를 Blog객체에서 가져오고 없으면 404에러 발생시켜
    return render(request, 'detail.html', {'blog': blog})


# CREATE
def new(request):
    return render(request, 'new.html') ##그냥 페이지만 뿌려주면 됌


def create(request):
    new_blog = Blog() ## 빈 모델 객체 만듦
    new_blog.title = request.POST['title'] ## POST요청으로 온 name=title인 정보 뺴서 new_blog객체의 title에 저장
    new_blog.content = request.POST['content']
    new_blog.save() ## 객체에 정보 저장
    return redirect('detail', new_blog.id) # detail이라는 이름의url로 redirect 하는데 new_blog.id도 들고가라
    # return render(request, 'detail.html', {'blog': new_blog})


# UPDATE
def edit(request, blog_id):
    edit_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'edit.html', {'edit_blog':edit_blog})


def update(request, blog_id):
    old_blog = get_object_or_404(Blog, pk=blog_id)
    old_blog.title = request.POST.get('title')
    old_blog.content = request.POST.get('content')
    old_blog.save()
    return redirect('detail', old_blog.id)
    # return render(request, 'detail.html', {'blog': old_blog}) #render요청은 url변경x, 근데 화면은 바뀜, 데이터를 dictionary형태로 전송가능git remote set-url origin


# DELETE
def delete(request, blog_id):
    delete_blog = get_object_or_404(Blog, pk=blog_id)
    delete_blog.delete()
    return redirect('home')