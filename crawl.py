import os
import requests
from bs4 import BeautifulSoup
import csv

# Function to get article data (abstract and keywords)
def get_article_data(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')

            # Extract abstract
            abstract_tag = soup.find('div', class_='padding_abstract justify rtl')
            abstract = abstract_tag.text.strip() if abstract_tag else None

            # Extract keywords
            keyword_tags1 = soup.find_all('li', class_='padding-3')
            keyword_tags2 = [tag.find_all('a', class_='tag_a') for tag in keyword_tags1]
            keywords = [tag.text.strip() for sublist in keyword_tags2 for tag in sublist]

            return abstract, keywords
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None, None


# Function to save article data to a CSV file
def save_to_csv(filename, file_path, abstract, keywords):
    # Ensure the file exists, otherwise create it with headers
    file_exists = os.path.exists(filename)
    
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(['File Path', 'Abstract', 'Keywords'])  # Write headers only once
        writer.writerow([file_path, abstract, ','.join(keywords)])


# Main function to crawl articles
def main():
    # Local file path for saving data
    output_file = 'all_articles.csv'

    # Directory containing local HTML files (adjust this directory as per your setup)
    articles_dir = './Articles/'  # Assuming the 'Articles' folder is in the same directory as the script

    count = 0
    i = 95766

    # Loop through a range of articles and fetch the data
    while count < 300:
        file_path = os.path.join(articles_dir, f'article_{i}.html')

        if os.path.exists(file_path):
            abstract, keywords = get_article_data(file_path)
            if abstract:
                count += 1
                save_to_csv(output_file, file_path, abstract, keywords)
                print(f"Processed {count} articles")
        else:
            print(f"File not found: {file_path}")

        i -= 2  # Adjust the counter for the next article

if __name__ == '__main__':
    main()
