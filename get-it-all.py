import os
from bs4 import BeautifulSoup
import nltk


def get_all_filenames(folder_name):
    """given a directory, return the filenames in it"""
    texts = []
    for (root, _, files) in os.walk(folder_name):
        for fn in files:
            path = os.path.join(root, fn)
            texts.append(path)
    return texts


def get_a_review_text(filename):
    """given a filename, use BeautifulSoup to get the text of the 10 reviews in it.
    Should be ten reviews"""
    with open(filename, 'rb') as file_input:
        ready_to_process = file_input.read()
        soup = BeautifulSoup(ready_to_process, 'lxml')
        reviews_html = soup.find_all('span', attrs={'class':'a-size-base review-text'})
        review_texts = [result.text for result in reviews_html]
    return review_texts

def save_each_file(corpus_output_folder, filename, text, counter):
    """given a filename and text, save the text of that review in a file"""
    # we're going to use the counter to give unique filenames as we we rip
    # through the corpuse folder.
    with open(corpus_output_folder + '/' + filename + '' + str(counter) + '.txt', 'w') as fout:
        fout.write(text)


def analyze_text(text):
    """given the text of a review, lowercase it and search for the words"""
    tokens = nltk.word_tokenize(text)
    lowercase_tokens = [token.lower() for token in tokens]
    return lowercase_tokens

corpus_input_folder = NEEDS_TO_BE_DEFINED_HERE
corpus_output_folder = NEEDS_TO_BE_DEFINED_HERE

# this will give you a list of all filenames in your corpus folder, at least in
# theory. I don't have the corpus to test it on
all_filenames = get_all_filenames(corpus_input_folder)
all_review_texts = []
corpus_tokens = []
counter = 0

for filename in all_filenames:
    # we're using .extend here and not .append, because get_a_review_text is
    # going to give us a list of 10 reviews each time. .append would append each
    # of those lists. So rather than having a final list of individual reviews
    # we'd have a list of lists - it would keep each of the ten reviews in a
    # list as a set. .extend flattens the hierarchy.
    text = get_a_review_text(filename)
    all_review_texts.extend(text)
    save_each_file(filename, text, counter)
    text_tokens = analyze_text(text)
    corpus_tokens.extend(text_tokens)
    counter += 1


frequency_distribution = nltk.FreqDist(corpus_tokens)
print(frequency_distribution['autism'])
print(frequency_distribution['aspergers'])
print(frequency_distribution['asperger'])

nltk.Text(corpus_tokens).dispersion_plot(['autism','aspergers','asperger'])
