import uiautomator2 as u2
import time

# --- Configuration ---
DEVICE_SERIAL = "emulator-5554"
PACKAGE_NAME = "com.admsqa.buggycalc"

RESULT_VIEW_SUFFIX = "resultView"
INPUT1_SUFFIX = "input1"
INPUT2_SUFFIX = "input2"
ADD_BUTTON_SUFFIX = "addButton"
SUBSTRACT_BUTTON_SUFFIX = "subtractButton"
DIVIDE_BUTTON_SUFFIX = "divideButton"
MULTIPLY_BUTTON_SUFFIX = "multiplyButton"

d = None

# --- Functions ---
def connect_to_the_device():
    '''Connects to the device.'''

    global d
    global DEVICE_SERIAL
    print(f"Attempting to connect to device with serial: {DEVICE_SERIAL}...")
    d = u2.connect(DEVICE_SERIAL)

    if not d:
        print(f"Failed to connect to device {DEVICE_SERIAL}.")
        print("Please ensure the emulator is running and `python -m uiautomator2 init` has been run for it.")
        exit()

    print(f"Successfully connected to: {d.device_info.get('serial', 'N/A')}")

def start_app():
    '''Starts an application'''

    global d
    global PACKAGE_NAME
    print(f"Stopping app {PACKAGE_NAME} if it's running...")
    d.app_stop(PACKAGE_NAME)
    time.sleep(1)

    print(f"Starting app: {PACKAGE_NAME}...")
    d.app_start(PACKAGE_NAME, stop=False)

    print("Waiting for app to load...")
    time.sleep(5)

def insert_value_to_input(RESULT_INPUT_SUFFIX, value):
    '''Inserts value to input with given input ID.'''
    
    global PACKAGE_NAME
    FULL_INPUT_ID = f"{PACKAGE_NAME}:id/{RESULT_INPUT_SUFFIX}"
    value = str(value)

    #print(f"\nLooking for element with resource ID: '{FULL_INPUT_ID}'")
    #print("Ensure the element is visible on the screen.")

    if d(resourceId=FULL_INPUT_ID).wait(timeout=20.0): 
        #print("Element found.")
        result_element = d(resourceId=FULL_INPUT_ID)
        result_element.send_keys(value)
        element_text = result_element.get_text()

        if element_text is not None:
            pass
            #print(f"\nSUCCESS: Text found in '{RESULT_INPUT_SUFFIX}': '{element_text}'")
        else:
            pass
            #print(f"\nINFO: Element '{RESULT_INPUT_SUFFIX}' found, but it has no text or text is empty.")
    else:
        pass
        #print(f"\nFAILED: Element with resource ID '{FULL_INPUT_ID}' not found within the timeout period.")

def click_element(ELEMENT_ID_SUFFIX):
    '''Clicks element with given element ID.'''
    global PACKAGE_NAME
    FULL_ELEMENT_ID = f"{PACKAGE_NAME}:id/{ELEMENT_ID_SUFFIX}"

    #print(f"\nLooking for element with resource ID: '{FULL_ELEMENT_ID}'")
    #print("Ensure the element is visible on the screen.")

    if d(resourceId=FULL_ELEMENT_ID).wait(timeout=20.0):
        #print("Element found.")
        result_element = d(resourceId=FULL_ELEMENT_ID)
        result_element.click()
    else:
        pass
        #print(f"\nFAILED: Element with resource ID '{FULL_ELEMENT_ID}' not found within the timeout period.")

def check_result_value(RESULT_VIEW_SUFFIX):
    '''Checks what value is present in result field.'''
    global PACKAGE_NAME
    global d
    FULL_RESULT_VIEW_ID = f"{PACKAGE_NAME}:id/{RESULT_VIEW_SUFFIX}"

    #print(f"\nLooking for element with resource ID: '{FULL_RESULT_VIEW_ID}'")
    #print("Ensure the element is visible on the screen.")

    if d(resourceId=FULL_RESULT_VIEW_ID).wait(timeout=20.0): 
        #print("Element found.")
        result_element = d(resourceId=FULL_RESULT_VIEW_ID)

        # Get the text property
        element_text = result_element.get_text()

        if element_text is not None:
            pass
            #print(f"\nSUCCESS: Text found in '{RESULT_VIEW_SUFFIX}': '{element_text}'")
        else:
            pass
            #print(f"\nINFO: Element '{RESULT_VIEW_SUFFIX}' found, but it has no text or text is empty.")
    else:
        pass
        #print(f"\nFAILED: Element with resource ID '{FULL_RESULT_VIEW_ID}' not found within the timeout period.")
    result = element_text if element_text == 'Error: invalid operation' else round(float(element_text), 2)
    return result

