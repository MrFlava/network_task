from django_filters import DateFilter, FilterSet

from posts.models import Like


class AnalyticsFilter(FilterSet):
    start_date = DateFilter(field_name='date_liked', lookup_expr='gte')
    end_date = DateFilter(field_name='date_liked', lookup_expr='lte')

    class Meta:
        model = Like
        fields = ['date_liked', 'start_date', 'end_date', ]
