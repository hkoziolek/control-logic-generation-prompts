import pandas as pd
import csv

# Read the CSV file
input_csv = 'chatgpt/ChatGPT-Prompts-PLC-Programming.csv'  # Replace with your input CSV file name
output_md = 'prompts/README.md'  # Replace with your output markdown file name

with open(output_md, 'w', encoding='utf-8') as md_file:
    md_file.write(f'# Control Logic Generation Prompt Collection\n\n')
    md_file.write(f'The following 100 prompts are designed to test the ability of LLMs to support control engineers in industrial automation. They are structured in 10 categories. Many of them generate IEC 61131-3 Structured Text as a typical control programming language. Below each prompt is the answer we obtained from ChatGPT with GPT-4.\n\n')


# Load the CSV file into a pandas DataFrame
data = pd.read_csv(input_csv, sep = ";", error_bad_lines=False)

# Open a new markdown file for writing
with open(output_md, 'a', encoding='utf-8') as md_file:
    # Iterate through the rows in the DataFrame
    current_category = ""
    for index, row in data.iterrows():
        number = row[0]
        category = row[1]
        short_name = row[2]
        prompt = row[3]
        pdf = row[14]

        if (category != current_category):
            current_category = category
            md_file.write(f'## {current_category}\n\n')

        
        # Write the heading and content to the markdown file
        md_file.write(f'### {short_name}:\n\n{prompt}<br>[ChatGPT Answer](<../chatgpt/{short_name}.md>)\n\n')



print(f'Markdown file saved as {output_md}')