# --- Tests ---

def TC01_check_add_operation():
    '''Tests add aperation with precision to 2 decimal points'''
    connect_to_the_device()
    start_app()

    #---
    insert_value_to_input(INPUT1_SUFFIX, 1)
    insert_value_to_input(INPUT2_SUFFIX, 1)
    click_element(ADD_BUTTON_SUFFIX)
    actual_result = round(check_result_value(RESULT_VIEW_SUFFIX), 2)
    expected_result = round(float(2), 1)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC01. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC01 - Add operation. Expected: {expected_result}. Observed: {actual_result}.')
        #---
    insert_value_to_input(INPUT1_SUFFIX, -1)
    insert_value_to_input(INPUT2_SUFFIX, -1)
    click_element(ADD_BUTTON_SUFFIX)
    actual_result = round(check_result_value(RESULT_VIEW_SUFFIX), 2)
    expected_result = round(float(-2), 1)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC01. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC01 - Add operation. Expected: {expected_result}. Observed: {actual_result}.')
    
    #-------------------------------
    insert_value_to_input(INPUT1_SUFFIX, 1)
    insert_value_to_input(INPUT2_SUFFIX, 0)
    click_element(ADD_BUTTON_SUFFIX)
    actual_result = round(check_result_value(RESULT_VIEW_SUFFIX), 2)
    expected_result = round(float(1), 1)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC01. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC01 - Add operation. Expected: {expected_result}. Observed: {actual_result}.')
    #-------------------------------
    insert_value_to_input(INPUT1_SUFFIX, -1)
    insert_value_to_input(INPUT2_SUFFIX, 0)
    click_element(ADD_BUTTON_SUFFIX)
    actual_result = round(check_result_value(RESULT_VIEW_SUFFIX), 2)
    expected_result = round(float(-1), 1)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC01. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC01 - Add operation. Expected: {expected_result}. Observed: {actual_result}.')
    #-------------------------------
    insert_value_to_input(INPUT1_SUFFIX, 0)
    insert_value_to_input(INPUT2_SUFFIX, 1)
    click_element(ADD_BUTTON_SUFFIX)
    actual_result = round(check_result_value(RESULT_VIEW_SUFFIX), 2)
    expected_result = round(float(1), 1)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC01. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC01 - Add operation. Expected: {expected_result}. Observed: {actual_result}.')
    #-------------------------------
    insert_value_to_input(INPUT1_SUFFIX, 0)
    insert_value_to_input(INPUT2_SUFFIX, -1)
    click_element(ADD_BUTTON_SUFFIX)
    actual_result = round(check_result_value(RESULT_VIEW_SUFFIX), 2)
    expected_result = round(float(-1), 1)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC01. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC01 - Add operation. Expected: {expected_result}. Observed: {actual_result}.')
    #-------------------------------
    insert_value_to_input(INPUT1_SUFFIX, 0.01)
    insert_value_to_input(INPUT2_SUFFIX, 0.00)
    click_element(ADD_BUTTON_SUFFIX)
    actual_result = round(check_result_value(RESULT_VIEW_SUFFIX), 2)
    expected_result = round(0.01, 2)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC01. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC01 - Add operation. Expected: {expected_result}. Observed: {actual_result}.')
    #-------------------------------
    insert_value_to_input(INPUT1_SUFFIX, -0.01)
    insert_value_to_input(INPUT2_SUFFIX, 0.00)
    click_element(ADD_BUTTON_SUFFIX)
    actual_result = round(check_result_value(RESULT_VIEW_SUFFIX), 2)
    expected_result = round(-0.01, 2)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC01. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC01 - Add operation. Expected: {expected_result}. Observed: {actual_result}.')
    #-------------------------------
    insert_value_to_input(INPUT1_SUFFIX, 0.00)
    insert_value_to_input(INPUT2_SUFFIX, 0.01)
    click_element(ADD_BUTTON_SUFFIX)
    actual_result = round(check_result_value(RESULT_VIEW_SUFFIX), 2)
    expected_result = round(0.01, 2)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC01. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC01 - Add operation. Expected: {expected_result}. Observed: {actual_result}.')
    #-------------------------------
    insert_value_to_input(INPUT1_SUFFIX, 0.00)
    insert_value_to_input(INPUT2_SUFFIX, -0.01)
    click_element(ADD_BUTTON_SUFFIX)
    actual_result = round(check_result_value(RESULT_VIEW_SUFFIX), 2)
    expected_result = round(-0.01, 2)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC01. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC01 - Add operation. Expected: {expected_result}. Observed: {actual_result}.')
    #-------------------------------
    insert_value_to_input(INPUT1_SUFFIX, 0.01)
    insert_value_to_input(INPUT2_SUFFIX, 0.01)
    click_element(ADD_BUTTON_SUFFIX)
    actual_result = round(check_result_value(RESULT_VIEW_SUFFIX), 2)
    expected_result = round(0.02, 2)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC01. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC01 - Add operation. Expected: {expected_result}. Observed: {actual_result}.')
    #-------------------------------
    insert_value_to_input(INPUT1_SUFFIX, 1)
    insert_value_to_input(INPUT2_SUFFIX, 1)
    click_element(ADD_BUTTON_SUFFIX)
    actual_result = round(check_result_value(RESULT_VIEW_SUFFIX), 2)
    expected_result = round(float(2), 1)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC01. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC01 - Add operation. Expected: {expected_result}. Observed: {actual_result}.')
    #-------------------------------
    insert_value_to_input(INPUT1_SUFFIX, 999999999)
    insert_value_to_input(INPUT2_SUFFIX, 999999999)
    click_element(ADD_BUTTON_SUFFIX)
    actual_result = round(check_result_value(RESULT_VIEW_SUFFIX), 2)
    expected_result = round(float(1999999998), 1)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC01. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC01 - Add operation. Expected: {expected_result}. Observed: {actual_result}.')
    #---
    insert_value_to_input(INPUT1_SUFFIX, -999999999)
    insert_value_to_input(INPUT2_SUFFIX, -999999999)
    click_element(ADD_BUTTON_SUFFIX)
    actual_result = round(check_result_value(RESULT_VIEW_SUFFIX), 2)
    expected_result = round(float(-1999999998), 1)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC01. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC01 - Add operation. Expected: {expected_result}. Observed: {actual_result}.')
    #---
    insert_value_to_input(INPUT1_SUFFIX, 0)
    insert_value_to_input(INPUT2_SUFFIX, 0)
    click_element(ADD_BUTTON_SUFFIX)
    actual_result = round(check_result_value(RESULT_VIEW_SUFFIX), 2)
    expected_result = round(float(0), 1)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC01. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC01 - Add operation. Expected: {expected_result}. Observed: {actual_result}.')

