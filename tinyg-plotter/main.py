#!usr/bin/env python
"""
main.py, by Pawel Wojcik, 20-01-2017

TINYG PLOTTER - Main screen
"""

import os
import serial
from time import sleep

title = "TINYG PLOTTER"

# Program main menu
def main_menu():
    menu_width = 32
    active_menu = "Main"
    menu_description = "* ITSligo - L7 in Mechatronics *"
    menu_list = ["C - Connect",
                 "A - About",
                 "Q - Quit"]

    os.system("clear")      # clear screen
    print(menu(menu_width,title, active_menu, menu_description, menu_list))     # print menu
    selection = input("Select: ").lower()      # wait for user selection
    if selection == "c":
        connect()
    elif selection == "a":
        about()
    elif selection == "q":
        close()
    else:
        invalid_selection()


# Connect to the board
def connect():
    menu_width = 25
    active_menu = "Connected"
    menu_description = "Sucesfully connected"
    menu_list = ["H - Home TinyG Plotter",
                 "M - Main menu",
                 "Q - Quit"]
    os.system("clear")

    # connection details goes here
    ser = serial.Serial(port="/dev/cu.usbserial-DN00WNBE",baudrate=115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=1, xonxoff=False, rtscts=True, write_timeout=None, dsrdtr=False, inter_byte_timeout=None)
    ser.close()
    os.system("clear")
    print(menu(menu_width, title, active_menu, menu_description, menu_list))

    selection = input("Select: ").lower()
    if selection == "m":
        main_menu()
    elif selection == "q":
        close()
    elif selection == "h":
        ser.open()
        sleep(0.5)
        ser.write(str.encode("g28.2x0y0\n"))
        ser.readlines()
        ser.close()
    else:
        invalid_selection()


# About information
def about():
    menu_width = 26
    active_menu = "About"
    menu_description = "Author: Pawel Wojcik\nEmail: wojcikpwl@gmail.com\nVersion: 0.1"
    menu_list = ["M - Main menu",
                 "Q - Quit"]
    os.system("clear")

    print(menu(menu_width, title, active_menu, menu_description, menu_list))

    selection = input("Select: ").lower()

    if selection == "m":
        main_menu()

    elif selection == "q":
        close()

    else:
        invalid_selection()


# Menu generator
def menu(width, title, menu_name, menu_description, menu_content):
    return (title + " [" + menu_name + "]\n" + width * "="
            + "\n" + menu_description + "\n" + width * "-" + "\n"
            + "\n".join(menu_content) + "\n" + width * "-")


# Wrong selection message
def invalid_selection():
    os.system("clear")
    menu_width = 27
    active_menu = "Error"
    menu_description = "Wrong entry"
    menu_list = ["Press ENTER to try again..."]

    os.system("clear")
    print(menu(menu_width, title, active_menu, menu_description, menu_list))

    input()

    main_menu()


# Closing message
def close():
    menu_width = 33
    active_menu = "Exit"
    menu_description = "Thank you for using TinyG Plotter"
    menu_list = ["Press ENTER to quit..."]

    os.system("clear")
    print(menu(menu_width, title, active_menu, menu_description, menu_list))

    input()

    os.system("clear")


if __name__ == '__main__':
    main_menu()
