import re  # Required for pattern matching

def remove_elements_with_pattern(array, pattern):
    new_array = []
    for element in array:
        if pattern not in element:
            new_array.append(element)
        else:
            print("Removed: " + element)
    return new_array

# Open the input file and read lines into an array
input_filename = "lc.txt"
output_filename = "lc_problems.txt"
pattern_to_remove = "/solution"

with open(input_filename, "r") as file:
    arr = file.readlines()

# Remove lines containing the specified pattern
arr = remove_elements_with_pattern(arr, pattern_to_remove)

# Remove duplicate lines
arr = list(set(arr))

# Write the modified lines to the output file
with open(output_filename, 'a') as f:
    # Iterate over each line in your final list
    for line in arr:
        # Write each line to the file, followed by a newline
        f.write(line)

print("Total lines written to", output_filename, ":", len(arr))