def TC02_check_substract_operation():
    '''Tests substract aperation with precision to 2 decimal points'''
    connect_to_the_device()
    start_app()

    #---
    insert_value_to_input(INPUT1_SUFFIX, 1)
    insert_value_to_input(INPUT2_SUFFIX, 1)
    click_element(SUBSTRACT_BUTTON_SUFFIX)
    actual_result = round(check_result_value(RESULT_VIEW_SUFFIX), 2)
    expected_result = round(float(0), 1)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC02. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC02 - Substract operation. Expected: {expected_result}. Observed: {actual_result}.')
    
    #-------------------------------
    insert_value_to_input(INPUT1_SUFFIX, -1)
    insert_value_to_input(INPUT2_SUFFIX, -1)
    click_element(SUBSTRACT_BUTTON_SUFFIX)
    actual_result = round(check_result_value(RESULT_VIEW_SUFFIX), 2)
    expected_result = round(float(0), 1)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC02. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC02 - Substract operation. Expected: {expected_result}. Observed: {actual_result}.')
    
    #-------------------------------
    insert_value_to_input(INPUT1_SUFFIX, 1)
    insert_value_to_input(INPUT2_SUFFIX, 0)
    click_element(SUBSTRACT_BUTTON_SUFFIX)
    actual_result = round(check_result_value(RESULT_VIEW_SUFFIX), 2)
    expected_result = round(float(1), 1)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC02. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC02 - Substract operation. Expected: {expected_result}. Observed: {actual_result}.')
    #-------------------------------
    insert_value_to_input(INPUT1_SUFFIX, -1)
    insert_value_to_input(INPUT2_SUFFIX, 0)
    click_element(SUBSTRACT_BUTTON_SUFFIX)
    actual_result = round(check_result_value(RESULT_VIEW_SUFFIX), 2)
    expected_result = round(float(-1), 1)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC02. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC02 - Substract operation. Expected: {expected_result}. Observed: {actual_result}.')
    #-------------------------------
    insert_value_to_input(INPUT1_SUFFIX, 0)
    insert_value_to_input(INPUT2_SUFFIX, 1)
    click_element(SUBSTRACT_BUTTON_SUFFIX)
    actual_result = round(check_result_value(RESULT_VIEW_SUFFIX), 2)
    expected_result = round(float(-1), 1)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC02. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC02 - Substract operation. Expected: {expected_result}. Observed: {actual_result}.')
    #-------------------------------
    insert_value_to_input(INPUT1_SUFFIX, 0.01)
    insert_value_to_input(INPUT2_SUFFIX, 0.00)
    click_element(SUBSTRACT_BUTTON_SUFFIX)
    actual_result = round(check_result_value(RESULT_VIEW_SUFFIX), 2)
    expected_result = round(0.01, 2)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC02. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC02 - Substract operation. Expected: {expected_result}. Observed: {actual_result}.')
    #-------------------------------
    insert_value_to_input(INPUT1_SUFFIX, 0.00)
    insert_value_to_input(INPUT2_SUFFIX, 0.01)
    click_element(SUBSTRACT_BUTTON_SUFFIX)
    actual_result = round(check_result_value(RESULT_VIEW_SUFFIX), 2)
    expected_result = round(-0.01, 2)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC02. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC02 - Substract operation. Expected: {expected_result}. Observed: {actual_result}.')
    #-------------------------------
    insert_value_to_input(INPUT1_SUFFIX, 0.00)
    insert_value_to_input(INPUT2_SUFFIX, -0.01)
    click_element(SUBSTRACT_BUTTON_SUFFIX)
    actual_result = round(check_result_value(RESULT_VIEW_SUFFIX), 2)
    expected_result = round(0.01, 2)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC02. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC02 - Substract operation. Expected: {expected_result}. Observed: {actual_result}.')
    #-------------------------------
    insert_value_to_input(INPUT1_SUFFIX, 0.01)
    insert_value_to_input(INPUT2_SUFFIX, 0.01)
    click_element(SUBSTRACT_BUTTON_SUFFIX)
    actual_result = round(check_result_value(RESULT_VIEW_SUFFIX), 2)
    expected_result = round(0, 1)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC02. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC02 - Substract operation. Expected: {expected_result}. Observed: {actual_result}.')
    #-------------------------------
    insert_value_to_input(INPUT1_SUFFIX, -0.01)
    insert_value_to_input(INPUT2_SUFFIX, 0.01)
    click_element(SUBSTRACT_BUTTON_SUFFIX)
    actual_result = round(check_result_value(RESULT_VIEW_SUFFIX), 2)
    expected_result = round(float(-0.02), 2)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC02. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC02 - Substract operation. Expected: {expected_result}. Observed: {actual_result}.')
    #-------------------------------
    insert_value_to_input(INPUT1_SUFFIX, 1)
    insert_value_to_input(INPUT2_SUFFIX, 1)
    click_element(SUBSTRACT_BUTTON_SUFFIX)
    actual_result = round(check_result_value(RESULT_VIEW_SUFFIX), 2)
    expected_result = round(float(0), 1)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC02. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC02 - Substract operation. Expected: {expected_result}. Observed: {actual_result}.')
    #-------------------------------
    insert_value_to_input(INPUT1_SUFFIX, 999999999)
    insert_value_to_input(INPUT2_SUFFIX, 999999999)
    click_element(SUBSTRACT_BUTTON_SUFFIX)
    actual_result = round(check_result_value(RESULT_VIEW_SUFFIX), 2)
    expected_result = round(float(0), 1)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC02. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC02 - Substract operation. Expected: {expected_result}. Observed: {actual_result}.')
    #---
    insert_value_to_input(INPUT1_SUFFIX, 0)
    insert_value_to_input(INPUT2_SUFFIX, 0)
    click_element(SUBSTRACT_BUTTON_SUFFIX)
    actual_result = round(check_result_value(RESULT_VIEW_SUFFIX), 2)
    expected_result = round(float(0), 1)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC02. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC02 - Substract operation. Expected: {expected_result}. Observed: {actual_result}.')
    #---
    insert_value_to_input(INPUT1_SUFFIX, 0)
    insert_value_to_input(INPUT2_SUFFIX, 999999999)
    click_element(SUBSTRACT_BUTTON_SUFFIX)
    actual_result = round(check_result_value(RESULT_VIEW_SUFFIX), 2)
    expected_result = round(float(-999999999), 1)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC02. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC02 - Substract operation. Expected: {expected_result}. Observed: {actual_result}.')

