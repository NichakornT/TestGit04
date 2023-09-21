def reduce_to_20_characters(original_text):
    substitution_table = {
        'aa': 'A', 'ab': 'B', 'ac': 'C', 'ad': 'D',
        'ba': 'E', 'bb': 'F', 'bc': 'G', 'bd': 'H',
        'ca': 'I', 'cb': 'J', 'cc': 'K', 'cd': 'L',
        'da': 'M', 'db': 'N', 'dc': 'O', 'dd': 'P'
    }
    reduced_text = ''

    for i in range(0, len(original_text), 2):
        pair = original_text[i:i + 2]
        if pair in substitution_table:
            reduced_text += substitution_table[pair]

    return reduced_text


def convert_to_original(reduced_text):
    reverse_substitution_table = {
        'A': 'aa', 'B': 'ab', 'C': 'ac', 'D': 'ad',
        'E': 'ba', 'F': 'bb', 'G': 'bc', 'H': 'bd',
        'I': 'ca', 'J': 'cb', 'K': 'cc', 'L': 'cd',
        'M': 'da', 'N': 'db', 'O': 'dc', 'P': 'dd'
    }
    original_text = ''

    for char in reduced_text:
        if char in reverse_substitution_table:
            original_text += reverse_substitution_table[char]

    return original_text


# Example:
def run():
    original_text = "abcadacddcacababbcadcbadcbabcdcaacbcabda"
    reduced_text = reduce_to_20_characters(original_text)
    converted_text = convert_to_original(reduced_text)

    print("Original Text:", original_text)
    print("Reduced Text:", reduced_text)
    print("Converted Text:", converted_text)
    print("Number of original text:", len(original_text))
    print("Number of characters reduced:", len(reduced_text))