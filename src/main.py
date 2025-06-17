import json
import re

with open('mapping.json', 'r', encoding='utf-8') as f:
    mapping = json.load(f)
    
def get_words(sentence):
    return re.findall(r'\w+|[^\w\s]|\s+', sentence)

def tokenize_single_word(word, mapping, max_len=2):
    tokens = []
    i = 0
    n = len(word)
    while i < n:
        for length in range(max_len, 0, -1):
            piece = word[i:i+length]
            if piece in mapping:
                tokens.append(piece)
                i += length
                break
        else:
            piece = word[i] + 'a'
            tokens.append(piece)
            i += 1
    return tokens

def tokenize_many_words(words):
    tokens = []
    for word in words:
        if word.isalpha():
            token = tokenize_single_word(word, mapping, 6)  
            tokens.extend(token)
        else:
            tokens.append(word) 
    return tokens

def parse_tokens(tokens):
    parsed_tokens = []
    for token in tokens:
        if token in mapping:
            parsed_tokens.append(mapping[token])
        else:
            parsed_tokens.append(token)
    return parsed_tokens

def join_tokens(tokens):
    return ''.join(tokens)


def convert(sentence="kushal pathak"):
    #step 1: find all words
    sentence = sentence.lower()
    words = get_words(sentence)
    #step 2: tokenize each word
    roman_tokens = tokenize_many_words(words)
    #step 3: parse each tokens
    devnagari_tokens = parse_tokens(roman_tokens)
    #step 4: join each parsed tokens
    final_output = join_tokens(devnagari_tokens)
    #step 5: return joined value
    return {"roman_tokens":roman_tokens, "devnagari_tokens":devnagari_tokens, "devnagari":final_output}

while True:
    input_str = input("> ")
    if input_str.strip().lower() == "quit" or input_str.strip() == "":
        break
    output = convert(input_str)
    print("->",output["devnagari"]) 
    #print(output["roman_tokens"])    
    #print(output["devnagari_tokens"])    
       
