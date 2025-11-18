import re


sampleLog = "auth.log"


# A general class for the login attempt.
class LogEntry:
    # Defining the log-in class
    def __init__(self, raw_line_text):
        # In case the parser failes, default settings
        self.__Logn = "Log 0"
        self.__Date = "Jan 01 00:01:01"
        self.__User = "Default"
        self.__Status = "No-status"
        self.__Ip = "0.0.0.0"
        self.__Port = "0"
        self.__Service = "No reachable"
        # This build the values on every field
        self.__parse_the_line(raw_line_text)

    # The main function to build the values from the text
    def __parse_the_line(self, line):
        self.__Logn = "Log"
        # Dictionary to iterate for the searched value
        regexs = {
            '__Date': r'^[A-Z]{1}[a-z]{2} [0-9]{2} (?:[0-9]{2}.){2}[0-9]{2}',
            '__User': r'user ([a-z]+)',
            '__Status': r'.([A-Z][a-z]{1,15} [a-z]{1,})',
            '__Ip': r'(([0-9]{1,3}\.){3}[0-9]{1,3})',
            '__Port': r'port ([0-9]{1,5})',
            '__Service': r'([a-z]{1,6}[1-9]{1,5})$'
        }
        # Iterating on every attribute
        # and changing it values for the regexs search results
        for key, regex in regexs.items():
            match = re.search(regex, line)
            if match:
                # We try to get only the capture group of the regex
                try:
                    found_value = match.group(1)
                # If there was no capture group, then get all the line
                except IndexError:
                    found_value = match.group(0)
                setattr(self, key, found_value)
            else:
                # If there was no value, put the field as empty
                setattr(self, key, "Empty")

    # A safe way to get the attributes.

    # Get the date.
    def get_date(self):
        return self.__Date

    # Get the user.
    def get_user(self):
        return self.__User

    # Get the status.
    def get_status(self):
        return self.__Status

    # Get the ipu.
    def get_ip(self):
        return self.__Ip

    # Get the port.
    def get_port(self):
        return self.__Port

    # Get the service.
    def get_service(self):
        return self.__Service

    def get_all_attributes(self):
        return self.__Logn, self.__Date, self.__User, self.__Status, self.__Ip, self.__Port, self.__Service
