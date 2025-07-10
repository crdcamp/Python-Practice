import os
import re

file_list = os.listdir('NumPy Random')

for filename in file_list:
    # Find all numbers in the filename
    numbers = re.findall(r'\d+', filename)
    
    new_filename = filename
    for i, number in enumerate(numbers, 1):
        # Replace each number with its position (count)
        new_filename = new_filename.replace(number, str(i), 1)  # Replace only first occurrence
    
    # Rename the file
    old_path = os.path.join('NumPy Random', filename)
    new_path = os.path.join('NumPy Random', new_filename)
    os.rename(old_path, new_path)
    print(f"Renamed: {filename} -> {new_filename}")