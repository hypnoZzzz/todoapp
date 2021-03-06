from django.contrib import admin

from tasks.models import TodoItem, Category


@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('description', 'is_completed', 'created', 'list_categories')

    def list_categories(self, obj):
        return list(obj.category.all())

    list_categories.short_description = 'Список категорий'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('slug', 'name', 'todos_count')

