import typer
import re

def remove_non_letters(input_string):
    # Use a regular expression to remove non-letter characters
    cleaned_string = re.sub(r'[^a-zA-Z]', '', input_string)
    return cleaned_string


def custom_split_to_dict(input_string):
    values = input_string.split(',')
    result_dict = {}

    for index, value in enumerate(values):
        # Check if the value represents a dictionary
        if ':' in value:
            args = value.split(':')
            result_dict[remove_non_letters(args[0].strip())] = args[1::]
        # Check if the value represents a list
        elif '[' in value and ']' in value:
            result_dict[f'list_{index}'] = [item.strip() for item in value[1:-1].split(',')]
        else:
            result_dict[f'item_{index}'] = value.strip()

    return result_dict

app = typer.Typer()

json_file_dict = {}

# Read text data from a file into a string
def load_txt_data(file_path):
    try:
        with open(file_path, 'r') as file:
            text_data = file.read()
        return text_data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None


@app.command()
def json_parser_print(json_file:str):
    string = load_txt_data(json_file)
    # Split by ':'
    json_file_dict = custom_split_to_dict(string)
    
    print(json_file_dict)
    
@app.command()
def json_parser_val(key:str):
    try:
        string = load_txt_data(json_file)
    except:
        raise ImportError("Cannot find the file")
    try:
        return_val = dict()
        arr = "".join(string.split('"'))
        val = dict(arr)
        print(val)
    except:
        raise ValueError("Not proper json file")

        


if __name__ == "__main__":
    app()