from ..models import TicketType, TicketField


class TicketFieldsSerializer():
    TICKET_TYPE = None

    def __init__(self, instance, object, ticket):
        self.instance = instance  # get a ticket_type for relational fields
        self.object = object  # get a list of filds from frontend form
        self.ticket = ticket  # get a ticker instance for create a relation in TicketField

     # VALIDATOR  

    def is_valid(self):
        """
        Main function for select a validator methods
        """

        self.TICKET_TYPE = TicketType.objects.get(pk=self.instance.id)  # get TicketType models

        for field in self.object:
            """
            Register New Model field hear follow the other pattern
            """

            # FieldTextArea
            if field["type_field"] == "text_field":
                if self.validator_inputtext(field["id"], field["value"]):
                    pass
                else:
                    return False

            # FieldTextArea
            if field["type_field"] == "text_area":
                if self.validator_textarea(field["id"], field["value"]):
                    pass
                else:
                    return False


            # FieldCeckBox
            if field["type_field"] == "ceck_box":
                if self.validator_ceckbox(field["id"], field["value"]):
                    pass
                else:
                    return False


            # GroupDropDown
            if field["type_field"] == "group_radio":
                if self.validator_group_radiobutton(field["id"], field["value"]):
                    pass
                else:
                    return False


            # GroupRadioButton
            if field["type_field"] == "group_dropdown":
                if self.validator_group_dropdown(field["id"], field["value"]):
                    pass
                else:
                    return False


            # GroupCeckBox
            if field["type_field"] == "group_ceckbox":
                if self.validator_group_ceckbox(field["id"], field["value"]):
                    pass
                else:
                    return False
    
    def validator_inputtext(self, id_obj, obj):
        """
        validator for FieldInputText Models
        """

        instance = self.TICKET_TYPE.ticket_type_inputtext.get(pk=id_obj)  # get reference from a ticketType fields

        # Validate Form
        if len(obj) <= instance.max_lenght and len(obj) >= instance.min_lenght:
            return True
        else:
            return False
    
    def validator_textarea(self, id_obj, obj):
        """
        validator for FieldTextArea Models
        """

        instance = self.TICKET_TYPE.ticket_type_textarea.get(pk=id_obj)  # get reference from a ticketType fields

        # Validate Form
        if instance.max_lenght != None and instance.min_lenght != None:
            if len(obj) <= instance.max_lenght and len(obj) >= instance.min_lenght:
                return True
            else:
                return False
        
        else:
            if len(obj) <= 10000:
                return True
            else:
                return False

    def validator_ceckbox(self, id_obj, obj):
        """
        validator for FieldCeckBox Models
        """

        instance = self.TICKET_TYPE.ticket_type_field_ceckbox.get(pk=id_obj)  # get reference from a ticketType fields

        # Validate Form
        if obj in [True, False]:
            return True
        else:
            return False

    def validator_group_radiobutton(self, id_obj, obj):
        """
        validator for GroupRadioButton Models
        """

        instance = self.TICKET_TYPE.ticket_type_radiogroup.get(pk=id_obj)  # get reference from a ticketType fields

        radios = []

        for item in instance.input_group_radiogroup.all():
            radios.append(item.value)

        if obj in radios:
            return True
        else:
            return False


    def validator_group_dropdown(self, id_obj, obj):
        """
        validator for GroupDropDown Models
        """

        instance = self.TICKET_TYPE.ticket_type_dropdown.get(pk=id_obj)  # get reference from a ticketType fields

        dropdowns = []

        for item in instance.input_group_dropdown.all():
            dropdowns.append(item.value)

        if obj in dropdowns:
            return True
        else:
            return False

    def validator_group_ceckbox(self, id_obj, obj):
        """
        validator for GroupCeckBox Models
        """

        instance = self.TICKET_TYPE.ticket_type_ceckbox.get(pk=id_obj)  # get reference from a ticketType fields

        cecks = []
        validated = True

        for item in instance.input_group_ceckbox.all():
            cecks.append(item.value)

        value = ''

        for item in obj:
            if item in cecks:
                value += f'{item}|'
            else:
                return False

        if validated:
            return True




    # SAVE

    def save(self):
        """
        Main function for select a serilizer methods
        """

        self.TICKET_TYPE = TicketType.objects.get(pk=self.instance.id)  # get TicketType models

        for field in self.object:
            """
            Register New Model field hear follow the other pattern
            """

            # FieldTextArea
            if field["type_field"] == "text_field":
                self.serializer_inputtext(field["id"], field["value"])

            # FieldTextArea
            if field["type_field"] == "text_area":
                self.serializer_textarea(field["id"], field["value"])

            # FieldCeckBox
            if field["type_field"] == "ceck_box":
                self.serializer_ceckbox(field["id"], field["value"])

            # GroupDropDown
            if field["type_field"] == "group_radio":
                self.serializer_group_radiobutton(field["id"], field["value"])

            # GroupRadioButton
            if field["type_field"] == "group_dropdown":
                self.serializer_group_dropdown(field["id"], field["value"])

                # GroupCeckBox
            if field["type_field"] == "group_ceckbox":
                self.serializer_group_ceckbox(field["id"], field["value"]) 

    def serializer_inputtext(self, id_obj, obj):
        """
        serializer for FieldInputText Models
        """

        instance = self.TICKET_TYPE.ticket_type_inputtext.get(pk=id_obj)  # get reference from a ticketType fields

        # Validate Form
        if len(obj) <= instance.max_lenght and len(obj) >= instance.min_lenght:

            # Save form in db
            TicketField.objects.create(lable=instance.lable, value=str(obj), ticket_type=self.ticket, ).save()
        else:
            # return Error
            print(
                f'{obj} does not meet the field requirements | max_lenght {instance.max_lenght} and min_lenght {instance.min_lenght}')
            raise ValueError

    def serializer_textarea(self, id_obj, obj):
        """
        serializer for FieldTextArea Models
        """

        instance = self.TICKET_TYPE.ticket_type_textarea.get(pk=id_obj)  # get reference from a ticketType fields

        if instance.max_lenght != None and instance.min_lenght != None:
            if len(obj) <= instance.max_lenght and len(obj) >= instance.min_lenght:
                TicketField.objects.create(lable=instance.lable, value=str(obj), ticket_type=self.ticket, ).save()
            else:
                # return Error
                print(
                    f'{obj} does not meet the field requirements | max_lenght {instance.max_lenght} and min_lenght {instance.min_lenght}')
                raise ValueError
        
        else:
            if len(obj) <= 10000:
                TicketField.objects.create(lable=instance.lable, value=str(obj), ticket_type=self.ticket, ).save()
            else:
                # return Error
                print(
                    f'{obj} does not meet the field requirements | max_lenght {10000}')
                raise ValueError

    def serializer_ceckbox(self, id_obj, obj):
        """
        serializer for FieldCeckBox Models
        """

        instance = self.TICKET_TYPE.ticket_type_field_ceckbox.get(pk=id_obj)  # get reference from a ticketType fields

        if obj in [True, False]:
            TicketField.objects.create(lable=instance.lable, value=str(obj), ticket_type=self.ticket, ).save()
        else:
            # return Error
            print(f'{obj} does not meet the field requirements | value must be a boolean (True, False)')
            raise ValueError

    def serializer_group_radiobutton(self, id_obj, obj):
        """
        serializer for GroupRadioButton Models
        """

        instance = self.TICKET_TYPE.ticket_type_radiogroup.get(pk=id_obj)  # get reference from a ticketType fields

        radios = []

        for item in instance.input_group_radiogroup.all():
            radios.append(item.value)

        if obj in radios:
            TicketField.objects.create(lable=instance.lable, value=str(obj), ticket_type=self.ticket, ).save()
        else:
            # return Error
            print(f'{obj} does not meet the field requirements | value not allowed')
            raise ValueError

    def serializer_group_dropdown(self, id_obj, obj):
        """
        serializer for GroupDropDown Models
        """

        instance = self.TICKET_TYPE.ticket_type_dropdown.get(pk=id_obj)  # get reference from a ticketType fields

        dropdowns = []

        for item in instance.input_group_dropdown.all():
            dropdowns.append(item.value)

        if obj in dropdowns:
            TicketField.objects.create(lable=instance.lable, value=str(obj), ticket_type=self.ticket, ).save()
        else:
            # return Error
            print(f'{obj} does not meet the field requirements | value not allowed')
            raise ValueError

    def serializer_group_ceckbox(self, id_obj, obj):
        """
        serializer for GroupCeckBox Models
        """

        instance = self.TICKET_TYPE.ticket_type_ceckbox.get(pk=id_obj)  # get reference from a ticketType fields

        cecks = []
        validated = True

        for item in instance.input_group_ceckbox.all():
            cecks.append(item.value)

        value = ''

        for item in obj:
            if item in cecks:
                value += f'{item}|'
            else:
                # return Error
                print(f'{obj} does not meet the field requirements | value not allowed')
                validated = False
                raise ValueError

        if validated:
            TicketField.objects.create(lable=instance.lable, value=value, ticket_type=self.ticket, ).save()
