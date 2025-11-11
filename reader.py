import re

sampleLog = "auth.log"

# A general class for the login attempt.


class log:
    # Defining the principal data from the log-in
    def __init__(self, Logn, Date, User, Status, Ip, Port, Services):
        self.__Logn = "Log 0"
        self.__Date = "Jan 01 00:01:01"
        self.__User = "Default"
        self.__Status = "No-status"
        self.__Ip = "0.0.0.0"
        self.__Port = "0"
        self.__Services = "No reachable"

    # A safe way to get the information of the attributes.
    def getatributes(self):
        return self.__Logn, self.__Date, self.__User, self.__Status, self.__Ip, self.__Port, self.__Services

    # To change any attribute from a secure way.
    def setattribute(self):
        pass

# To search for regex and create a list with each log try
# this function search line by line the


def regex(r, i):
    return re.findall(r, i)

# Creating a list with all the data of the search_in_text function.


def list_log(listed, dat1, dat2, dat3, dat4, dat5, dat6):
    listed.extend(dat1)
    listed.extend(dat2)
    listed.extend(dat3)
    listed.extend(dat4)
    listed.extend(dat5)
    listed.extend(dat6)
    return listed


def search_in_text(logs=[], n=0):
    # We need the text exist on the carpet
    # so we gave the instruction to comprobe it
    try:
        # If there is a file to read, we go line by line searcching for regex
        with open(sampleLog, "r") as log:
            for line in log:
                # We search for the date and time of the executed log.
                DateTime = re.findall(
                    r'^[A-Z]{1}[a-z]{2} [0-9]{2} (?:[0-9]{2}.){2}[0-9]{2}',
                    line, flags=re.MULTILINE
                )
                # This is the second relevant data, the attempt under the log.
                Status = regex(r'.[A-Z][a-z]{1,15} [a-z]{1,}', line)
                # Finding the user.
                User = regex(r'user [a-z]{1,}', line)
                # Looking for the ip of the attempt machine
                Ip = regex(r'(?:[0-9]{1,3}\.){3}[0-9]{1,3}', line)
                # Which port they use to try the attempt
                Port = regex(r'port [0-9]{1,5}', line)
                # And which service was executing that port.
                Service = regex(r'(?:[a-z]{1,6}[1-9]{1,5})$', line)
                # Creating a list with every log field
                list_log(logs, DateTime, User, Status, Ip, Port, Service)
                # Putting all logs on a dictionary
                numberLog = "log" + str(n+1)
                dicLogs = {
                    numberLog: logs
                }
                return dicLogs
    except FileNotFoundError:
        print(
            "[/] ERROR You must have the file on the same carpet of the scipt"
        )

    print("End of file")


print(search_in_text())
