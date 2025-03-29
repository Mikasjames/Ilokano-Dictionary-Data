import re
from raw import input_text
from extract import text_to_json

def is_new_word(line):
    return bool(re.match(r'^(?!--)[1-9]?[A-Z-]+(?!\.)(?=[^a-z]|$)', line))

def is_page_number_or_title(line):
    return bool(re.match(r'^\d+$', line)) or line.strip() == "ILOKANO DICTIONARY"

def parse_dictionary(text):
    dictionary = {}
    current_word = None
    current_definition = []
    is_syn_or_ant = False

    def add_to_dictionary(word, definition):
        if word not in dictionary:
            dictionary[word] = []
        dictionary[word].append(' '.join(definition).strip())

    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or is_page_number_or_title(line):
            continue

        while is_syn_or_ant:
            current_definition[-1] += ' '
            gotcha_word = ''
            for letter in line:
                if letter != '.':
                    current_definition[-1] += letter
                    gotcha_word += letter
                else:
                    is_syn_or_ant = False
                    gotcha_word += '.'
                    line = line[len(gotcha_word):].strip()
                    break

        if is_new_word(line):
            if current_word and current_definition:
                add_to_dictionary(current_word, current_definition)

            match = re.match(r'^([1-9])?([A-Z-]+)', line)
            current_word = match.group(2)
            current_definition = []

            remainder = line[len(match.group(0)):].strip()
            if remainder:
                if (remainder.startswith(', ')):
                    remainder = remainder[2:]
                current_definition.append(remainder)

        elif line.startswith(('n.', 'v.', 'adj.', 'adv.')):
            if current_definition:
                add_to_dictionary(current_word, current_definition)
            current_definition = [line]

        else:
            current_definition.append(line)

        found = re.findall(r'--(syn\.|var\.|ant\.|cf\.)', line)
        found = [f'--{match}' for match in found]

        if found and '.' not in line.strip().split(found[-1])[1]:
            is_syn_or_ant = True

    if current_word and current_definition:
        add_to_dictionary(current_word, current_definition)

    return dictionary

def yield_jsonized_dictionary(text):
    ilokano_dict = parse_dictionary(text)
    jsonized_ilokano_dict = {}

    for word, definitions in ilokano_dict.items():
        definitions_str = ' '.join(definitions)
        jsonized_ilokano_dict[word] = text_to_json(definitions_str)

    return jsonized_ilokano_dict

if __name__ == '__main__':
    print(yield_jsonized_dictionary(input_text))
