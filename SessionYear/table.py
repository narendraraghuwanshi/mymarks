import django_tables2 as tables
from django.utils.html import format_html
from SessionYear.models import SessionYear,SessionCourseExam
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

class SessionYearTable(tables.Table):
    # devenv = tables.Column(verbose_name='Development Environment')
    id = tables.Column(verbose_name='Sr.no')
    Operations = tables.Column(empty_values=(),orderable=False)
    # isGrade = BootstrapBooleanColumn()
    # grade_system = BooleanColumn(yesno='1,2')

    def render_Operations(self, record):
        return format_html('<a href="{}/edit" class="btn btn-sm btn-success"><i class="fa fa-pencil"></i></a> <a href="{}" class="btn btn-sm btn-warning"><i class="fa fa-eye"></i></a> <a onclick="Delete({})" class="btn btn-sm btn-danger"><i class="fa fa-trash"></i></a>',record.id,record.id,record.id)

    class Meta:
        model = SessionYear
        fields = ('id', 'year','sessionDescription')
        template_name = 'django_tables2/bootstrap4.html'

