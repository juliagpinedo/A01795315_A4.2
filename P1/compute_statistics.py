"""
Compute Statistics

This program computes descriptive statistics from a
TXT input file containing numbers and prints the
results into a TXT output file

Author:
    Julia Gabriela Pinedo (A01795315)
"""
import sys
import time


class ComputeStatistics:
    """
    Class to compute statistics from a TXT input file
    """

    def __init__(self, file):
        """
        Initializes the ComputeStatistics object

        Returns:
            None
        """
        self.file_path = file
        self.total_lines = None

    def process_txt_file(self):
        """
        Reads the text file, processes the data, and inputs it into the
        'compute_statistics' function

        Returns:
            None
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()

                self.total_lines = self.lines_counter(lines)
                num_list = self.store_nums(lines)

                if num_list:
                    self.compute_statistics(num_list)

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
                    num_in_line = float(stripped_line)
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
    def adder(added_elements):
        """
        This function adds the elements of an iterable object

        Args:
            added_elements (iterable): An iterable object

        Returns:
            int|float: The result of the addition
        """
        result = 0
        for element in added_elements:
            result += element
        return result

    @staticmethod
    def setting(iterable):
        """
        This function creates a set from the given iterable object

        Args:
            iterable (iterable): An iterable object

        Returns:
            set: The set of the unique elements from the iterable
        """
        elements = []
        for element in iterable:
            if element not in elements:
                elements.append(element)
        return elements

    @staticmethod
    def mapping(func, iterable):
        """
        This function applies the given function to each element
        of a given iterable object

        Args:
            func: The function to apply to the elements
            iterable (iterable): An iterable object

        Returns:
            A list containing the results of applying the function to each
            element
        """
        return [func(element) for element in iterable]

    def sorter(self, iterable, key=None, reverse=False):
        """
        This function returns a sorted list from the elements
        of the given iterable object

        Args:
            iterable (iterable): An iterable object
            key: A function to extract a comparison key from each
            element. Default is None
            reverse (bool): Indicates whether to sort in descending
            order. Default is False

        Returns:
            A sorted list containing the sorted elements from the iterable
        """
        elements = list(iterable)

        n = self.counter(elements)
        for i in range(n):
            for j in range(0, n - i - 1):
                compare_value_j = elements[j] if key is None else key(elements[j])
                compare_value_j_plus_1 = elements[j + 1] if key is None else key(elements[j + 1])

                if (reverse and compare_value_j < compare_value_j_plus_1) or \
                        (not reverse and compare_value_j > compare_value_j_plus_1):
                    elements[j], elements[j + 1] = elements[j + 1], elements[j]
        return elements

    def calculate_mean(self, num_list):
        """
        This function takes a list of numbers and calculates their mean

        Args:
            num_list (list): A list of numbers

        Returns:
            int|float: The mean of the numbers
        """
        mean_val = self.adder(num_list) / self.counter(num_list)
        return int(mean_val) if mean_val == int(mean_val) else mean_val

    def calculate_median(self, num_list):
        """
        This function takes a list of numbers and calculates their median

        Args:
            num_list (list): A list of numbers

        Returns:
            int|float: The median of the numbers
        """
        sorted_list = self.sorter(num_list)
        n = self.counter(sorted_list)
        mid_index_1 = n // 2
        mid_index_2 = (n - 1) // 2
        even_num_median = (sorted_list[mid_index_1] + sorted_list[mid_index_2]) / 2
        return even_num_median if n % 2 == 0 else sorted_list[mid_index_1]

    def calculate_mode(self, num_list):
        """
        This function takes a list of numbers and calculates their mode

        Args:
            num_list (list): A list of numbers

        Returns:
            int|float|str|None:
            If there is only one number with the highest mode, returns that number as
            integer or float,
            If there are multiple numbers with the highest mode, returns them as a string
            separated by commas
            If all numbers have the same mode, returns None
        """
        sorted_nums = self.sorter(num_list)
        max_freq = max(sorted_nums.count(num) for num in self.setting(sorted_nums))
        mode_nums = [num for num in self.setting(sorted_nums) if sorted_nums.count(num) == max_freq]
        if self.counter(self.setting(sorted_nums.count(num) for num in sorted_nums)) == 1:
            return 'N/A'
        return mode_nums[0] if self.counter(mode_nums) == 1 else ', '.join(self.mapping(str,
                                                                                        mode_nums))

    def calculate_variance(self, num_list):
        """
        This function takes a list of numbers and calculates their variance

        Args:
            num_list (list): The list of numbers

        Returns:
            float: The variance of the list
        """
        calc_mean = self.calculate_mean(num_list)
        return self.adder((x - calc_mean) ** 2 for x in num_list) / self.counter(num_list)

    def calculate_stddev(self, num_list):
        """
        This function takes a list of numbers and calculates their standard deviation

        Args:
            num_list (list): A list of numbers

        Returns:
            float: The standard deviation of the list
        """
        get_variance = self.calculate_variance(num_list)
        return get_variance ** 0.5

    def compute_statistics(self, num_list):
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
        output_mean = self.calculate_mean(num_list)
        output_median = self.calculate_median(num_list)
        output_mode = self.calculate_mode(num_list)
        output_variance = self.calculate_variance(num_list)
        output_stddev = self.calculate_stddev(num_list)

        end_time = time.time()

        print('\nDescriptive Statistics Results:')
        print(f'\nTotal Initial Count: {output_initial_count}')
        print(f'\nRemoved a total of: {removed_elements} elements')
        print(f'\nMean: {output_mean}')
        print(f'\nMedian: {output_median}')
        print(f'\nMode: {output_mode}')
        print(f'\nVariance: {output_variance}')
        print(f'\nStandard Deviation: {output_stddev}\n')
        print(f'\nElapsed Time: {end_time - start_time} s')

        with open('StatisticsResults.txt', 'w', encoding='utf-8') as file:
            file.write('Descriptive Statistics Results:')
            file.write(f'\nTotal Initial Count: {output_initial_count}')
            file.write(f'\nRemoved a total of: {removed_elements} elements')
            file.write(f'\nMean: {output_mean}')
            file.write(f'\nMedian: {output_median}')
            file.write(f'\nMode: {output_mode}')
            file.write(f'\nVariance: {output_variance}')
            file.write(f'\nStandard Deviation: {output_stddev}\n')
            file.write(f'\nElapsed Time: {end_time - start_time} s')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python3 compute_statistics.py <file_path>')
    else:
        file_path = sys.argv[1]
        data_processor = ComputeStatistics(file_path)
        data_processor.process_txt_file()
