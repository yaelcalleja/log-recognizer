import re

sampleLog = "auth.log"


def read_the_text():
    print(f"--------Reading the file: {sampleLog}----------")

    try:
        with open(sampleLog, "r") as log:
            for line in log:
                print(line.strip())

    except FileNotFoundError:
        print("* ERROR You must have the file on the same carpet of the scipt!!")

    print("End of file")


"""
def log_reconigzer():
    re.search("Failed")
    return
"""
