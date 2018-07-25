from formidable.register import load_serializer, FieldSerializerRegister
from formidable.serializers.fields import FieldSerializer, BASE_FIELDS

field_register = FieldSerializerRegister.get_instance()


@load_serializer(field_register)
class ColorPickerFieldSerializer(FieldSerializer):

    type_id = 'color_picker'

    class Meta(FieldSerializer.Meta):
        fields = BASE_FIELDS
