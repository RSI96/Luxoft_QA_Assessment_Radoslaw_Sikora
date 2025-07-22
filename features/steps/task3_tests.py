from behave import *
from task1_mobile_app_test import start_app, connect_to_the_device, insert_value_to_input, click_element, check_result_value
from task1_mobile_app_test import INPUT1_SUFFIX, INPUT2_SUFFIX, ADD_BUTTON_SUFFIX, RESULT_VIEW_SUFFIX

@given("App is running")
def given_app(context):
    connect_to_the_device()
    start_app()

@when(u'Numbers {num1} and {num2} are given')
def when_input_values_are_given(context, num1, num2):
    insert_value_to_input(INPUT1_SUFFIX, num1)
    insert_value_to_input(INPUT2_SUFFIX, num2)
    click_element(ADD_BUTTON_SUFFIX)
    context.actual_result = round(check_result_value(RESULT_VIEW_SUFFIX), 2)

@then(u'Result should be {expected_result}')
def then_check_result(context, expected_result):
    expected_result = round(float(expected_result), 1)
    assert(context.actual_result == expected_result)