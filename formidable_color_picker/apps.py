from __future__ import absolute_import
from django.apps import AppConfig


class FormidableColorPickerConfig(AppConfig):
    """
    Formidable Color Picker configuration class.
    """
    name = 'formidable_color_picker'

    def ready(self):
        """
        Load external serializer when ready
        """
        from . import serializers  # noqa
