from rest_framework import serializers
from formidable.register import load_serializer, FieldSerializerRegister
from formidable.serializers.fields import FieldSerializer, BASE_FIELDS

field_register = FieldSerializerRegister.get_instance()


@load_serializer(field_register)
class ColorPickerFieldSerializer(FieldSerializer):

    type_id = 'color_picker'
    parameters = serializers.JSONField()

    allowed_formats = ('rgb', 'hex')
    default_error_messages = {
        "missing_parameter": "You need a `format` parameter for this field",
        "invalid_format": "Invalid format: `{format}` is not one of {formats}."
    }

    class Meta(FieldSerializer.Meta):
        fields = BASE_FIELDS + ('parameters',)

    def to_internal_value(self, data):

        # Check if the parameters are compliant
        parameters = data.get('parameters', {})
        if set(parameters.keys()) != {'format'}:
            self.fail('missing_parameter')

        format = parameters.get('format')
        if format not in self.allowed_formats:
            self.fail("invalid_format",
                      format=format, formats=self.allowed_formats)

        return super(ColorPickerFieldSerializer, self).to_internal_value(data)
