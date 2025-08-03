# Customer Complaint Analyzer

A Python project leveraging generative AI to extract key insights and generate SQL queries for customer complaint analysis. This tool connects to a PostgreSQL database, analyzes unstructured complaint text, automatically generates relevant SQL queries, executes them, and provides actionable business insights to help companies improve customer satisfaction.

---

## Features

- **Natural Language Question Processing:** Turn customer service questions into key database filters and SQL queries using Google Gemini AI.
- **Automated SQL Generation:** Get accurate, schema-compliant SQL statements for complex queries.
- **Database Integration:** Seamlessly connects and fetches results from a PostgreSQL database.
- **AI-Powered Insights:** Analyzes data returned by SQL and offers business improvement suggestions.
- **Token Usage Feedback:** Displays language model token consumption for transparency.

---

## Use Cases

- Business intelligence for customer service teams.
- Data-driven root cause analysis of complaint trends.
- Automate reporting for customer satisfaction initiatives.
- Accelerate development/testing of GPT-powered analytics tooling.

---

**4. Configure environment variables**

- Insert your **Google Gemini AI API Key.**
- Update your **PostgreSQL database credentials** (host, port, database, user, password).

---

## Usage Example

1. **Prepare Your Database:**  
   Ensure the required tables (`customer` and `complaint`) exist and are populated as described in the schema in the script comments.

2. **Run the Analyzer Script:**
   '''bash
    python googleapi.py
   '''

4. **Example Query Flow:**
   - Script asks: _"How many times was the product delivered late?"_
   - Extracts keywords and constructs SQL with Gemini AI.
   - Executes SQL and returns results, along with AI-driven analysis.


---
## Table Schemas
Below are the database schemas used by the analyzer:

customer Table
Column	        Type	            Description
customer_id	    SERIAL            PRIMARY KEY / INTEGER	Unique customer identifier
name	          VARCHAR(100)	    Customer's name
PIN	            VARCHAR(10)	      Postal identification number
city	          VARCHAR(50)	      Customer's city
customer_size	  VARCHAR(10)	      Size: 'large', 'medium', 'small'

complaint Table
Column	        Type	            Description
complaint_id	  SERIAL            PRIMARY KEY / INTEGER	Unique complaint identifier
complaint_date	DATE	            Date complaint was made
customer_id	    INTEGER	          References customer.customer_id
text	          TEXT	            Complaint description
severity	      VARCHAR(10)	      'high', 'medium', or 'low'
priority	      VARCHAR(10)	      'high', 'medium', or 'low'
status	        VARCHAR(15)	      'open', 'in progress', 'resolved', 'closed'




