#!/bin/bash

echo "Activating virtual environment..."

source venv/Scripts/activate

echo "Running test suite..."

python -m pytest

if [ $? -eq 0 ]; then
    echo "✅ All tests passed!"
    exit 0
else
    echo "❌ Some tests failed!"
    exit 1
fi