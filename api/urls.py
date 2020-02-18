from django.urls import include, path
from .views import ParkirDetail,ParkirList,UserCreate,SaldoList

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("parkirs/", ParkirList.as_view(), name="parkir_list"),
    path("parkirs/<str:booking_place>/", ParkirDetail.as_view(), name="parkir_detail"),
    path("users/", UserCreate.as_view(), name="user_create"),
    path("saldos/<int:pk>", SaldoList.as_view(), name="saldo_list"),
    # path("login/", LoginView.as_view(), name="login"),
]