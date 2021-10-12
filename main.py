from alarm_clock import AlarmClock
from cell_phone import CellPhone
from customer import Customer
from product import Product

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

customer_1  = Customer('John')
print(customer_1.name)

bread = Product('Bread', 2.50, 'Food')
eggs = Product('Eggs', 3.00, 'Food')
milk = Product('Milk', 3.50, 'Food')
customer_1.add_product(bread)
customer_1.add_product(eggs)
customer_1.add_product(milk)

customer_1.view_cart()
total_price = customer_1.cart.total_price()
print(f'${total_price}')

customer_1.cart.clear_cart()
customer_1.view_cart()