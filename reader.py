import re

sampleLog = "auth.log"


def search_in_text():
    print(f"------------------Reading the file: {sampleLog}--------------------")

    try:
        with open(sampleLog, "r") as log:
            for line in log:
                DateTime = re.findall(
                    r'^[A-Z]{1}[a-z]{2} [1-3][0-9] (?:[0-5][0-9].){2}[0-5][0-9]',
                    line, flags=re.MULTILINE
                )
                Status = re.findall(
                    r'.[A-Z][a-z]{1,15} [a-z]{1,}',
                    line
                )
                User = re.findall(
                    r'user [a-z]{1,}',
                    line
                )
                Ip = re.findall(
                    r'(?:[0-9]{1,3}\.){3}[0-9]{1,3}',
                    line
                )
                Port = re.findall(
                    r'port [0-9]{1,5}',
                    line
                )
                Service = re.findall(
                    r'(?:[a-z]{1,6}[1-9]{1,5})$',
                    line
                )
        return DateTime, Status, User, Ip, Port, Service
    except FileNotFoundError:
        print(
            "[/] ERROR You must have the file on the same carpet of the scipt"
        )

    print("End of file")


print(search_in_text())
