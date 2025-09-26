# Data Mining: Text Processing & Clustering

This repository contains various projects and implementations related to **data mining**, focusing on **text mining**, **web scraping**, and **clustering algorithms**. It demonstrates techniques for processing Persian text, extracting information from web pages, and clustering documents based on their content.

- **Web Scraping**: This part of the project uses `BeautifulSoup` to extract article data (abstracts and keywords) from local HTML files. It processes and saves the extracted data into CSV files for further analysis. Codes for this part are available at ./crawl.py .
  
- **Text Preprocessing**: Tokenization and lemmatization of Persian text using the **Hazm** library. The text is cleaned by removing stop words and filtering out irrelevant content (e.g., punctuation, numbers). Codes for this part are available at ./find_keywords.py .
  
- **Clustering**: The project implements **clustering algorithms** to group similar articles based on their content. The clustering can be applied to keyword sets or the full text of articles. Codes for this part are available at ./project.ipynb .


## Setup and Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Data-Mining.git
   cd Data-Mining
2. Install dependencies :
   ```bash
   pip install -r requirements.txt
3. Web Scraping: To extract article data and save it to a CSV file, run:
   ```bash
   python crawl.py
5. Text Preprocessing: To process the articles and extract keywords, run:
   ```bash
   python find_keywords.py  
7. Clustering: To run clustering algorithms on the processed data, navigate to notebook project.ipynb and follow the instructions inside.
