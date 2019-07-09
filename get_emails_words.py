import os
import nltk
print(os.listdir("../input"))
path = '../input/fradulent_emails.txt'

def parse_raw_message(raw_message):
    lines = raw_message.split('\n')
    email = {}
    message = ''
    keys_to_extract = ['from', 'to']
    for line in lines:
        if ':' not in line:
            message += line.strip()
            email['body'] = message
        else:
            pairs = line.split(':')
            key = pairs[0].lower()
            val = pairs[1].strip()
            if key in keys_to_extract:
                email[key] = val
    return email

with open(path, mode= 'r', errors='ignore') as f:
    mail_list = f.read().split('From')
    tokens = []
    print(len(mail_list)) 
    for i, x in enumerate(mail_list):
        print(i+1)
        raw_message = parse_raw_message('from:' + x.lower()).get('body')
        if raw_message is not None:
            untagged = nltk.word_tokenize(raw_message)
            tagged = nltk.pos_tag(untagged)
            for term, pos in tagged:
                if len(term) > 2 and pos in ['JJ', 'NN',"NNP"]:
                    tokens.append(term)
    freq = nltk.FreqDist(tokens)
    print(freq.most_common(1000))


