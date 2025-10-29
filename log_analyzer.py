import re

sampleLog = "auth.log"


def search_in_text():
    print(f"--------Reading the file: {sampleLog}----------")

    try:
        with open(sampleLog, "r") as log:
            for line in log:
                DateTime = re.findall(r'^[A-Z]{1}[a-z]{2} [1-30]+ ([00-60].){2}.[00-60]', line, flags=re.MULTILINE)
                Status = re.search()
                User = re.search()
                Ip = re.search()
                Port = re.search()
                Service = re.findall()

    except FileNotFoundError:
        print("[/] ERROR You must have the file on the same carpet of the scipt!!")

    print("End of file")


"""
def log_reconigzer():
    re.search("Failed")
    return
"""
