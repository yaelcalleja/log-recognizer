import re

sampleLog = "auth.log"


# To create a dictionary with all the data assigned to a log"n" key
# We're going to put all the values generated for the reader function
# on a log key
# This function will be called later on the search_in_text function.

def dictioner(list, n=1):
    # Making the key value with the log number
    numberLog = 'log' + str(n)
    # Adding the information to the key
    dictonaryLog = {
            numberLog: list,
    }
    return dictonaryLog, n + 1


# To search for regex and create a list with each log try
# this function search line by line the


def search_in_text(logs=[]):
    print(f"------------------Reading the file: {sampleLog}--------------------")
    # We need the text exist on the carpet
    # so we gave the instruction to comprobe it
    try:
        # If there is a file to read, we go line by line searcching for regex
        with open(sampleLog, "r") as log:
            for line in log:
                # We've search for the date and time of the executed log.
                # Ex; Oct 27 09:25:01
                DateTime = re.findall(
                    r'^[A-Z]{1}[a-z]{2} [1-3][0-9] (?:[0-5][0-9].){2}[0-5][0-9]',
                    line, flags=re.MULTILINE
                )
                # This is the second relevant data, the attempt under the log.
                # Ex; failed password
                Status = re.findall(
                    r'.[A-Z][a-z]{1,15} [a-z]{1,}',
                    line
                )
                # Finding the user.
                # Ex; root
                User = re.findall(
                    r'user [a-z]{1,}',
                    line
                )
                # Looking for the ip of the attempt machine
                # Ex; 197.1.205.25
                Ip = re.findall(
                    r'(?:[0-9]{1,3}\.){3}[0-9]{1,3}',
                    line
                )
                # Which port they use to try the attempt
                # Ex ; Port 22
                Port = re.findall(
                    r'port [0-9]{1,5}',
                    line
                )
                # And which service was executing that port.
                # Ex; ssh22
                Service = re.findall(
                    r'(?:[a-z]{1,6}[1-9]{1,5})$',
                    line
                )
                # Creating a list for every log field
                logs.extend(DateTime)
                logs.extend(User)
                logs.extend(Status)
                logs.extend(Ip)
                logs.extend(Port)
                logs.extend(Service)
                # Putting all logs on a dictionary
                dictioner(logs)
        return dictionaryLog
    except FileNotFoundError:
        print(
            "[/] ERROR You must have the file on the same carpet of the scipt"
        )

    print("End of file")


print(search_in_text())
