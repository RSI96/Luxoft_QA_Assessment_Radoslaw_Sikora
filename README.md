# Luxoft_QA_Assessment_Radoslaw_Sikora
Developed on Windows.

## Task 1: Mobile Application Testing
It would be much better to use pytest for test execution but it was not listed in available tools for this task so I tried to do the task without it.
I used Gemini AI (from Android Studio) to generate script that connects to the device, starts an app and puts value into the input field. The rest was developed by me.

### Prerequisites
- Download and install the Android SDK from developer.android.com
- Add platform-tools directory to your system's PATH environment variable
- Set Up an Android Virtual Device (Click Create Virtual Device and choose a hardware profile) and Launch the Emulator
- Install the APK File (For example: Drag and drop the APK file into the emulator window)

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

### Limitations and known bugs
- Multiply operation does not work as expected. Instead of multpilying it adds two numbers

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

