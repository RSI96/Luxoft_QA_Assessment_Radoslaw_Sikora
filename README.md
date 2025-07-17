# Luxoft_QA_Assessment_Radoslaw_Sikora
Developed on Windows

## Task 2: API Testing
First three tests are fulfilling requirements for this task. The rest is for better coverage.
It would be much better to use pytest for test execution but it was not listed in available tools for this task so I tried to do the task without it.

### Prerequisites
- Python
- Requests libary
- Flask
- Windows Operating System
#### Run Python Flask mock API
```powershell
py -m flask --app .\mock_api.py run
```
#### Run automated tests
```powershell
py -m task2_api_test.py
```

