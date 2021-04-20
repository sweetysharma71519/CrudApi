from django.urls import path,include
from . import view
urlpatterns = [
    path('viewrecord/', view.stu_view),
    path('addrecord/', view.stu_add),
    path('recordupdate/<int:id>', view.stu_update),
    path('viewrecord_id/<int:id>', view.stu_view_id),
    path('delete/<int:id>', view.stu_delete),
    path('update_by_patch/<int:id>', view.stu_update_patch),
]
