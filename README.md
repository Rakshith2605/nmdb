# NLMDB: Natural Language & MCP Database

NLMDB is a Python library that allows you to query databases using natural language through the Model Context Protocol (MCP) approach. The library provides a simple API for interacting with databases using either OpenAI or Hugging Face models.

## Features

- Query databases using natural language
- Support for both OpenAI and Hugging Face models
- Automatic schema extraction
- Clean, professional responses
- Simple, intuitive API

## Installation

```bash
pip install nlmdb
```

## Quick Start

### Using OpenAI

```python
from nlmdb import dbagent

# Initialize the agent with your API key and database path
response = dbagent(
    api_key="your-openai-api-key",
    db_path="path/to/your/database.db",
    query="What tables are in the database and what columns do they have?"
)

print(response["output"])
```

### Using Hugging Face

```python
from nlmdb import dbagent_private

# Initialize the agent with your Hugging Face token and model name
response = dbagent_private(
    hf_config=("your-huggingface-token", "model-repo-name"),
    db_path="path/to/your/database.db",
    query="What tables are in the database and what columns do they have?"
)

print(response["output"])
```

## Advanced Usage

### Running with Verbose Output

You can enable verbose output to see the SQL queries being generated and executed:

```python
response = dbagent(
    api_key="your-openai-api-key",
    db_path="path/to/your/database.db",
    query="How many customers do we have?",
    verbose=True
)
```

### Using Local Hugging Face Models

For improved performance or when working offline, you can run Hugging Face models locally:

```python
response = dbagent_private(
    hf_config=("your-huggingface-token", "model-repo-name"),
    db_path="path/to/your/database.db",
    query="What tables are in the database?",
    use_local=True  # This will download and run the model locally
)
```

### Customizing Model Parameters

You can customize the behavior of the language model by passing additional parameters:

```python
model_kwargs = {
    "temperature": 0.2,
    "max_new_tokens": 1024,
    "repetition_penalty": 1.1
}

response = dbagent_private(
    hf_config=("your-huggingface-token", "mistralai/Mixtral-8x7B-Instruct-v0.1"),
    db_path="path/to/your/database.db",
    query="Summarize the sales data for the last quarter",
    model_kwargs=model_kwargs
)
```

## Supported Databases

Currently, NLMDB supports:

- SQLite

Future releases will add support for:

- PostgreSQL
- MySQL
- Microsoft SQL Server

## Requirements

- Python 3.8+
- openai>=1.0.0
- langchain>=0.1.0
- langchain-core>=0.1.0
- langchain-community>=0.0.0
- langchain-huggingface>=0.0.1 (for Hugging Face integration)

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Acknowledgements

This library is built on top of:

- LangChain
- OpenAI API
- Hugging Face Inference API
- SQLite
