$env:ENV = "test"
$env:PYTHONPATH = "."
pytest tests/auth
