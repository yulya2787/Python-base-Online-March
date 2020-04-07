def get_text(text):
    with open(text, 'r') as file:
        pretext = file.read()
    return pretext


def text_output(text_output, file_name):
    with open(file_name, 'a') as new_file:
        new_file.write(str(text_output))