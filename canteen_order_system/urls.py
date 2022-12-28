"""canteen_order_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
'''
添加路由规则时顺序是很重要的，因为在尝试匹配时会按照从上到下的顺序进行，
因此应该把最模糊的路由（即空路由，对应当前网址（根网址））放在最下面
'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),   # 增加这一行 验证码
    path('', include('canteen.urls')),
    path('user/', include('user.urls')),
    path('', include('order.urls')),

]
if settings.DEBUG or True:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
