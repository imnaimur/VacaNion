from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name ='index'),
    path('signup/',views.signup,name="signup"),
    path('signin/',views.signin,name='signin'),
    path('signout/',views.signout,name='signout'),
    path('tours/',views.tours,name='tours'),
    path('profile/',views.profile,name='profile'),
    path('changepass/',views.changepass,name='changepass'),
    path('addHotel/',views.addHotel,name='changepass'),
    path('book/<str:book_name>/',views.book,name='book')
]
