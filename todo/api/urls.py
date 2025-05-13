from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('',views.TodoModelViewSet,basename='todo')
urlpatterns = router.urls