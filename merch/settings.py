import os
from google.oauth2 import service_account

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'k#=wzv+*d%7=f&w_d6&nsg9t_)8*o$qfn$t*b&u&n%fqpa+wfy'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '192.168.100.186']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'products.apps.ProductsConfig',
    'search.apps.SearchConfig',
    'carts.apps.CartsConfig',
    'home.apps.HomeConfig',
    'subscribe.apps.SubscribeConfig',
    'people.apps.PeopleConfig',
    'checkout.apps.CheckoutConfig',
    'myauth.apps.AuthConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'merch.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'social_django.context_processors.backends',
                # 'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'merch.wsgi.application'


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.myauth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.myauth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.myauth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.myauth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# MAILCHIMP_API_KEY = '4ad83f190d09fae8301858782dba9207-us3'
# MAILCHIMP_DATA_CENTER = 'us3'
# MAILCHIMP_AUDIENCE_ID = 'f312f373de'
#
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
#
# DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
# GS_BUCKET_NAME = 'damerch-media'
# GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
#     os.path.join(BASE_DIR, "damerch-db061d4f5ab2.json")
# )

PROJECT_ROOT = os.path.join(os.path.abspath(__file__))

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static", "static_files"),
]
MEDIA_URL = '/media/'


MEDIA_ROOT = os.path.join(BASE_DIR, "static", "media")
STATIC_ROOT = os.path.join(BASE_DIR, "static", "static_root")

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home:home'
LOGOUT_REDIRECT_URL = 'login'

# SOCIAL_AUTH_FACEBOOK_KEY = '1417736718377705'
# SOCIAL_AUTH_FACEBOOK_SECRET = '5146699705fb949e8818b47e9548872e'
# SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
# SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
#     'fields': 'id,name,email',
# }

# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '179499723802-u0bush4c1r5kpvbn4nv1fu70itfm9tgu.apps.googleusercontent.com'
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'Kr_t-xazJG29TSS8PTBR4K6a'
# SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['email']

# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SECURE_SSL_REDIRECT = True
#
# SENDGRID_API_KEY = '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'
# EMAIL_HOST = 'smtp.sendgrid.net'
# EMAIL_HOST_USER = 'damerch'
# EMAIL_HOST_PASSWORD = 'DM4288197'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
