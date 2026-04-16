#!/bin/bash
echo "Activating virtual environment..."

# Activate virtual environment 
source venv/bin/activate

echo "Running tests..."

pytest

# Check exit status
if [ $? -eq 0 ]; then
    echo "All tests passed "
    exit 0
else
    echo "Tests failed "
    exit 1
fi