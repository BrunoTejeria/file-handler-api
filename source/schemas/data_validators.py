import re

class Validators:
    """
    A class to handle validation of various types of data using regular expressions.
    """

    @staticmethod
    def validate_email(email: str) -> bool:
        """
        Validates an email address using a regular expression.

        Parameters:
        email (str): The email address to validate.

        Returns:
        bool: True if the email is valid, False otherwise.
        """
        return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

    @staticmethod
    def validate_ssid(ssid: str) -> bool:
        """
        Validates an SSID to ensure it only contains alphanumeric characters and is not longer than 32 characters.

        Parameters:
        ssid (str): The SSID to validate.

        Returns:
        bool: True if the SSID is valid, False otherwise.
        """
        return re.match(r"^[a-zA-Z0-9]{1,32}$", ssid) is not None

    class file:
        @staticmethod
        def basic(string: str) -> bool:
            """
            Checks if a given string contains any file path separators.

            Parameters:
            string (str): The string to check.

            Returns:
            bool: True if the string contains path separators, False otherwise.
            """
            return re.search(r"[./\\]", string)

        @staticmethod
        def txt(string: str) -> bool:
            """
            Checks if a given string does not end with '.txt'.

            Parameters:
            string (str): The string to check.

            Returns:
            bool: True if the string does not end with '.txt', False otherwise.
            """
            return string.endswith(".txt") is not True

        @staticmethod
        def size(size: bytes, file: bytes) -> bool:
            """
            Checks if the size of a given file does not exceed a specified limit.

            Parameters:
            - size (bytes): The maximum allowed size of the file.
            - file (bytes): The file content to check the size of.

            Returns:
            - bool: False if the file size is less the specified size, True otherwise.
            """
            return len(file) >= size