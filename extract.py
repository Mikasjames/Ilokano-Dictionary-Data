import re

def split_entry(text):
    pattern = r'(?:^|\s)(n\.|v\.|adj\.|adv\.|interj\.)\s|(\[.*?\])|(\/[^\/\n]+\/)|(/[^/\s]+(?::[^/\s]+)?)'

    parts = [part for part in re.split(pattern, text) if part and not part.isspace() and part != ',']
    return parts

def text_to_json(text):
    entries = []
    current_common_form = ''
    current_origin = ''
    current_plural_form = ''
    current_conjugation_note = ''
    current_conjugation = ''

    parts = split_entry(text)

    current_pos = ''
    for part in parts:
        if part.strip().startswith('='):
            current_origin = part.lstrip('= ').strip()
        elif re.search(r'\[.*?]', part):
            bracket_item = re.search(r'\[.*?]', part).group(0).strip('[]')
            if bracket_item.startswith('pl.'):
                current_plural_form = bracket_item
            elif bracket_item.startswith('with'):
                current_conjugation_note = bracket_item
            else:
                current_origin = bracket_item
        elif part.strip() in ['n.', 'v.', 'adj.', 'adv.', 'interj.']:
            current_pos = part.strip()
        elif part.strip().startswith('/'):
            current_conjugation = part.strip()
        elif part.strip().isupper() and current_conjugation and not current_conjugation.endswith('/'):
            current_conjugation += ' ' + part.strip()
        elif part.strip().isupper() or part.strip().startswith('or') and not part.strip().startswith('/'):
            current_common_form += part.strip('; ')
        elif part.strip():
            definitions = re.split(r'(?<=[.]) (?=/)', part)
            for definition in definitions:
                if definition.startswith(','):
                    definition = definition[1:].strip()
                def_entry = {
                    'part_of_speech': current_pos,
                    'definition': '',
                    'eng_example': '',
                    'ilok_example': '',
                    'conjugation': '',
                    'origin': '',
                    'synonyms': [],
                    'antonyms': [],
                    'variations': [],
                    'cross_reference': '',
                    'common_forms': [],
                    'plural_form': '',
                }

                if current_origin:
                    def_entry['origin'] = current_origin
                    definition = definition.replace(f'[{current_origin}]', '').strip()
                    current_origin = ''

                if current_common_form:
                    def_entry['common_forms'].append(current_common_form.strip(',. '))
                    definition = definition.replace(f'{current_common_form}', '').strip()
                    current_common_form = ''

                if current_plural_form:
                    def_entry['plural_form'] = current_plural_form
                    current_plural_form = ''

                if current_conjugation:
                    def_entry['conjugation'] = current_conjugation
                    current_conjugation = ''

                found = re.split(r'--\s?(syn\.|var\.|ant\.)', definition)
                if len(found) > 1:
                    definition = found.pop(0).strip()
                    current_relation = ''
                    for item in found:
                        if item.startswith('syn.'):
                            current_relation = 'synonyms'
                        elif item.startswith('var.'):
                            current_relation = 'variations'
                        elif item.startswith('ant.'):
                            current_relation = 'antonyms'
                        else:
                            def_entry[current_relation].append(item.strip(',. '))
                            current_relation = ''

                parts = re.split(r'(?<=[.?]) (?=[A-Z])', definition)

                if parts:
                    def_entry['definition'] = parts[0].strip()
                    if len(parts) > 1:
                        def_entry['ilok_example'] = parts[1].strip()
                    if len(parts) > 2:
                        def_entry['eng_example'] = parts[2].strip()

                if '[' in def_entry['conjugation'] and ']' in def_entry['conjugation']:
                    usage_parts = def_entry['conjugation'].split('[', 1)
                    def_entry['conjugation'] = usage_parts[0].strip()
                    def_entry['usage'] = '[' + usage_parts[1].strip()

                if current_conjugation_note:
                    if def_entry['conjugation']:
                        def_entry['conjugation'] += ' ' + current_conjugation_note
                        current_conjugation_note = ''
                    else:
                        def_entry['definition'] = f'[{current_conjugation_note}]' + ' ' + def_entry['definition']
                        current_conjugation_note = ''

                entries.append(def_entry)

    if current_origin and not entries:
        entries.append({
            'part_of_speech': '',
            'definition': '',
            'eng_example': '',
            'ilok_example': '',
            'conjugation': '',
            'origin': current_origin,
            'synonyms': [],
            'antonyms': [],
            'variations': [],
            'cross_reference': '',
            'common_forms': [],
            'plural_form': '',
        })

    return entries