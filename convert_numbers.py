"""
Convert Numbers

This program converts the numbers from a TXT input file 
into binary and hexadecimal and prints the results into a 
TXT output file

Author:
    Julia Gabriela Pinedo (A01795315)
"""
import sys
import time


class ConvertNumbers:
    """
    Class to convert numbers from a TXT input file
    """

    def __init__(self, file):
        """
        Initializes the ConvertNumbers object

        Returns:
            None
        """
        self.file_path = file
        self.total_lines = None

    def process_txt_file(self):
        """
        Reads the text file, processes the data, and inputs it into the
        'convert_numbers' function

        Returns:
            None
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()

                self.total_lines = self.lines_counter(lines)
                num_list = self.store_nums(lines)

                if num_list:
                    self.convert_numbers(num_list)

        except FileNotFoundError:
            print(f'File not found: {self.file_path}')

    @staticmethod
    def store_nums(lines):
        """
        Extracts and stores numerical values from the given list of lines

        Args:
            lines (list): List of lines from the TXT input file

        Returns:
            list: List of numerical values
        """
        num_list = []
        for line in lines:
            stripped_line = line.strip()
            if stripped_line:
                try:
                    num_in_line = int(stripped_line)
                    num_list.append(num_in_line)
                except ValueError:
                    print(f'Skipping invalid value: {stripped_line}')
            else:
                print(f'Skipping empty line: {stripped_line}')
        return num_list

    @staticmethod
    def lines_counter(lines):
        """
        This function counts the total number of lines in a TXT file
        before cleaning any non-valid values

        Args:
            lines (list): List of lines from the TXT input file

        Returns:
            int: Total number of lines in the list before cleaning
        """
        total_count = 0

        for _ in lines:
            total_count += 1
        return total_count

    @staticmethod
    def counter(counted_elements):
        """
        This function counts the total number of elements in an
        iterable object

        Args:
            counted_elements (iterable): An iterable object

        Returns:
            int: Total number of elements in the list or set
        """
        count = 0
        for _ in counted_elements:
            count += 1
        return count

    @staticmethod
    def abs_value(num_element):
        """
        This function returns the absolute value of a given
        number

        Args:
            num_element (int|float): Number to be converted

        Returns:
            The absolute value of the number
        """
        return -num_element if num_element < 0 else num_element

    @staticmethod
    def invert_bits_of_binary_number(bin_input):
        """
        This function is used to invert the bits of a given binary number

        Args:
            bin_input (str): The binary number

        Returns:
            str: The inverted binary number
        """
        inverted_bin = ''
        for bit in '0' + bin_input:
            inverted_bin += '0' if bit == '1' else '1'
        return inverted_bin

    def binary_addition(self, inverted_bin):
        """
        This function is used to increment 1 to the LSB of the given inverted
        binary number

        Args:
            inverted_bin (str): The binary number

        Returns:
            str: The result of the addition
        """
        max_len = self.counter(inverted_bin)
        carry = 1
        bin_add = ''

        for i in range(max_len - 1, -1, -1):
            bit_sum = carry + int(inverted_bin[i])
            bin_add = str(bit_sum % 2) + bin_add
            carry = bit_sum // 2

        while self.counter(bin_add) < 10:
            bin_add = '1' + bin_add
        return bin_add

    def twos_complement_of_binary_number(self, bin_input):
        """
        This function obtains the 2's complement of a binary number

        Args:
            bin_input (str): The binary number

        Returns:
            str: The 2's complement of the given binary number
        """
        inverted_binary = self.invert_bits_of_binary_number(bin_input)
        incremented_binary = self.binary_addition(inverted_binary)
        return incremented_binary

    def dec_to_bin_converter(self, input_num):
        """
        This function converts a decimal number into a binary representation

        Args:
            input_num (int): The decimal number to be converted

        Returns:
            str: The binary representation of the decimal number
        """
        if input_num < 0:
            invert_binary = True
            input_num = self.abs_value(input_num)
        else:
            invert_binary = False

        bin_num = ''
        while True:
            if input_num == 0:
                break
            if (input_num % 2) == 0:
                input_num = input_num // 2
                bin_num = '0' + bin_num
            else:
                input_num = input_num // 2
                bin_num = '1' + bin_num
        if invert_binary:
            bin_num = self.twos_complement_of_binary_number(bin_num)
        return bin_num

    def positive_bin_to_hex_converter(self, binary_str):
        """
        This function converts a positive binary string into
        its hexadecimal representation

        Args:
            binary_str (str): The positive binary representation to be converted

        Returns:
            str: The hexadecimal representation of the binary string
        """
        bin_transformed = binary_str.zfill((self.counter(binary_str) + 3) // 4 * 4)

        hex_dict = {
            '0000': '0',
            '0001': '1',
            '0010': '2',
            '0011': '3',
            '0100': '4',
            '0101': '5',
            '0110': '6',
            '0111': '7',
            '1000': '8',
            '1001': '9',
            '1010': 'A',
            '1011': 'B',
            '1100': 'C',
            '1101': 'D',
            '1110': 'E',
            '1111': 'F'
        }

        hex_digit = \
            [hex_dict[bin_transformed[i:i + 4]] for i in range(0, self.counter(bin_transformed), 4)]
        hex_num = ''.join(hex_digit)
        return hex_num

    def negative_bin_to_hex_converter(self, binary_str):
        """
        This function converts a negative binary string into
        its hexadecimal representation

        Args:
            binary_str (str): The negative binary representation to be converted

        Returns:
            str: The hexadecimal representation of the binary string
        """
        hex_digits = '0123456789ABCDEF'

        while self.counter(binary_str) % 40 != 0:
            binary_str = '1' + binary_str

        hex_num = ''

        for i in range(0, self.counter(binary_str), 4):
            nibble = binary_str[i:i + 4]
            dec_value = int(nibble, 2)
            hex_num += hex_digits[dec_value]
        return hex_num

    def dec_to_bin_to_hex_converter(self, input_num):
        """
        This function converts a decimal number into a binary
        and its hexadecimal representation

        Args:
            input_num (int): The decimal number to be converted

        Returns:
            str: The hexadecimal representation of the decimal number
        """
        dec_transformed = self.dec_to_bin_converter(input_num)

        if input_num >= 0:
            hex_num = self.positive_bin_to_hex_converter(dec_transformed)
        else:
            hex_num = self.negative_bin_to_hex_converter(dec_transformed)
        return hex_num

    def convert_numbers(self, num_list):
        """
        This function takes the input list of numbers from the TXT file
        and calculates its statistics

        Args:
            num_list (list): The list of numbers from the TXT file

        Returns:
            int|float: The statistics of the input list of numbers
        """
        start_time = time.time()

        output_initial_count = self.total_lines
        output_cleaned_count = self.counter(num_list)
        removed_elements = output_initial_count - output_cleaned_count

        with open('ConvertionResults.txt', 'w', encoding='utf-8') as file:
            for number in num_list:
                if number == 0:
                    binary_transformation = '0'
                    hex_transformation = '0'
                else:
                    binary_transformation = self.dec_to_bin_converter(number)
                    hex_transformation = self.dec_to_bin_to_hex_converter(number)
                print(f'Decimal: {number}, Binary: {binary_transformation}, '
                      f'Hex: {hex_transformation}\n')
                file.write(f'Decimal: {number}, Binary: {binary_transformation}, '
                           f'Hex: {hex_transformation}\n')

        end_time = time.time()

        print(f'\n\nTotal Initial Count: {output_initial_count}')
        print(f'\nRemoved a total of {removed_elements} elements')
        print(f'\nElapsed Time: {end_time - start_time} s')

        with open('ConvertionResults.txt', 'a', encoding='utf-8') as file:
            file.write(f'\n\nTotal Initial Count: {output_initial_count}')
            file.write(f'\nRemoved a total of {removed_elements} elements\n')
            file.write(f'\nElapsed Time: {end_time - start_time} s')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python3 convert_numbers.py <file_path>')
    else:
        file_path = sys.argv[1]
        data_processor = ConvertNumbers(file_path)
        data_processor.process_txt_file()
