import re

class Regex:
    """
    A class to handle regular expressions.
    """
    @staticmethod
    def validate_email(email: str) -> bool:
        """
        Validates an email address.
        """
        return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

    @staticmethod
    def validate_ssid(ssid: str) -> bool:
        """
        Validates an SSID.
        """
        return re.match(r"^[a-zA-Z0-9]{1,32}$", ssid) is not None

    class file:
        @staticmethod
        def basic(string: str) -> bool:
            return re.search(r"[./\\]", string) and re.search(r"[./\\]", string)

        
