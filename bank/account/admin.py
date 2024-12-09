from django.contrib import admin
from .models import bndjango
class bndjangoAdmin(admin.ModelAdmin):
  list_display= ('username','password','email')
admin.site.register(bndjango,bndjangoAdmin)
