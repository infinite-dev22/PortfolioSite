from django.contrib import admin
from .models import ContactModel, UploadModel

# Register your models here.
admin.site.register(ContactModel)
admin.site.register(UploadModel)
