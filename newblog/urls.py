from django.contrib import admin
from django.urls import path
import newapp.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', newapp.views.home, name="home"),
    path('create/', newapp.views.create, name="create"),
    path('new/', newapp.views.new, name="new"),
    path('read/<int:post_id>/', newapp.views.read, name="read"),
    path('read/<int:post_id>/update/', newapp.views.update, name="update"),
    path('read/<int:post_id>/renew/', newapp.views.renew, name='renew'), 
    #newapp.views.renew는 뉴앱에 있는 views.py에서 renew라는 함수를 실행하겠다는 뜻.
    path('read/<int:blog_id>/delete/', newapp.views.delete, name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
