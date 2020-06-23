from rest_framework.routers import DefaultRouter
from .views.login_view import LoginView
from .views.add_product_view import AddProduct
from .views.registration_view import RegisterViewSet
from .views.get_product import GetProduct
from .views.list_products import ListProducts
from .views.update_product import UpdateProduct
from .views.upload_image import UploadImage

router = DefaultRouter()
router.register(r'login', viewset=LoginView, basename='user')
router.register(r'add-product', viewset=AddProduct, basename='user')
router.register(r'registration', viewset=RegisterViewSet, basename='user')
router.register(r'get-product', viewset=GetProduct, basename='user')
router.register(r'all-products', viewset=ListProducts, basename='user')
router.register(r'update-product', viewset=UpdateProduct, basename='user')
router.register(r'image', viewset=UploadImage, basename='user')
urlpatterns = router.urls
