from nlmdb import dbagent, dbagent_private
'''
# Use the simplified API
response = dbagent(
    api_key="api",
    db_path="Database.db",
    query="show all tables"
)

# Get the response
print(response["output"])
'''


import os
from nlmdb import dbagent_private

def main():
    # Get Hugging Face token from environment variable
    hf_token = "df-taken"
    if not hf_token:
        print("Please set your HUGGINGFACE_TOKEN environment variable")
        return
    
    # Specify the Hugging Face model to use
    # This example uses Meta's Llama 3 model
    model_repo = "mistralai/Mixtral-8x7B-Instruct-v0.1"
    
    # Path to your database
    db_path = "/Users/rakshithdharmappa/projects/car_company_database/Car_Database.db"
    
    # Your natural language query
    query = "Give me sql code to show all rows od models table"
    
    # Configure additional model parameters (optional)
    model_kwargs = {
        "task": "text-generation",
        "max_new_tokens": 4000,
        "temperature": 0.7,
        "do_sample": False,
        "repetition_penalty": 1
    }
    
    # Option 1: Pass configuration as a tuple
    response = dbagent_private(
    (hf_token, model_repo),  # More reliable model
    db_path,
    query,
    verbose=False
)

    
    # Option 2: Pass configuration as a dictionary
    # response = dbagent_private(
    #     {"token": hf_token, "model_repo": model_repo},
    #     db_path,
    #     query,
    #     verbose=True,
    #     model_kwargs=model_kwargs
    # )
    
    # Print the result
    print("Response:")
    print(response["output"])

if __name__ == "__main__":
    main()