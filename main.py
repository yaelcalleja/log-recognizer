import re
from reader import search_in_text as look


def main():
    print("------------------------------------")
    print("[*] Welcome to the log analyzer [*]")
    print("------------------------------------")
    flag = input(
        "[?] Do you want me to analyze your log? \n[Press any key to continue or \"e\" to exit]: "
    )
    if flag == "e":
        flag = False
    else:
        flag = True
    while flag:
        print("[*] --------------------------------------------------------------------------------- [*]")
        print("[*] This script will create a dictionary with all the data... Pls wait a few seconds")
