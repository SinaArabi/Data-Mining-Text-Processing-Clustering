import csv
from hazm import Normalizer, WordTokenizer, Lemmatizer, POSTagger
import os

# Initialize NLP tools
normalizer = Normalizer()
tokenizer = WordTokenizer()
lemmatizer = Lemmatizer()
posTagger = POSTagger(model='pos_tagger.model')

# Forbidden word types
forbidden_word_types = ['PUNCT', 'CCONJ', 'VERB', 'ADP', 'SCONJ', 'DET', 'NUM', 'PRON']

def tokenize_news(news_content):
    """
    Tokenizes and lemmatizes the news content, removing unwanted words and special characters.
    """
    persian_alphabet = set(['ا', 'آ', 'ب', 'پ', 'ت', 'ث', 'ج', 'چ', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'ژ',
                            'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ک', 'گ', 'ل', 'م', 'ن', 'و', 'ه', 'ی'])
    
    # Normalize and tokenize the content
    normalized_news = normalizer.normalize(news_content)
    normalized_news = normalizer.remove_specials_chars(normalized_news)
    tokenized_news = tokenizer.tokenize(normalized_news)
    tagged_tokenized_news = posTagger.tag(tokens=tokenized_news)
    
    clean_tagged_tokenized_news = []
    for word in tagged_tokenized_news:
        # Check word conditions and lemmatize
        if all(word_type not in word[1] for word_type in forbidden_word_types) and \
           ('!' not in word[0]) and \
           ('?' not in word[0]) and \
           all(c in persian_alphabet for c in word[0]) and \
           word[0] not in ["هدف", "پژوهش", "بررسی", "حاضر", ")", "(", "]", "["]:
            lemmatized_word = lemmatizer.lemmatize(word[0])
            clean_tagged_tokenized_news.append(lemmatized_word)

    return clean_tagged_tokenized_news

def process_content(content):
    """
    Processes the content by normalizing, tokenizing, and lemmatizing the words.
    """
    persian_alphabet = set(['ا', 'آ', 'ب', 'پ', 'ت', 'ث', 'ج', 'چ', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'ژ',
                            'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ک', 'گ', 'ل', 'م', 'ن', 'و', 'ه', 'ی'])
    all_nums = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
    
    # Normalize and tokenize content
    content = normalizer.normalize(content)
    tokenized_content = tokenizer.tokenize(content)
    tagged = posTagger.tag(tokens=tokenized_content)
    
    new_listof_tokenized = []
    for tok in tagged:
        if all(c in persian_alphabet for c in tok[0]) and \
           all(x not in all_nums for x in tok[0]) and \
           tok[1] not in ["NUM,EZ", "NUM", "ADP", "CCONJ", "PUNCT", "VERB", "SCONJ", "DET", "PRON"] and \
           tok[0] not in ["هدف", "پژوهش", "بررسی", "حاضر", ")", "("]:
            lemmatized_content = lemmatizer.lemmatize(tok[0])
            new_listof_tokenized.append(lemmatized_content)

    return ' '.join(new_listof_tokenized)

def load_articles(file_path):
    """
    Loads articles from a CSV file and processes them.
    """
    contents = []
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            contents.append([row[0], row[1] + row[2]])

    return contents

def save_keywords_to_csv(contents, output_file):
    """
    Saves processed keywords to a CSV file.
    """
    total_documents = [[content[0], tokenize_news(content[1])] for content in contents]
    
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['URL', 'Keywords'])
        for doc in total_documents:
            tokenized_doc = ','.join([str(elem) for elem in doc[1]])
            writer.writerow([doc[0], tokenized_doc])

def main():
    input_file = 'all_articles.csv'  # Input CSV with articles
    output_file = 'all_keywords.csv'  # Output CSV for keywords

    # Load and process articles
    contents = load_articles(input_file)

    # Save the processed keywords
    save_keywords_to_csv(contents, output_file)

if __name__ == '__main__':
    main()
