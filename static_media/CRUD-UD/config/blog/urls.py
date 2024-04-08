from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # READ
    path('', views.home, name='home'), ## views에 있는 home을 실행해라 뒤에 name은 별칭
    # DETAIL READ
    path('blog/<int:blog_id>', views.detail, name='detail'), # views에서 보낸 id도 들고와서 int로 변환해라
    # CREATE
    path('blog/new', views.new, name='new'), ##새글작성하기 누르면 이거 실행
    path('blog/create', views.create, name='create'), ## 작성하기 버튼 누르면 실행
    # UPDATE
    path('blog/edit/<int:blog_id>', views.edit, name='edit'),
    path('blog/update/<int:blog_id>', views.update, name='update'),
    # DELETE
    path('blog/delete/<int:blog_id>', views.delete, name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)