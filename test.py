from nlmdb import dbagent

# Use the simplified API
response = dbagent(
    api_key="api",
    db_path="Database.db",
    query="show all tables"
)

# Get the response
print(response["output"])