from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

#These url patterns match the first routing. So when we go to localhost:8000
# then it checks wheter we have a pattern for a empty string or not. Yes there is a empty string.
# So then goes to included portion which is blog.urls. It chops of the initaial portion which was matched.
# So if path was blog/about/ then it would only return about/ to the blog.urls
urlpatterns = [
path("admin/", admin.site.urls),
path('register/',user_views.register,name = 'register'),
path('profile/',user_views.profile,name = 'profile'),
path('login/',auth_views.LoginView.as_view(template_name = 'users/login.html'),name = 'login'),
path('logout/',auth_views.LogoutView.as_view(template_name = 'users/logout.html'),name = 'logout'),
path('password-reset/',auth_views.PasswordResetView.as_view(template_name = 'users/password_reset.html'),name = 'password_reset'),
path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name = 'users/password_reset_complete.html'),name = 'password_reset_complete'),
path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name = 'users/password_reset_done.html'),name = 'password_reset_done'),
path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = 'users/password_reset_confirm.html'),name = 'password_reset_confirm'),
path("", include('blog.urls')),

]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

