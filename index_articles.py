import os
import frontmatter # Parses YAML front matter from Markdown files
import markdown    # Converts Markdown text to HTML
from bs4 import BeautifulSoup # Strips HTML tags to get plain text
# Import the synchronous client class using the correct path
from algoliasearch.search.client import SearchClientSync 
from dotenv import load_dotenv # Loads variables from .env file

# --- Configuration ---
# Load environment variables from .env file in the current directory
load_dotenv() 
ALGOLIA_APP_ID = os.getenv("ALGOLIA_APP_ID")
# Use the ADMIN key loaded from .env for indexing (ensure this is regenerated if shared)
ALGOLIA_ADMIN_KEY = os.getenv("ALGOLIA_ADMIN_KEY") 
ALGOLIA_INDEX_NAME = "articles" # Or your chosen index name
# Define character limit for the content field to stay under Algolia's record size limit
CONTENT_CHAR_LIMIT = 8500 

# --- !!! IMPORTANT: Define which files to index !!! ---
# List derived from links in /ai and /math pages (including the previously excluded large file)
files_to_index = [
    # --- From /ai page ---
    "AI/2025/Introducing Vantage/Introducing Vantage.md",        # /introducing_vantage
    "AI/2024/Autoformalizer/Autoformalizer.md",                  # /the_need_for_an_autoformalizer
    "AI/2024/Catan/catan_ai.md",                                 # /catan_ai
    "AI/2020/Brain age project/brain_age_project.md",            # /brain_age_project

    # --- From /math page ---
    "math/articles/2024/Hilberts-10th-problem/Hilberts-10th-problem.md",    # /hilberts-10th-problem
    "math/articles/2024/Infinity-categories/infinity-categories.md",        # /infinity-categories
    "math/articles/2023/Metric-space-CH/Metric-Space-CH.md",                # /metric-space-ch
    "math/articles/2023/Casas-Alvero-conjecture/Casas-Alvero-Conjecture.md", # /casas-alvero
    "math/articles/2023/Categorical-coproducts/Categorical-Coproducts.md",  # /categorical-coproducts
    "math/articles/2023/Euler-characteristic-is-an-index/Euler-characteristic-is-an-index.md", # /euler-characteristic-is-an-index
    "math/articles/2023/Gauss-Legendre/Gauss-Legendre.md",                  # /gauss-legendre
    "math/articles/2023/IU-analysis-qualifying-solutions/IU-analysis-qualifying-solutions.md", # /iu-analysis-qualifying-solutions (RE-INCLUDED)
    "math/articles/2023/Local-systems-as-locally-constant-sheaves/LS-as-LCS.md", # /ls-as-lcs
    "math/articles/2023/Weil-conjectures-intro/Weil-Conjectures-Intro.md",  # /weil-conjectures-intro
    "math/articles/2023/Ramanujan-conjecture/Ramanujan-conjecture.md",      # /ramanujan-Conjecture (Note: Link had capital C, assuming filename doesn't)
]

# --- Check Credentials ---
# Ensure API keys are loaded from the .env file
if not ALGOLIA_APP_ID or not ALGOLIA_ADMIN_KEY:
    raise ValueError("ALGOLIA_APP_ID and ALGOLIA_ADMIN_KEY must be set in the .env file.")

# --- Initialize Algolia Client ---
# Initialize SearchClientSync directly using credentials from .env
print("Initializing Algolia client...")
client = SearchClientSync(ALGOLIA_APP_ID, ALGOLIA_ADMIN_KEY) 
print("Algolia client initialized.")

# --- Process Files and Prepare Data ---
records_to_index = []
# Get the absolute path of the directory the script is running from
project_root = os.path.dirname(os.path.abspath(__file__)) 
print(f"Looking for Markdown files in project root: {project_root}")

