
from ticket.models import TicketType, TicketField

class TicketFieldsSerializer():

    TICKET_TYPE = None

    def __init__(self, instace, object, ticket):
        self.instace = instace # get a ticket_type for relational fields
        self.object = object   # get a list of filds from frontend form
        self.ticket = ticket   # get a ticker instace for create a relation in TicketField
        
        self.main()   # Execute a main fuction in class


    def main(self):
        """
        Main function for select a serilizer methods
        """

        self.TICKET_TYPE = TicketType.objects.get(pk=self.instace.id) # get TicketType models


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

        instace = self.TICKET_TYPE.ticket_type_inputtext.get(pk=id_obj) # get reference from a ticketType fields


        #Validate Form
        if len(obj) <= instace.max_lenght and len(obj) >= instace.min_lenght:

            # Save form in db
            TicketField.objects.create(
                lable=instace.lable,
                value=str(obj),
                ticket_type=self.ticket,
            ).save()
        else:
            #return Error
            print(f'{obj} does not meet the field requirements | max_lenght {instace.max_lenght} and min_lenght {instace.min_lenght}')
            raise ValueError
    

    def serializer_textarea(self, id_obj, obj):
        """
        serializer for FieldTextArea Models
        """

        instace = self.TICKET_TYPE.ticket_type_textarea.get(pk=id_obj) # get reference from a ticketType fields

        if instace.max_lenght != None and instace.min_lenght != None:
            if len(obj) <= instace.max_lenght and len(obj) >= instace.min_lenght:
                TicketField.objects.create(
                    lable=instace.lable,
                    value=str(obj),
                    ticket_type=self.ticket,
                ).save()
            else:
                #return Error
                print(f'{obj} does not meet the field requirements | max_lenght {instace.max_lenght} and min_lenght {instace.min_lenght}')
                raise ValueError
    
    def serializer_ceckbox(self, id_obj, obj):
        """
        serializer for FieldCeckBox Models
        """

        instace = self.TICKET_TYPE.ticket_type_field_ceckbox.get(pk=id_obj) # get reference from a ticketType fields

        if obj in [True, False]:
            TicketField.objects.create(
                lable=instace.lable,
                value=str(obj),
                ticket_type=self.ticket,
            ).save()
        else:
            #return Error
            print(f'{obj} does not meet the field requirements | value must be a boolean (True, False)')
            raise ValueError

    def serializer_group_radiobutton(self, id_obj, obj):
        """
        serializer for GroupRadioButton Models
        """

        instace = self.TICKET_TYPE.ticket_type_radiogroup.get(pk=id_obj) # get reference from a ticketType fields

        radios = []

        for item in instace.input_group_radiogroup.all():
            radios.append(item.value)

        if obj in radios:
            TicketField.objects.create(
                lable=instace.lable,
                value=str(obj),
                ticket_type=self.ticket,
            ).save()
        else:
            #return Error
            print(f'{obj} does not meet the field requirements | value not allowed')
            raise ValueError
        
    def serializer_group_dropdown(self, id_obj, obj):
        """
        serializer for GroupDropDown Models
        """

        instace = self.TICKET_TYPE.ticket_type_dropdown.get(pk=id_obj) # get reference from a ticketType fields

        dropdowns = []

        for item in instace.input_group_dropdown.all():
            dropdowns.append(item.value)
            
        if obj in dropdowns:
            TicketField.objects.create(
                lable=instace.lable,
                value=str(obj),
                ticket_type=self.ticket,
            ).save()
        else:
            #return Error
            print(f'{obj} does not meet the field requirements | value not allowed')
            raise ValueError
        

    def serializer_group_ceckbox(self, id_obj, obj):
        """
        serializer for GroupCeckBox Models
        """

        instace = self.TICKET_TYPE.ticket_type_ceckbox.get(pk=id_obj) # get reference from a ticketType fields

        cecks = []
        validated = True

        for item in instace.input_group_ceckbox.all():
            cecks.append(item.value)

        value = ''

        for item in obj:
            if item in cecks:
                value += f'{item}|'
            else:
                #return Error
                print(f'{obj} does not meet the field requirements | value not allowed')
                validated = False
                raise ValueError

        if validated:
            TicketField.objects.create(
                lable=instace.lable,
                value=value,
                ticket_type=self.ticket,
            ).save()

