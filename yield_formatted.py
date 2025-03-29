from yield_json import yield_jsonized_dictionary
from raw import input_text

# Print the organized dictionary
for word, definitions in yield_jsonized_dictionary(input_text).items():
    print(f"Word: {word}")
    print("Definitions:")
    for i, definition in enumerate(definitions, 1):
        print(f"\t{i}. {definition}")
    print()