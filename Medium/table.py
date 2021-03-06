import django_tables2 as tables
from django.utils.html import format_html
from Subject.models import Subject
from django_tables2 import BooleanColumn
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





class MediumTable(tables.Table):
    # devenv = tables.Column(verbose_name='Development Environment')
    id = tables.Column(verbose_name='Sr.no')
    Operations = tables.Column(empty_values=(),orderable=False)
    isGrade = BootstrapBooleanColumn()
    # grade_system = BooleanColumn(yesno='1,2')

    def render_Operations(self, record):
        return format_html('<a href="{}/edit"><i class="fa fa-pencil"></i></a> <a href="{}/delete"><i class="fa fa-trash"></i></a>',record.id,record.id)

    class Meta:
        model = Subject
        fields = ('id', 'subjectName','isGrade','description')
        template_name = 'django_tables2/bootstrap4.html'