"""
Django settings for canteen_order_system project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# 绑定当前项目 BookStore 所在的绝对路径，项目中的所有的文件都需要依赖此路径
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-588i%97#7oqezrm%)pel+0d#5b7q+_5%ta^6+*+73!9g6gmsbo'

# SECURITY WARNING: don't run with debug turned on in production!
# True 表示处于调试模式（会输出报错信息），开发时使用
DEBUG = True

# 用于配置能够访问当前站点的域名（IP地址），当 DEBUG = False 时，必须填写。详见...
ALLOWED_HOSTS = []


# Application definition
# 应用列表
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap4',
    'captcha',
    'canteen',
    'user',
    'order'

]
# 注册请求和响应之间的中间件 （不需要改）
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware', # 处理会话
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# 定了当前项目的根 URL，是 Django 路由系统的入口（网址）
ROOT_URLCONF = 'canteen_order_system.urls'
# 指定模板的配置信息
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {    # 类似全局变量
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]
# 项目部署时，Django 的内置服务器将使用的 WSGI 应用程序对象的完整 Python 路径
WSGI_APPLICATION = 'canteen_order_system.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        # 连接本地mysql数据库
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'COMS',          #你的数据库名
        'USER': 'root',         # 你的用户名
        'PASSWORD': '123456',   #你的密码
        'HOST': 'localhost',    # 本地连接
        'PORT': '3306',         # 本地端口号

    }
}



# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators
# 支持插拔的密码验证器
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/
# 语言配置（中文）
LANGUAGE_CODE = 'zh-Hans'   # 英文：'en-us'
# 时区（中国）
TIME_ZONE = 'Asia/Shanghai'              # 世界时区：'UTC'
# 开启国际化
USE_I18N = True
# 开启本地化
USE_L10N = True
# true表示存储到数据库的时间是世界时间
USE_TZ = False

# 静态资源的存放位置，静态资源包括 CSS、JS、Images
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = '/static/'

# 静态资源路径
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

# 文件、图片上传路径（数据库中只保存了一个字符串类型，真正文件保存在服务器中,即media目录下）
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')





# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'