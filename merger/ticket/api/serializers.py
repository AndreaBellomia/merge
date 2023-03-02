from rest_framework     import serializers
from ticket.models      import (ElementRadio, ElementDropDown, ElementCeckBox,
                                FieldInputText, FieldTextArea, FieldCeckBox, 
                                GroupRadioButton, GroupDropDown, GroupCeckBox,
                                TicketType, Ticket, TicketField)





""" Element Section """
class ElementRadioSerializer(serializers.ModelSerializer):
    """
    Serilize a related_name for a FieldType 
    """
    class Meta:
        model = ElementRadio
        fields = "__all__"


class ElementDropDownSerializer(serializers.ModelSerializer):
    """
    Serilize a related_name for a FieldType 
    """
    class Meta:
        model = ElementDropDown
        fields = "__all__"


class ElementCeckBoxSerializer(serializers.ModelSerializer):
    """
    Serilize a related_name for a FieldType 
    """
    class Meta:
        model = ElementCeckBox
        fields = "__all__"








""" Group Section """
class GroupRadioButtonSerializer(serializers.ModelSerializer):
    """
    Serilize a related_name for a FieldType 
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
    Serilize a related_name for a FieldType 
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
    Serilize a related_name for a FieldType 
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
    Serilize a related_name for a FieldType 
    """

    type_field = serializers.SerializerMethodField()

    def get_type_field(self, obj):
        return "text_field"

    class Meta:
        model = FieldInputText
        fields = "__all__"

class FieldTextAreaSerializer(serializers.ModelSerializer):
    """
    Serilize a related_name for a FieldType 
    """

    type_field = serializers.SerializerMethodField()

    def get_type_field(self, obj):
        return "text_area"
    class Meta:
        model = FieldTextArea
        fields = "__all__"

class FieldCeckBoxSerializer(serializers.ModelSerializer):
    """
    Serilize a related_name for a FieldType 
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

    type_document = TicketTypeRelatedSerializer(many=True)
    
    class Meta:
        model = Ticket
        fields = "__all__"