from rest_framework import serializers

from .autofield import TicketFieldsSerializer
from ..models import (ElementRadio, ElementDropDown, ElementCeckBox,
                      FieldInputText, FieldTextArea, FieldCeckBox,
                      GroupRadioButton, GroupDropDown, GroupCeckBox,
                      TicketType, Ticket)

""" Element Section """


class ElementRadioSerializer(serializers.ModelSerializer):
    """
    Serialize a related_name for a FieldType
    """

    class Meta:
        model = ElementRadio
        fields = "__all__"


class ElementDropDownSerializer(serializers.ModelSerializer):
    """
    Serialize a related_name for a FieldType
    """

    class Meta:
        model = ElementDropDown
        fields = "__all__"


class ElementCeckBoxSerializer(serializers.ModelSerializer):
    """
    Serialize a related_name for a FieldType
    """

    class Meta:
        model = ElementCeckBox
        fields = "__all__"


""" Group Section """


class GroupRadioButtonSerializer(serializers.ModelSerializer):
    """
    Serialize a related_name for a FieldType
    """

    input_group_radiogroup = ElementRadioSerializer(many=True)

    type_field = serializers.SerializerMethodField()

    def get_type_field(self, obj):
        return "group_radio"

    class Meta:
        model = GroupRadioButton
        fields = "__all__"


class GroupDropDownSerializer(serializers.ModelSerializer):
    """
    Serialize a related_name for a FieldType
    """

    input_group_dropdown = ElementDropDownSerializer(many=True)

    type_field = serializers.SerializerMethodField()

    def get_type_field(self, obj):
        return "group_dropdown"

    class Meta:
        model = GroupDropDown
        fields = "__all__"


class GroupCeckBoxSerializer(serializers.ModelSerializer):
    """
    Serialize a related_name for a FieldType
    """

    input_group_ceckbox = ElementCeckBoxSerializer(many=True)

    type_field = serializers.SerializerMethodField()

    def get_type_field(self, obj):
        return "group_ceckbox"

    class Meta:
        model = GroupCeckBox
        fields = "__all__"


""" Field Section """


class FieldInputTextSerializer(serializers.ModelSerializer):
    """
    Serialize a related_name for a FieldType
    """

    type_field = serializers.SerializerMethodField()

    def get_type_field(self, obj):
        return "text_field"

    class Meta:
        model = FieldInputText
        fields = "__all__"


class FieldTextAreaSerializer(serializers.ModelSerializer):
    """
    Serialize a related_name for a FieldType
    """

    type_field = serializers.SerializerMethodField()

    def get_type_field(self, obj):
        return "text_area"

    class Meta:
        model = FieldTextArea
        fields = "__all__"


class FieldCeckBoxSerializer(serializers.ModelSerializer):
    """
    Serialize a related_name for a FieldType
    """
    type_field = serializers.SerializerMethodField()

    def get_type_field(self, obj):
        return "ceck_box"

    class Meta:
        model = FieldCeckBox
        fields = "__all__"


class TicketTypeSerializer(serializers.ModelSerializer):
    """
    TicketType Serializer without related fields
    """

    class Meta:
        model = TicketType
        fields = "__all__"


class TicketTypeRelatedSerializer(serializers.ModelSerializer):
    """
    TicketType Serializer with related fields
    """

    class Meta:
        model = TicketType
        exclude = ('img_url', 'status')

    ticket_type_radiogroup = GroupRadioButtonSerializer(many=True)
    ticket_type_dropdown = GroupDropDownSerializer(many=True)
    ticket_type_ceckbox = GroupCeckBoxSerializer(many=True)

    ticket_type_inputtext = FieldInputTextSerializer(many=True)
    ticket_type_textarea = FieldTextAreaSerializer(many=True)
    ticket_type_field_ceckbox = FieldCeckBoxSerializer(many=True)


class TicketsSerializer(serializers.ModelSerializer):
    json_fields = serializers.JSONField(required=False)


    class Meta:
        model = Ticket
        fields = '__all__'

    
    def validate(self, value):
        # Validate autofield
        try:
            # Get instance of TicketType
            instance = TicketType.objects.get(pk=self.initial_data["type_document"])
            if TicketFieldsSerializer(instance, value["json_fields"], instance).is_valid() == False:
                raise serializers.ValidationError("Fields Value not validated")
        except:
            raise serializers.ValidationError("Error during get a TicketType instance")
        return value
    

    def create(self, validated_data):
        # get info for the class
        type_document = validated_data["type_document"]
        json_fields = validated_data["json_fields"]

        # Delete extra fields for saving in db model
        del validated_data["json_fields"]
        instance = super().create(validated_data)
        
        # Save fields in correct model
        TicketFieldsSerializer(type_document, json_fields, instance).save()
        return instance
