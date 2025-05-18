# your code goes here!
import re

class EmailAddressParser:
    def __init__(self,addresses):
        self.addresses = addresses

    def parse(self):

        given_email = re.split(r'[,\s]+', self.addresses.strip())

        email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]+$')
        filtered_emails = filter(email_pattern.fullmatch,given_email)

        unique_address = sorted(set(filtered_emails))
        return unique_address