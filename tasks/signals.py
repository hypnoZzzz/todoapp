from django.db.models.signals import m2m_changed, post_delete, post_save
from django.dispatch import receiver
from tasks.models import TodoItem, Category


@receiver(post_delete, sender=TodoItem)
def task_removed(sender, **kwargs):
    task_cats_changed('dummy', 'dummy', 'post_remove', 'dummy')


@receiver(m2m_changed, sender=TodoItem.category.through)
def task_cats_changed(sender, instance, action, model, **kwargs):
    if action == 'post_add':
        qs = instance.category.all()
    elif action == 'post_remove':
        qs = Category.objects.all()
    else:
        return
    for cat in qs:
        Category.objects.filter(id=cat.id).update(
            todo_count=TodoItem.objects.filter(category__id=cat.id).count()
        )

    todo_qs = TodoItem.objects.prefetch_related('category')

    for cat in Category.objects.all():
        cat_qs = todo_qs.filter(category__id=cat.id)

        high_priority = cat_qs.filter(priority=TodoItem.PRIORITY_HIGH).count()
        medium_priority = cat_qs.filter(priority=TodoItem.PRIORITY_MEDIUM).count()
        low_priority = cat_qs.filter(priority=TodoItem.PRIORITY_LOW).count()

        cat.high_priority = high_priority
        cat.medium_priority = medium_priority
        cat.low_priority = low_priority
        cat.save()




# from django.db.models.signals import m2m_changed
# from django.dispatch import receiver
# from tasks.models import TodoItem, Category
# from collections import Counter
#
#
# @receiver(m2m_changed, sender=TodoItem.category.through)
# def task_cats_added(sender, instance, action, model, **kwargs):
#     if action != "post_add":
#         return
#
#     for cat in instance.category.all():
#         slug = cat.slug
#
#         new_count = 0
#         for task in TodoItem.objects.all():
#             new_count += task.category.filter(slug=slug).count()
#
#         Category.objects.filter(slug=slug).update(todos_count=new_count)
#
#
# @receiver(m2m_changed, sender=TodoItem.category.through)
# def task_cats_removed(sender, instance, action, model, **kwargs):
#     if action != "post_remove":
#         return
#
#     cat_counter = Counter()
#     for t in TodoItem.objects.all():
#         for cat in t.category.all():
#             cat_counter[cat.slug] += 1
#
#     for slug, new_count in cat_counter.items():
#         Category.objects.filter(slug=slug).update(todos_count=new_count)