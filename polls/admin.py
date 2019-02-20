from django.contrib import admin

# Register your models here.
from .models import Question, CL_CHASIS

admin.site.register(Question)
admin.site.register(CL_CHASIS)
