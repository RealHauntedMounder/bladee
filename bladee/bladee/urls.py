from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from core.views import index, contact, biography, discography, album_detail, signup, user_profile, like_album, unlike_album, add_comment, delete_comment
from core.forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('discography/<int:pk>/delete-comment', delete_comment, name='delete_comment'),
    path('discography/<int:pk>/add-comment', add_comment, name='add_comment'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('album/<int:album_id>/like/', like_album, name='like_album'),
    path('album/<int:album_id>/unlike/', unlike_album, name='unlike_album'),
    path('profile/', user_profile, name='user_profile'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('signup/', signup, name='signup'),
    path('discography/', discography, name='discography'),
    path('discography/<int:pk>', album_detail, name='album_detail'),
    path('biography/', biography, name='biography'),
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