def TC03_check_divide_operation():
    '''Tests divide aperation with precision to 2 decimal points'''
    connect_to_the_device()
    start_app()

    #---
    insert_value_to_input(INPUT1_SUFFIX, 1)
    insert_value_to_input(INPUT2_SUFFIX, 1)
    click_element(DIVIDE_BUTTON_SUFFIX)
    actual_result = check_result_value(RESULT_VIEW_SUFFIX)
    expected_result = round(float(1), 1)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC03. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC03 - Divide operation. Expected: {expected_result}. Observed: {actual_result}.')
    
    #-------------------------------
    insert_value_to_input(INPUT1_SUFFIX, 1)
    insert_value_to_input(INPUT2_SUFFIX, 0)
    click_element(DIVIDE_BUTTON_SUFFIX)
    actual_result = check_result_value(RESULT_VIEW_SUFFIX)
    expected_result = "Error: invalid operation"
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC03. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC03 - Divide operation. Expected: {expected_result}. Observed: {actual_result}.')
    #-------------------------------
    insert_value_to_input(INPUT1_SUFFIX, 0)
    insert_value_to_input(INPUT2_SUFFIX, 1)
    click_element(DIVIDE_BUTTON_SUFFIX)
    actual_result = check_result_value(RESULT_VIEW_SUFFIX)
    expected_result = round(float(0), 1)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC03. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC03 - Divide operation. Expected: {expected_result}. Observed: {actual_result}.')
    #-------------------------------
    insert_value_to_input(INPUT1_SUFFIX, 0.01)
    insert_value_to_input(INPUT2_SUFFIX, 0.00)
    click_element(DIVIDE_BUTTON_SUFFIX)
    actual_result = check_result_value(RESULT_VIEW_SUFFIX)
    expected_result = "Error: invalid operation"
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC03. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC03 - Divide operation. Expected: {expected_result}. Observed: {actual_result}.')
    #-------------------------------
    insert_value_to_input(INPUT1_SUFFIX, 0.00)
    insert_value_to_input(INPUT2_SUFFIX, 0.01)
    click_element(DIVIDE_BUTTON_SUFFIX)
    actual_result = check_result_value(RESULT_VIEW_SUFFIX)
    expected_result = round(0, 1)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC03. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC03 - Divide operation. Expected: {expected_result}. Observed: {actual_result}.')
    #-------------------------------
    insert_value_to_input(INPUT1_SUFFIX, 0.01)
    insert_value_to_input(INPUT2_SUFFIX, 0.01)
    click_element(DIVIDE_BUTTON_SUFFIX)
    actual_result = check_result_value(RESULT_VIEW_SUFFIX)
    expected_result = round(1, 1)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC03. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC03 - Divide operation. Expected: {expected_result}. Observed: {actual_result}.')
    #-------------------------------
    insert_value_to_input(INPUT1_SUFFIX, 1)
    insert_value_to_input(INPUT2_SUFFIX, 1)
    click_element(DIVIDE_BUTTON_SUFFIX)
    actual_result = check_result_value(RESULT_VIEW_SUFFIX)
    expected_result = round(float(1), 1)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC03. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC03 - Divide operation. Expected: {expected_result}. Observed: {actual_result}.')
    #-------------------------------
    insert_value_to_input(INPUT1_SUFFIX, 999999999)
    insert_value_to_input(INPUT2_SUFFIX, 999999999)
    click_element(DIVIDE_BUTTON_SUFFIX)
    actual_result = check_result_value(RESULT_VIEW_SUFFIX)
    expected_result = round(float(1), 1)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC03. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC03 - Divide operation. Expected: {expected_result}. Observed: {actual_result}.')
    #---
    insert_value_to_input(INPUT1_SUFFIX, 0)
    insert_value_to_input(INPUT2_SUFFIX, 0)
    click_element(DIVIDE_BUTTON_SUFFIX)
    actual_result = check_result_value(RESULT_VIEW_SUFFIX)
    expected_result = "Error: invalid operation"
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC03. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC03 - Divide operation. Expected: {expected_result}. Observed: {actual_result}.')
    #---
    insert_value_to_input(INPUT1_SUFFIX, 0)
    insert_value_to_input(INPUT2_SUFFIX, 999999999)
    click_element(DIVIDE_BUTTON_SUFFIX)
    actual_result = check_result_value(RESULT_VIEW_SUFFIX)
    expected_result = round(float(0), 1)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC03. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC03 - Divide operation. Expected: {expected_result}. Observed: {actual_result}.')
    #---
    insert_value_to_input(INPUT1_SUFFIX, 1)
    insert_value_to_input(INPUT2_SUFFIX, 3)
    click_element(DIVIDE_BUTTON_SUFFIX)
    actual_result = check_result_value(RESULT_VIEW_SUFFIX)
    expected_result = round(float(0.33), 2)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC03. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC03 - Divide operation. Expected: {expected_result}. Observed: {actual_result}.')

