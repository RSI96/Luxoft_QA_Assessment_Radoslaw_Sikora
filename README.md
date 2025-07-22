# Luxoft_QA_Assessment_Radoslaw_Sikora
## Environment Details
- Developed on Windows.
- Android Studio Narwhal - version: 2025.1.1 Patch 1
- Python - version: 3.9.0
- uiautomator2 - version: 3.3.3
- Flask - version: 3.1.1
- Requests - version: 2.32.4
- Behave - version: 1.2.6

## Task 1: Mobile Application Testing
It would be much better to use pytest for test execution but it was not listed in available tools for this task so I tried to do the task without it.
I used Gemini AI (from Android Studio) to generate script that connects to the device, starts an app and puts value into the input field. The rest was developed by me.

### Prerequisites
- Download and install the Android SDK from developer.android.com
- Add platform-tools directory to your system's PATH environment variable
- Set Up an Android Virtual Device (Click Create Virtual Device and choose a hardware profile) and Launch the Emulator
- Install the APK File (For example: Drag and drop the APK file into the emulator window)
- Python
- uiautomator2, time libaries

### Setup and run tests
- Open Android Studio. Go to Device Manager. Start emulator of one of your devices.
- Open folder C:\Users\YOUR_USERNAME\AppData\Local\Android\Sdk\platform-tools
- Inside of that folder run.
```powershell
adb devices
```
- Save device name from 'List of devices' column. Update DEVICE_SERIAL variable in task1_mobile_app_test.py with that name.
- Run task1_mobile_app_test.py file.
- Test results are printed into the terminal.

### Test description
- TC01_check_add_operation - Tests add operation with precision to 2 decimal points with various inputs. Boundary value analysis is performed for value of 0.
- TC02_check_substract_operation() - Tests substract operation with precision to 2 decimal points with various inputs. Boundary value analysis is performed for value of 0.
- TC03_check_divide_operation() - Tests divide operation with precision to 2 decimal points with various inputs. Boundary value analysis is performed for value of 0.
- TC04_check_multiply_operation() - Tests multiply operation with precision to 2 decimal points with various inputs. Boundary value analysis is performed for value of 0.

### Limitations and known bugs
- Multiply operation does not work as expected. Instead of multpilying it adds two numbers.
- Without requirement about mi and max ranges I decided to test this application with 2 decimal points precision.

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

### Test description
- TC01_test_get_user - Tests Get User with id = 1.
- TC02_test_create_user - Test Create User.
- TC03_test_error_handling - Test Create User. Status Code is 400.
- TC04_test_get_users - Test Get User with all available ids.
- TC05_test_get_user_status_code - Test Get User Status Code. Status code is 200.
- TC06_test_get_users_status_code - Test Get Users Status Code. Status code is 200.
- TC07_test_create_user_status_code - Test Create New User Status Code. Status code is 201.

## Task 3: Gherkin Scenario Creation

### Prerequisites
- Python
- Behave 

### Test description
- Test Add operation - Tests add operation with values 1 and 2

#### Run automated tests
```powershell
py -m behave
```