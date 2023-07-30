from django.contrib import admin
from .models import Language, Tag, Discussion, Solution, Problem, SolvedProblem


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Discussion)
class DiscussionAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'title')


@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'solution')


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'language', 'difficulty')
    filter_horizontal = ('tags', )
    date_hierarchy = 'created_date'


@admin.register(SolvedProblem)
class SolvedProblemAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'problem')