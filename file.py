import os
import pandas as pd
import PyPDF2 as pypdf2
import csv

#for training data...... 
# reading pdf files and making pandas dataframe with columns having name "text" and its corresponding "labels"
def create_dataframe(directory):
    df = pd.DataFrame(columns=['text', 'label'])
    for filename in os.listdir(directory):
        if filename.endswith('.pdf'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'rb') as f:
                reader = pypdf2.PdfReader(f)  # use PdfReader instead of PdfFileReader
                num_pages = len(reader.pages)
                file_content = ''
                for i in range(num_pages):
                    page = reader.pages[i]
                    file_content += page.extract_text()
                df = df.append({'text': file_content, 'label': filename}, ignore_index=True)
    return df

#for testing data
def create_dataframe(directory):
    df = pd.DataFrame(columns=['text'])
    for filename in os.listdir(directory):
        if filename.endswith('.pdf'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'rb') as f:
                reader = pypdf2.PdfReader(f)  # use PdfReader instead of PdfFileReader
                num_pages = len(reader.pages)
                file_content = ''
                for i in range(num_pages):
                    page = reader.pages[i]
                    file_content += page.extract_text()
                df = df.append({'text': file_content}, ignore_index=True)
    return df


#replacing new lines with '.'
def replace_newlines(file_path):
    with open(file_path, 'r', newline='') as input_file:
        reader = csv.reader(input_file)
        rows = []
        for row in reader:
            row[0] = row[0].replace('\n', '.')
            rows.append(row)
    with open(file_path, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(rows)

# df = create_dataframe('D:\document classification\Training')
# df = create_dataframe('D:\document classification\Testing')

# df.to_csv('D:\document classification\Testing\illy.csv')

# replace_newlines('D:\document classification\Training\ill.csv')