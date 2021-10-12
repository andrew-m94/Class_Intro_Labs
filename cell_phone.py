class CellPhone:
    def __init__(self, model):
        self.model = model
        self.phone_number = 0
        self.contacts = {}
        self.messages = []
        self.vibrate = False

    def recieve_text(self,text_message):
        self.messages.append(text_message)

    def toggle_vibrate(self):

        if self.vibrate == False:
            print('Vibrate: ON')
            self.vibrate = True

        elif self.vibrate == True:
            print('Vibrate: OFF')
            self.vibrate == False

    def send_text(self):
        found = False
        while found == False:
            contact = input('Enter contact name: ')
            
            if contact in self.contacts:
                found = True
                input('Enter message: ')
                print(f'Sending message to {self.contacts[contact]}...')
                print('message sent')
            else:
                print('Contact not found')
                
    def add_contact(self):
        name = input('Enter contact name: ')
        phone_number = input('Enter phone number: ')
        self.contacts[name] = int(phone_number)

    def print_contacts(self):
        for contact in self.contacts:
            print('{}:{}'.format(contact, self.contacts[contact]))

    def check_messages(self):
        for message in self.messages:
            print(message)