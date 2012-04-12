DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

INSTALLED_APPS = (
    'raiseexception',
)

ROOT_URLCONF = 'raiseexception.urls'
