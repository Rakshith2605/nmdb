"""
Test script for the MCP library.
"""

# Import from the correct package name
from nmdb import Config, DatabaseHandler, DatabaseTools, MCPHandler, create_database_agent
from openai import OpenAI
import os

def main():
    # Get API key from environment variable instead of hardcoding
    # You should set this in your environment or .env file
    # export OPENAI_API_KEY="your-key-here"
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        # Fallback only for testing - don't use in production!
        api_key = "your-api-key-here"  # Replace with your key before running
    
    # Path to your existing database
    db_path = "/Users/rakshithdharmappa/projects/car_company_database/Car_Database.db"
    
    # Initialize configuration
    config = Config(openai_api_key=api_key, db_path=db_path)
    
    # Initialize database handler
    # Note: We're not creating a sample database since you're using an existing one
    db_handler = DatabaseHandler(config.db_path)
    
    # Initialize database tools
    db_tools = DatabaseTools(db_handler)
    tools = db_tools.get_tools()
    
    # Initialize OpenAI client
    client = OpenAI(api_key=config.openai_api_key)
    
    # Initialize MCP handler
    mcp_handler = MCPHandler(client, db_handler)
    
    # Create agent executor
    agent_executor = create_database_agent(
        openai_api_key=config.openai_api_key,
        tools=tools,
        mcp_handler=mcp_handler,
        verbose=True
    )
    
    # Run a query
    response = agent_executor.invoke({
        "input": "show all customers detail in Customers tables where customer name is Pitbull Perez",
        "chat_history": []
    })
    
    print("Response:")
    print(response["output"])

if __name__ == "__main__":
    main()