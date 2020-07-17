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

SECRET_KEY = 'YS+ATOQdtOwhA4TRgIyOBO12y7bGswjW9W0NTFjED8bYAqF/RA'
