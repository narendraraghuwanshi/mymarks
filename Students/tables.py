import django_tables2 as tables

from django_tables2.utils import A
from django.utils.html import format_html
from Students.models import Students
from django_tables2 import BooleanColumn, Column, Table
from django.utils.safestring import mark_safe
from django_tables2.utils import AttributeDict


class BootstrapBooleanColumn(BooleanColumn):
    def __init__(self, null=False, **kwargs):
        if null:
            kwargs["empty_values"] = ()
        super(BooleanColumn, self).__init__(**kwargs)

    def render(self, value):
        value = bool(value)
        html = "<i %s></i>"

        class_name = "fa fa-times"
        if value:
            class_name = "fa fa-check"
        attrs = {'class': class_name,'style':'font-size:20px'}

        attrs.update(self.attrs.get('span', {}))

        return mark_safe(html % (AttributeDict(attrs).as_html()))





class StudentsTable(tables.Table):

    Operations = tables.Column(empty_values=(),orderable=False)

    def render_Operations(self, record):
        return format_html('<a href="{}/edit" class="btn btn-sm btn-success"><i class="fa fa-pencil"></i></a> <a onclick="Delete({})" class="btn btn-sm btn-danger"><i class="fa fa-trash"></i></a>',record.user_id,record.user_id)

    class Meta:
        model = Students
        fields = ('user.first_name','course.courseName','rollNumber','fatherName','motherName')
        template_name = 'django_tables2/bootstrap4.html'

