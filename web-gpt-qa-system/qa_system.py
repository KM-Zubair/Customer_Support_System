import pandas as pd
import numpy as np
from openai import OpenAI
import os
from ast import literal_eval
from scipy.spatial.distance import cosine

class QASystem:
    def __init__(self, embeddings_path='processed/embeddings.csv'):
        self.client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
        self.df = self.load_embeddings(embeddings_path)

    def load_embeddings(self, path):
        df = pd.read_csv(path, index_col=0)
        df['embeddings'] = df['embeddings'].apply(literal_eval).apply(np.array)
        return df

    def get_embedding(self, text):
        try:
            response = self.client.embeddings.create(input=text, model='text-embedding-ada-002')
            return response.data[0].embedding
        except Exception as e:
            print(f"Error getting embedding: {e}")
            return None

    def create_context(self, question, max_len=1800):
        q_embeddings = self.get_embedding(question)
        self.df["distances"] = self.df["embeddings"].apply(lambda x: cosine(q_embeddings, x))
        
        returns = []
        cur_len = 0

        for i, row in self.df.sort_values('distances', ascending=True).iterrows():
            cur_len += row['n_tokens'] + 4
            if cur_len > max_len:
                break
            returns.append(row["text"])

        return "\n\n###\n\n".join(returns)

    def answer_question(self, question, debug=False):
        context = self.create_context(question)
        
        if debug:
            print("Context:\n" + context)
            print("\n\n")
        
        messages = [
            {"role": "system", "content": "Answer the question based on the context below, and if the question can't be answered based on the context, say \"I don't know\"\n\n"},
            {"role": "user", "content": f"Context: {context}\n\n---\n\nQuestion: {question}\nAnswer:"}
        ]
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0,
                max_tokens=150,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error getting answer: {e}")
            return ""

def main():
    qa_system = QASystem()
    
    # Example questions
    questions = [
        "What's the website about?",
        "How to fix a bug?",
        # Add more questions as needed
    ]
    
    for question in questions:
        print(f"\nQuestion: {question}")
        answer = qa_system.answer_question(question)
        print(f"Answer: {answer}")

if __name__ == "__main__":
    main()