# Loop through the specified list of files
for relative_path in files_to_index:
    # Construct the full path to the markdown file
    filepath = os.path.join(project_root, relative_path)
    
    # Check if the file actually exists before trying to open it
    if not os.path.exists(filepath):
        print(f"Warning: File not found at specified path, skipping: {filepath}")
        continue

    try:
        # Read the file content and parse its YAML front matter
        print(f"Processing file: {relative_path}")
        post = frontmatter.load(filepath)
        
        # --- Extract Data from Front Matter ---
        # Get the permalink (required for link and unique ID)
        permalink = post.metadata.get('permalink')
        if not permalink:
            print(f"Warning: 'permalink' missing in front matter, skipping file: {relative_path}")
            continue
            
        # Use permalink for Algolia's unique objectID, remove leading/trailing slashes
        object_id = permalink.strip('/') 
        # Ensure the link starts with a slash for website navigation
        link = permalink if permalink.startswith('/') else '/' + permalink

        # Get the title, use object_id as a fallback if title is missing
        title = post.metadata.get('title', object_id) 
        # Get keywords if available (add 'keywords: [tag1, tag2]' to front matter)
        keywords = post.metadata.get('keywords', []) 
        # Get layout if you want to store/filter by it
        layout = post.metadata.get('layout', 'default')

        # --- Process Markdown Content ---
        # Convert the main content from Markdown to HTML
        html_content = markdown.markdown(post.content) 
        # Use BeautifulSoup to strip HTML tags and get plain text for indexing
        soup = BeautifulSoup(html_content, 'html.parser')
        plain_content = soup.get_text(separator=' ', strip=True)

        # --- Truncate Content if Necessary ---
        # Check if the extracted plain text exceeds the defined limit
        if len(plain_content) > CONTENT_CHAR_LIMIT:
            print(f"Truncating content for: {object_id} (Original length: {len(plain_content)})")
            # Keep the first part and add ellipsis to indicate truncation
            plain_content = plain_content[:CONTENT_CHAR_LIMIT] + "..." 
        
        # --- Create Algolia Record Object ---
        # Assemble the data into a dictionary matching Algolia's expected record structure
        record = {
            'objectID': object_id, # Unique ID for the record
            'title': title,
            'link': link,         # URL path for the article
            'content': plain_content, # The searchable (potentially truncated) body text
            'keywords': keywords,   # Associated keywords/tags
            'layout': layout        # Store the layout if useful
            # Add any other fields from front matter you want to index
        }
        # Add the processed record to the list that will be sent to Algolia
        records_to_index.append(record)
        print(f"Prepared record for: {object_id}")

    except Exception as e:
        # Print errors encountered during file processing
        print(f"Error processing file {relative_path}: {e}")

# --- Send Data to Algolia ---
# Check if any records were successfully prepared
if records_to_index:
    try:
        print(f"\nSending {len(records_to_index)} records to Algolia index '{ALGOLIA_INDEX_NAME}'...")
        # Call save_objects directly on the client, passing index_name and the list of records
        res = client.save_objects(
            index_name=ALGOLIA_INDEX_NAME, 
            objects=records_to_index 
        ) 
        
        # Correctly access the task_id from the BatchResponse object inside the list 'res'
        # Check if the response list is not empty before accessing its element
        if res and isinstance(res, list) and len(res) > 0 and hasattr(res[0], 'task_id'):
             print(f"Algolia task initiated. Task ID: {res[0].task_id}")
             # Wait for the task using the client, index name, and task ID from the response
             client.wait_for_task(index_name=ALGOLIA_INDEX_NAME, task_id=res[0].task_id) 
             print("Successfully indexed records!")
        else:
             # Handle cases where the response might not be as expected
             print(f"Indexing initiated, but couldn't confirm task ID or wait. Response: {res}")
             print("Please check the Algolia dashboard to verify indexing.")

    except Exception as e:
        # Print errors encountered during communication with Algolia
        print(f"Error sending records to Algolia: {e}")
else:
    # Message if no valid files were found or processed
    print("No valid records prepared to index.")
