from selene.support.shared import browser
from selene import be, have
import os

def test_demoqa_3_5():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Oleg')
    browser.element('#lastName').type('Avakimyanov')
    browser.element('#userEmail').type('testqa@gmail.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('1234567890')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type("July")
    browser.element('.react-datepicker__year-select').type("2000")
    browser.element('[aria-label="Choose Tuesday, July 25th, 2000"]').click()
    browser.element('#subjectsInput').type('Computer Science').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').set_value(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, 'files/tools_qa.png')))
    browser.element('#currentAddress').type('Antares')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('#submit').press_enter()

    browser.all('.table-responsive td:nth-child(2)').should(have.texts(
        'Oleg Avakimyanov',
        'testqa@gmail.com',
        'Male',
        '1234567890',
        '25 July,2000',
        'Computer Science',
        'Sports',
        'tools_qa.png',
        'Antares',
        'NCR Delhi'))