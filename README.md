# project1
# Commit One 
Basic vending machine code structure using PySimpleGUI. Initial states and transitions without servo motor functionality.
# Hardware 
Integration with Raspberry Pi hardware using gpiozero library. Introduction of Button for coin insertion and Servo for product delivery. Verification of code compatibility with Raspberry Pi.
# Servo Motor 
Implementation of servo motor functionality for product delivery. Inclusion of servo commands to simulate the delivery process.
# Main Working 
The logic of a vending machine using PySimpleGUI and gpiozero on a Raspberry Pi. The vending machine operates through a series of states, starting in the 'waiting' state, awaiting coin insertion or product selection. Upon coin insertion, it transitions to the 'add_coins' state, allowing users to add more coins, request a refund, or select a product. If a product is selected, and the user has sufficient funds, the machine enters the 'deliver_product' state, simulating product delivery using a servo motor. After product delivery, it moves to the 'product_delivered' state, waiting for the user to press the RETURN button. Pressing RETURN in this state triggers the 'return_change_after_delivery' state, where any remaining change is returned using the servo motor. If the RETURN button is pressed in the 'add_coins' state, it enters the 'count_change' state, counting and returning the inserted coins.
