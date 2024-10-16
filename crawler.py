import requests
import re
import urllib.request
from bs4 import BeautifulSoup
from collections import deque
from html.parser import HTMLParser
from urllib.parse import urlparse
import os
import pandas as pd
import tiktoken
from openai import OpenAI
import csv

# Regex pattern to match a URL
HTTP_URL_PATTERN = r'^http[s]*://.+'

# Define root domain to crawl
domain = "simpleprogrammer.com"
full_url = "https://simpleprogrammer.com/blog-2/"

class HyperlinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hyperlinks = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a" and "href" in attrs:
            self.hyperlinks.append(attrs["href"])

def get_hyperlinks(url):
    try:
        with urllib.request.urlopen(url) as response:
            if not response.info().get('Content-Type').startswith("text/html"):
                return []
            html = response.read().decode('utf-8')
    except Exception as e:
        print(f"Error opening {url}: {e}")
        return []
    
    parser = HyperlinkParser()
    parser.feed(html)
    return parser.hyperlinks

def get_domain_hyperlinks(local_domain, url):
    clean_links = []
    for link in set(get_hyperlinks(url)):
        clean_link = None
        if re.search(HTTP_URL_PATTERN, link):
            url_obj = urlparse(link)
            if url_obj.netloc == local_domain:
                clean_link = link
        else:
            if link.startswith("/"):
                link = link[1:]
            elif link.startswith("#") or link.startswith("mailto:"):
                continue
            clean_link = "https://" + local_domain + "/" + link

        if clean_link is not None:
            if clean_link.endswith("/"):
                clean_link = clean_link[:-1]
            clean_links.append(clean_link)
    return list(set(clean_links))

def crawl(url):
    local_domain = urlparse(url).netloc
    queue = deque([url])
    seen = set([url])

    if not os.path.exists("text/"):
        os.mkdir("text/")
    if not os.path.exists("text/" + local_domain + "/"):
        os.mkdir("text/" + local_domain + "/")
    if not os.path.exists("processed"):
        os.mkdir("processed")

    while queue:
        url = queue.pop()
        print(f"Fetching {url}")

        try:
            with open('text/' + local_domain + '/' + url[8:].replace("/", "_") + ".txt", "w", encoding='utf-8') as f:
                response = requests.get(url)
                response.raise_for_status()
                soup = BeautifulSoup(response.text, "html.parser")
                text = soup.get_text()
                
                if "You need to enable JavaScript to run this app." in text:
                    print(f"Unable to parse page {url} due to JavaScript being required")
                    continue
                
                f.write(text)

            for link in get_domain_hyperlinks(local_domain, url):
                if link not in seen:
                    queue.append(link)
                    seen.add(link)

        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            continue

def process_text_files():
    texts = []
    for file in os.listdir("text/" + domain + "/"):
        with open("text/" + domain + "/" + file, "r", encoding='utf-8') as f:
            text = f.read()
            texts.append((file[11:-4].replace('-', ' ').replace('_', ' ').replace('#update', ''), text))

    df = pd.DataFrame(texts, columns=['fname', 'text'])
    df['text'] = df.fname + ". " + df.text.str.replace('\n', ' ').replace('\r', ' ')
    return df

def get_embeddings(df):
    client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
    tokenizer = tiktoken.get_encoding("cl100k_base")
    max_tokens = 500

    def get_embedding(text):
        try:
            response = client.embeddings.create(input=text, model='text-embedding-ada-002')
            return response.data[0].embedding
        except Exception as e:
            print(f"Error processing text: {text[:50]}..., Error: {e}")
            return None

    def split_into_many(text, max_tokens=max_tokens):
        sentences = text.split('. ')
        n_tokens = [len(tokenizer.encode(" " + sentence)) for sentence in sentences]
        
        chunks = []
        tokens_so_far = 0
        chunk = []

        for sentence, token in zip(sentences, n_tokens):
            if tokens_so_far + token > max_tokens:
                chunks.append(". ".join(chunk) + ".")
                chunk = []
                tokens_so_far = 0
            if token > max_tokens:
                continue
            chunk.append(sentence)
            tokens_so_far += token + 1

        if chunk:
            chunks.append(". ".join(chunk) + ".")

        return chunks

    df['n_tokens'] = df.text.apply(lambda x: len(tokenizer.encode(x)))
    
    shortened = []
    for _, row in df.iterrows():
        if row['text'] is None:
            continue
        if row['n_tokens'] > max_tokens:
            shortened += split_into_many(row['text'])
        else:
            shortened.append(row['text'])
    
    df_shortened = pd.DataFrame(shortened, columns=['text'])
    df_shortened['n_tokens'] = df_shortened.text.apply(lambda x: len(tokenizer.encode(x)))
    df_shortened['embeddings'] = df_shortened.text.apply(get_embedding)
    
    return df_shortened

def main():
    crawl(full_url)
    df = process_text_files()
    df_with_embeddings = get_embeddings(df)
    df_with_embeddings.to_csv('processed/embeddings.csv')
    print("Crawling and embedding generation completed successfully!")

if __name__ == "__main__":
    main()