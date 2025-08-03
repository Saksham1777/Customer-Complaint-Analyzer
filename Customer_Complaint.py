from google import genai
from google.genai import types
import psycopg2

client = genai.Client(api_key="") #Your api key here
model = "gemini-2.0-flash"


query = "how many times was the product delivered late"

prompt  = "Find key words from the text relavent to 2 tables - customer and complaint tables and their columns." \
"Table names: customer, complaint"\
"The complaint table schema: (complaint_id, complaint_date, customer_id, text, severity(high, medium, low), priority(high, medium, low), status(open, in progress, resolved, closed))." \
"The customer table schema: (customer_id, name, PIN, city, customer_size (large, medium, small)). " \
"Find them for both tables and return them. Also try to find the filter for the data."\
"Format your answer as such - customer tabel -(your repsonse) followed by complaint table -(your repsonse). Folow this with your explenation if asked "\
"Give a very simple explenation of the question at the end."

response1 = client.models.generate_content(
    model=model, contents=query,
    config=types.GenerateContentConfig(     
        temperature=2,
        system_instruction = prompt
    )
)
print(response1.text)
output_1 = response1.text


prompt2  = "Create an sql command for the given  - customer and complaint tables and their columns." \
"Table names: customer, complaint"\
"The complaint table schema: (complaint_id, complaint_date, customer_id, text, severity(high, medium, low), priority(high, medium, low), status(open, in progress, resolved, closed)). " \
"The customer table schema: (customer_id, name, PIN, city, customer_size (large, medium, small)). "\
"write an sql for input -  customer table - (extract from prompt) and complaint table - (extract from prompt)" \
"only provide simple sql from - from 'select' to ';'. keep case sensitivity in mind and stick to schema provided here."

response2 = client.models.generate_content(
    model=model, contents=output_1,
    config=types.GenerateContentConfig(     
        temperature=2,
        system_instruction = prompt2
    )
)
print("\n")

prompt3 = "extract bare bones sql comand only. extract from 'select' to ';'"
response3 = client.models.generate_content(
    model=model, contents=response2.text,
    config=types.GenerateContentConfig(     
        temperature=0,
        system_instruction = prompt3,
    )
)
print("repsonse3")
print(response3.text)
print("\n")

# database connection
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="Lead",
    user="postgres",
    password="postgres"
)

cursor = conn.cursor()
cursor.execute(response3.text)
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()


prompt4 = "analyse the data based on the sql command and the data returned and tell what can be improved upon for the company to cater to its customers."\
"Table names: customer, complaint"\
"The complaint table schema: (complaint_id, complaint_date, customer_id, text, severity(high, medium, low), priority(high, medium, low), status(open, in progress, resolved, closed)). " \
"The customer table schema: (customer_id, name, PIN, city, customer_size (large, medium, small)). "
response4 = client.models.generate_content(
    model=model, contents=[response2.text,response3.text],
    config=types.GenerateContentConfig(     
        temperature=2,
        system_instruction = prompt4,
    )
)
print(response4.text)


#intial - catching key words
total_tokens = client.models.count_tokens(
    model=model, contents=prompt
)
print("total_tokens1: ", total_tokens)

#2nd prompt - sql genrations
total_tokens = client.models.count_tokens(
    model=model, contents=prompt2
)
print("total_tokens2: ", total_tokens)

#3rd prompt - sql extraction
total_tokens = client.models.count_tokens(
    model=model, contents=prompt3
)
print("total_tokens3: ", total_tokens)

#4th prompt - analysis of data
total_tokens = client.models.count_tokens(
    model=model, contents=prompt4
)

print("total_tokens4: ", total_tokens)
