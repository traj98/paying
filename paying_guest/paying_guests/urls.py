from paying_guests import views
from django.conf.urls import url
from django.urls import path

urlpatterns = [
			path('home',views.Home,name ='home'),
            # path('',views.index,name ='index'),
            # path('contact',views.Contact,name ='contact'),
            # path('gallery',views.Gallery,name ='gallery'),
            # path('detail/<int:course_id>/',views.detail,name ='detail'),
            # path('payment',views.Payment,name = 'payment'),
            # path('success',views.Final,name = 'success'),
            # path('blog',views.Blog,name='blog'),
            # path('blog-detail/<slug:slug>/',views.blog_detail,name='blog-detail'),
           
]