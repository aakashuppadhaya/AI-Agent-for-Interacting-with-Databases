# Natural Language to PostgreSQL AI Agent

A local AI agent that converts natural language queries into PostgreSQL SQL using Mistral-7B LLM. Runs entirely on your MacBook (no API costs).

## Features
- 🗣️ Natural language to SQL conversion
- 🔒 100% local execution (no cloud dependencies)
- 🐘 PostgreSQL integration
- ⚡ Optimized for Apple Silicon (M-series chips)

## Prerequisites
- macOS (Tested on Ventura/Sonoma)
- Apple Silicon (M1/M2/M3)
- Python 3.9+
- 16GB+ RAM recommended
- Homebrew (for PostgreSQL installation)

## Setup

brew install postgresql@14
brew services start postgresql@14 

## create database
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100),
    salary NUMERIC
);


INSERT INTO employees (name, department, salary) VALUES
('Alice', 'Engineering', 85000),
('Bob', 'Marketing', 75000),
('Charlie', 'Sales', 90000);

install CODE lAMMA from hugging face and other dependencies
python3 -m pip install llama-cpp-python langchain sqlalchemy psycopg2-binary
wget https://huggingface.co/TheBloke/CodeLlama-7B-Instruct-GGUF/resolve/main/codellama-7b-instruct.Q4_K_M.gguf


ask following questions:
Show all employees in Engineering?
What's the average salary?
What's the average salary in sales?
List employees earning more than $80,000?


