import pytest
from unittest.mock import Mock
from vending_machine_AMAN import VendingMachine, WaitingState, AddCoinsState, DeliverProductState, CountChangeState

# Add more imports as needed for your specific test cases

def test_waiting_state():
    vending = VendingMachine()
    waiting_state = WaitingState()

    # Your test logic for WaitingState goes here

def test_add_coins_state():
    vending = VendingMachine()
    add_coins_state = AddCoinsState()

    # Your test logic for AddCoinsState goes here

def test_deliver_product_state():
    vending = VendingMachine()
    deliver_product_state = DeliverProductState()

    # Your test logic for DeliverProductState goes here

def test_count_change_state():
    vending = VendingMachine()
    count_change_state = CountChangeState()



if __name__ == '__main__':
    pytest.main()
