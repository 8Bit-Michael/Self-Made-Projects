# This just opens up the CSV file and reads it:
import string
import csv
# This can be used to remove any type of puntuation from the text:
translator = str.maketrans('', '', string.punctuation)
filename = 'Analysis_Text.csv'
text = []
with open(filename, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        for cell in row:
            cleaned_text = cell.translate(translator).lower()
            text.extend(cleaned_text.split())

# Word frequency analysis:
each_word = []
counts = []

for word in text:
    if word in each_word:
        index = each_word.index(word)
        counts[index] += 1
    else:
        each_word.append(word)
        counts.append(1)

# Longest and shortest words analysis:
word_lengths = [len(word) for word in text]
word_lengths.sort()

# Average word length analysis:
average = sum(word_lengths) / len(text) if text else 0

print(f"""Your text has the following statistics:

Word frequencies - {dict(zip(each_word, counts))}

Longest to shortest words - {word_lengths}

Average word length - {average:.2f}""")