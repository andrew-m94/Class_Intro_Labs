import datetime

class AlarmClock:
    def __init__(self,):
        self.current_time = datetime.datetime.now()
        self.on_off = False
        self.alarm_time = ''

    def set_change_time(self):
        
        print(self.current_time.strftime('%I:%M %p'))
        yes_no = input('is this the current time? Y/N: ')
        
        if yes_no.upper() == 'N':
            new_time = input('\nPlease enter the correct time: ')
            self.current_time = new_time

    def toggle_on_off(self):
        
        if self.on_off == False:
            print('The alarm is now on.')
            print(f'It will ring at {self.alarm_time}')
            self.on_off = True

        elif self.on_off == True:
            print('The alarm is now off.')
            self.on_off = False
    
    def set_alarm(self):

        if self.alarm_time == '':
            self.alarm_time = input('Enter the time you want your alarm to ring: ')

        else:
            print(f'Your current alarm time is: {self.alarm_time}')
            yes_no = input('Would you like to change the time? Y/N')

            if yes_no.upper() == 'Y':
                self.alarm_time = input('Enter the time you want your alarm to ring: ')

