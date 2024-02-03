"""
Word Count

This program counts the words from a TXT input file and
prints the obtained count into a TXT output file

Author:
    Julia Gabriela Pinedo (A01795315)
"""
import sys
import time


class WordCount:
    """
    Class to convert numbers from a TXT input file
    """

    def __init__(self, file):
        """
        Initializes the WordCount object

        Returns:
            None
        """
        self.file_path = file
        self.total_lines = None

    def process_txt_file(self):
        """
        Reads the text file, processes the data, and inputs it into the
        'word_count' function

        Returns:
            None
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()

                self.total_lines = self.lines_counter(lines)
                word_list = self.store_words(lines)

                if word_list:
                    self.word_count(word_list)

        except FileNotFoundError:
            print(f'File not found: {self.file_path}')

    @staticmethod
    def store_words(lines):
        """
        Extracts and stores numerical values from the given list of lines

        Args:
            lines (list): List of lines from the TXT input file

        Returns:
            list: List of numerical values
        """
        word_list = []
        for line in lines:
            stripped_line = line.strip()
            if stripped_line:
                try:
                    word_list.append(stripped_line)
                except ValueError:
                    print(f'Skipping invalid value: {stripped_line}')
            else:
                print(f'Skipping empty line: {stripped_line}')
        return word_list

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
    def count_items(iterable):
        """
        This function to pair a counter object and return a list
        of tuples

        Args:
            iterable (iterable): An iterable object

        Returns:
            A list of tuples
        """
        counted = []
        for item in iterable:
            counted.append((item, iterable[item]))
        return counted

    @staticmethod
    def word_counter(word_list):
        """
        This function counts the occurrences of each word in a list

        Args:
            word_list (list): A list of words

        Returns:
            dict: A dictionary where each key is a word and each value is
            the corresponding count of each word
        """
        word_counts = {}

        for word in word_list:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
        return word_counts

    def word_count(self, word_list):
        """
        This function takes the input list of numbers from the TXT file
        and calculates its statistics

        Args:
            word_list (list): The list of numbers from the TXT file

        Returns:
            int|float: The statistics of the input list of numbers
        """
        start_time = time.time()

        output_initial_count = self.total_lines
        output_cleaned_count = self.counter(word_list)
        removed_elements = output_initial_count - output_cleaned_count
        counter_output = self.word_counter(word_list)

        with open('WordCountResults.txt', 'w', encoding='utf-8') as file:
            for word, count in self.count_items(counter_output):
                print(f'Word: {word}, Count: {count}\n')
                file.write(f'Word: {word}, Count: {count}\n')

        end_time = time.time()

        print(f'\n\nTotal Initial Count: {output_initial_count}')
        print(f'\nRemoved a total of {removed_elements} elements')
        print(f'\nElapsed Time: {end_time - start_time} s')

        with open('WordCountResults.txt', 'a', encoding='utf-8') as file:
            file.write(f'\n\nTotal Initial Count: {output_initial_count}')
            file.write(f'\nRemoved a total of {removed_elements} elements')
            file.write(f'\nElapsed Time: {end_time - start_time} s')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python3 convert_numbers1.py <file_path>')
    else:
        file_path = sys.argv[1]
        data_processor = WordCount(file_path)
        data_processor.process_txt_file()
