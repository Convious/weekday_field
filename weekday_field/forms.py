from django import forms

import functools
import operator

from weekday_field import utils, widgets


def coerce_value(value):
    if value is None:
        return []
    if utils.is_str(value):
        if value:
            value = [int(x) for x in value.strip('[]').split(',') if x]
        else:
            value = []
    elif isinstance(value, list):
        return [int(x) for x in value]
    return value


def has_changed(instance, initial, data):
    if instance.disabled:
        return False
    initial = coerce_value(initial)
    data = coerce_value(data)
    if len(initial) != len(data):
        return True
    initial_set = set(initial)
    data_set = set(data)
    return data_set != initial_set


class WeekdayFormField(forms.TypedMultipleChoiceField):
    def __init__(self, *args, **kwargs):
        if 'choices' not in kwargs:
          kwargs['choices'] = utils.DAY_CHOICES
        kwargs.pop('max_length', None)
        if 'widget' not in kwargs:
          kwargs['widget'] = forms.widgets.SelectMultiple
        super(WeekdayFormField, self).__init__(*args, **kwargs)

    def has_changed(self, initial, data):
        return has_changed(self, initial, data)

class AdvancedWeekdayFormField(WeekdayFormField):
    def __init__(self, *args, **kwargs):
        if 'choices' not in kwargs:
            kwargs['choices'] = utils.ADVANCED_DAY_CHOICES
        if 'widget' not in kwargs:
            kwargs['widget'] = widgets.ToggleCheckboxes
        super(AdvancedWeekdayFormField, self).__init__(*args, **kwargs)

    def clean(self, value):
        value = super(AdvancedWeekdayFormField, self).clean(value)
        if [int(i) for i in value] == list(range(7)):
            return []
        return value

    def has_changed(self, initial, data):
        return has_changed(self, initial, data)

class BitwiseWeekdayFormField(WeekdayFormField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = [(x[0], x[2]) for x in utils.BITWISE_DAY_CHOICES]
        if 'short' in kwargs:
            if kwargs['short']:
                kwargs['choices'] = [(x[0], x[1]) for x in utils.BITWISE_DAY_CHOICES]
            del kwargs['short']
        super(BitwiseWeekdayFormField, self).__init__(*args, **kwargs)

    def clean(self, value):
        value = super(BitwiseWeekdayFormField, self).clean(value)
        return functools.reduce(operator.or_, [int(x) for x in value], 0)

    def has_changed(self, initial, data):
        return has_changed(self, initial, data)
