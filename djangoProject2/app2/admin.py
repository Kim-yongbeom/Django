from django.contrib import admin

# Register your models here.

import app2.models

admin.site.register(app2.models.Product)