& "venv\Scripts\Activate"
$env:FLASK_APP = "app.py"
$env:FLASK_ENV = "development"
Start-Process powershell -ArgumentList "flask run --port 5001"
Start-Sleep -Seconds 3
Start-Process "http://127.0.0.1:5001"