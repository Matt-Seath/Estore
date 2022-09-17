from django.urls import path, include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register("products", views.ProductViewSet, basename="products")
router.register("collections", views.CollectionViewSet)
router.register("cart", views.CartViewSet)
router.register("customer", views.CustomerViewSet)
router.register("order", views.OrderViewSet, basename="order")

products_router = routers.NestedDefaultRouter(router, "products", lookup="product")
products_router.register("reviews", views.ReviewViewSet, basename="product-reviews")

cart_router = routers.NestedDefaultRouter(router, "cart", lookup="cart")
cart_router.register("items", views.CartItemViewSet, basename="cart-items")

urlpatterns = router.urls + products_router.urls + cart_router.urls
#     path("", include(router.urls))
#     # path('products/', views.ProductList.as_view()),
#     # path('products/<int:pk>/', views.ProductDetails.as_view()),
#     # path('collections/', views.CollectionList.as_view()),
#     # path('collections/<int:pk>/', views.CollectionDetails.as_view(), name="collection-detail"),
# ]
    