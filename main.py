from item import Item
from phone import Phone
from keyboard import Keyboard

if __name__ == '__main__':

    item1 = Keyboard("jscKeyboard", 1000, 3)
    item1.apply_discount()
    print(item1.price)

