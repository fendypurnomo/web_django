from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from django.urls import include, path
from rest_framework import routers
from apps.news.views import ReporterViewSet, ArticleViewSet
from apps.offices.views import DepartmentViewSet, EmployeeViewSet

admin.site.site_title = 'Fendy site admin'
admin.site.site_header = 'Fendy administration'
admin.site.index_title = 'Site administration'

router = routers.DefaultRouter()
router.register(r'news/reporter', ReporterViewSet)
router.register(r'news/article', ArticleViewSet)
router.register(r'offices/department', DepartmentViewSet)
router.register(r'offices/employee', EmployeeViewSet)

urlpatterns = [
    path('catalog/', include('apps.catalog.urls')),
    path('news/', include('apps.news.urls')),
    path('polls/', include('apps.polls.urls')),

    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/docs/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),

    path('resetPassword/', views.PasswordResetView.as_view(), name='password_reset'),
    path('resetPassword/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('resetPassword/confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('resetPassword/complete/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('signin/', admin.site.login, name='signin'),
    path('login/', admin.site.login, name='login'),

    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
