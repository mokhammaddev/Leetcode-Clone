from django.contrib import admin
from .models import Category, Problem, Tag, Solutions, Difficulty, Statistic, Descriptions

admin.site.register(Category)
admin.site.register(Difficulty)
admin.site.register(Problem)
admin.site.register(Tag)
admin.site.register(Descriptions)
admin.site.register(Solutions)
admin.site.register(Statistic)
