from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from triptraceapi.views import register_user, check_user, TripView, UserView, StopView, ItemView, StopCategoryView, CategoryView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'trips', TripView, 'trip')
router.register(r'users', UserView, 'user')
router.register(r'stops', StopView, 'stop')
router.register(r'items', ItemView, 'item')
router.register(r'stopcategories', StopCategoryView, 'stopcategory')
router.register(r'categories', CategoryView, 'category')

urlpatterns = [
    path('register', register_user),
    path('checkuser', check_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
