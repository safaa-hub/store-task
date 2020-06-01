from rest_framework.routers import DefaultRouter
from .views.login_view import LoginView
from .views.add_product_view import AddProduct


router = DefaultRouter()
router.register(r'login', viewset=LoginView, basename='user')
router.register(r'product', viewset=AddProduct, basename='user')
urlpatterns = router.urls
