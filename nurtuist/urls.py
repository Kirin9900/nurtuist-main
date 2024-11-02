from django.urls import path
from chatapp import views

urlpatterns = [
    path('page1/', views.page1_view, name='page1'),  # 将 page1 设置为根 URL
    path('', views.log_in_view, name='log_in'),
    path('get_log_in/', views.log_in, name='get_log_in'),
    path('get_recipe/', views.get_recipe, name='get_recipe'),  # URL 用于处理表单提交
    path('personal/', views.personal_page_view, name='personal_page'),
    path('index/', views.index_view, name='index'),  # 添加 index.html 的 URL
    path('sign_up/', views.sign_up_view, name='sign_up'),
    path('get_sign_up/', views.sign_up, name='get_sign_up'),
    path('lunbo/', views.get_food_view, name='lunbo'),
    path('store/', views.store, name='store'),
    path('distribution/', views.distribution, name='distribution')
    # ... 其他 URL 模式 ...
]
