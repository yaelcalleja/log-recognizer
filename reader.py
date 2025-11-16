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
        self.__Services = "No reachable"
        # This build the values on every field
        self.__parse_the_line(raw_line_text)

    # The main function to build the values from the text
    def __parse_the_line(self, line):
        self.__Logn = "Log"
        # Dictionary to iterate for the searched value
        regexs = {
            '__Date': r'^[A-Z]{1}[a-z]{2} [0-9]{2} (?:[0-9]{2}.){2}[0-9]{2}',
            '__User': r'user [a-z]+',
            '__Status': r'.([A-Z][a-z]{1,15} [a-z]{1,})2',
            '__Ip': r'([0-9]{1,3}\.){3}[0-9]{1,3}',
            '__Port': r'port ([0-9]{1,5})',
            '__Service': r'([a-z]{1,6}[1-9]{1,5})$'
        }
        # Iterating on every attribute
        # and changing it value for the regex search results
        for key, regex in regexs:
            match = re.search(regex, line)
            if match:
                # Because we have more than 1 posible group
                # on our search, we try to get only the value.
                try:
                    found_value = match.group(1)
                # If there was no value on the second group of the search
                # Then try to get the first one
                except IndexError:
                    found_value = match.group(0)
                setattr(self, key, found_value)
            else:
                # If there was no value, put the field as empty
                setattr(self, key, "Empty")

    # A safe way to get the attributes.
    def getatributes(self):
        return self.__Logn, self.__Date, self.__User, self.__Status, self.__Ip, self.__Port, self.__Services
