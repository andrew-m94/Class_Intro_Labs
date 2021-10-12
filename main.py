from alarm_clock import AlarmClock
from cell_phone import CellPhone

alarm_clock_1 = AlarmClock()
alarm_clock_1.set_change_time()
alarm_clock_1.set_alarm()
alarm_clock_1.toggle_on_off()

johns_cell = CellPhone('Samsung Galaxy')

johns_cell.add_contact()
johns_cell.add_contact()
johns_cell.add_contact()
johns_cell.print_contacts()

johns_cell.recieve_text('Hi john, you won a car! Go "here" to claim!')
johns_cell.recieve_text('Urgent: Call me back!')
johns_cell.check_messages()

johns_cell.send_text()

johns_cell.toggle_vibrate()