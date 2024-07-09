# Content to write into the file
content = """\
This is a new text file.
It contains some lines of text.
Hello, world!
"""

# Specify the file path
file_path = 'new_file.txt'

# Open the file in write mode ('w')
with open(file_path, 'w') as file:
    # Write the content to the file
    file.write(content)

print(f"Content has been written to '{file_path}'.")
