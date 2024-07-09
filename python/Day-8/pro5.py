def count_words_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            lines = text.splitlines()
            words = text.split()

        num_lines = len(lines)
        num_words = len(words)

        print(f"Number of lines: {num_lines}")
        print(f"Number of words: {num_words}")

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
file_path = 'C:\python\Day-8\simple.txt'  
count_words_lines(file_path)