def TC04_check_multiply_operation():
    '''Tests multiply aperation with precision to 2 decimal points'''
    connect_to_the_device()
    start_app()

    #---
    insert_value_to_input(INPUT1_SUFFIX, 1)
    insert_value_to_input(INPUT2_SUFFIX, 1)
    click_element(MULTIPLY_BUTTON_SUFFIX)
    actual_result = check_result_value(RESULT_VIEW_SUFFIX)
    expected_result = round(float(1), 1)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC04. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC04 - Multiply operation. Expected: {expected_result}. Observed: {actual_result}.')
    
    #-------------------------------
    insert_value_to_input(INPUT1_SUFFIX, 1)
    insert_value_to_input(INPUT2_SUFFIX, -1)
    click_element(MULTIPLY_BUTTON_SUFFIX)
    actual_result = check_result_value(RESULT_VIEW_SUFFIX)
    expected_result = round(float(-1), 1)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC04. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC04 - Multiply operation. Expected: {expected_result}. Observed: {actual_result}.')
    
    #-------------------------------
    insert_value_to_input(INPUT1_SUFFIX, 1)
    insert_value_to_input(INPUT2_SUFFIX, 0)
    click_element(MULTIPLY_BUTTON_SUFFIX)
    actual_result = check_result_value(RESULT_VIEW_SUFFIX)
    expected_result = round(0, 1)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC04. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC04 - Multiply operation. Expected: {expected_result}. Observed: {actual_result}.')
    #-------------------------------
    insert_value_to_input(INPUT1_SUFFIX, 0)
    insert_value_to_input(INPUT2_SUFFIX, 1)
    click_element(MULTIPLY_BUTTON_SUFFIX)
    actual_result = check_result_value(RESULT_VIEW_SUFFIX)
    expected_result = round(0, 1)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC04. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC04 - Multiply operation. Expected: {expected_result}. Observed: {actual_result}.')
    #-------------------------------
    insert_value_to_input(INPUT1_SUFFIX, 0.01)
    insert_value_to_input(INPUT2_SUFFIX, 0.00)
    click_element(MULTIPLY_BUTTON_SUFFIX)
    actual_result = check_result_value(RESULT_VIEW_SUFFIX)
    expected_result = round(0, 1)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC04. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC04 - Multiply operation. Expected: {expected_result}. Observed: {actual_result}.')
    #-------------------------------
    insert_value_to_input(INPUT1_SUFFIX, 0.00)
    insert_value_to_input(INPUT2_SUFFIX, 0.01)
    click_element(MULTIPLY_BUTTON_SUFFIX)
    actual_result = check_result_value(RESULT_VIEW_SUFFIX)
    expected_result = round(0, 1)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC04. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC04 - Multiply operation. Expected: {expected_result}. Observed: {actual_result}.')
    #-------------------------------
    insert_value_to_input(INPUT1_SUFFIX, 0.00)
    insert_value_to_input(INPUT2_SUFFIX, -0.01)
    click_element(MULTIPLY_BUTTON_SUFFIX)
    actual_result = check_result_value(RESULT_VIEW_SUFFIX)
    expected_result = round(0, 1)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC04. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC04 - Multiply operation. Expected: {expected_result}. Observed: {actual_result}.')
    #-------------------------------
    insert_value_to_input(INPUT1_SUFFIX, 0.01)
    insert_value_to_input(INPUT2_SUFFIX, 0.01)
    click_element(MULTIPLY_BUTTON_SUFFIX)
    actual_result = check_result_value(RESULT_VIEW_SUFFIX)
    expected_result = round(float(0.0001), 4)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC04. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC04 - Multiply operation. Expected: {expected_result}. Observed: {actual_result}.')
    #-------------------------------
    insert_value_to_input(INPUT1_SUFFIX, 1)
    insert_value_to_input(INPUT2_SUFFIX, 1)
    click_element(MULTIPLY_BUTTON_SUFFIX)
    actual_result = check_result_value(RESULT_VIEW_SUFFIX)
    expected_result = round(float(1), 1)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC04. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC04 - Multiply operation. Expected: {expected_result}. Observed: {actual_result}.')
    #-------------------------------
    insert_value_to_input(INPUT1_SUFFIX, 1000000)
    insert_value_to_input(INPUT2_SUFFIX, 999999999)
    click_element(MULTIPLY_BUTTON_SUFFIX)
    actual_result = check_result_value(RESULT_VIEW_SUFFIX)
    expected_result = round(float(999999999000000), 1)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC04. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC04 - Multiply operation. Expected: {expected_result}. Observed: {actual_result}.')
    #---
    insert_value_to_input(INPUT1_SUFFIX, 0)
    insert_value_to_input(INPUT2_SUFFIX, 0)
    click_element(MULTIPLY_BUTTON_SUFFIX)
    actual_result = check_result_value(RESULT_VIEW_SUFFIX)
    expected_result = round(0, 1)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC04. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC04 - Multiply operation. Expected: {expected_result}. Observed: {actual_result}.')
    #---
    insert_value_to_input(INPUT1_SUFFIX, 0)
    insert_value_to_input(INPUT2_SUFFIX, 999999999)
    click_element(MULTIPLY_BUTTON_SUFFIX)
    actual_result = check_result_value(RESULT_VIEW_SUFFIX)
    expected_result = round(0, 1)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC04. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC04 - Multiply operation. Expected: {expected_result}. Observed: {actual_result}.')
    #---
    insert_value_to_input(INPUT1_SUFFIX, 0)
    insert_value_to_input(INPUT2_SUFFIX, -999999999)
    click_element(MULTIPLY_BUTTON_SUFFIX)
    actual_result = check_result_value(RESULT_VIEW_SUFFIX)
    expected_result = round(0, 1)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC04. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC04 - Multiply operation. Expected: {expected_result}. Observed: {actual_result}.')
    #---
    insert_value_to_input(INPUT1_SUFFIX, 1)
    insert_value_to_input(INPUT2_SUFFIX, 3)
    click_element(MULTIPLY_BUTTON_SUFFIX)
    actual_result = check_result_value(RESULT_VIEW_SUFFIX)
    expected_result = round(3, 1)
    try:
        assert actual_result == expected_result, 'Operation is not correct'
    except AssertionError as error:
        print(f'FAILED - TC04. Error: {error}. Expected: {expected_result}. Observed: {actual_result}.')
    else:
        print(f'PASSED - TC04 - Multiply operation. Expected: {expected_result}. Observed: {actual_result}.')

if __name__ == "__main__":

    TC01_check_add_operation()
    TC02_check_substract_operation()
    TC03_check_divide_operation()
    TC04_check_multiply_operation()