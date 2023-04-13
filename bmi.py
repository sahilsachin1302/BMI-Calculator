from pywebio.input import *
from pywebio.output import *
from pywebio import start_server

def bmi_calculator():
    while True:
        info = input_group('BMI Calculator',
                           [
                            input('Enter your name', name='name'),
                            input('Enter your age', type=NUMBER, name='age'),
                            input('Enter your weight (in kg)', type=FLOAT, name='weight'),
                            input('Enter your height (in cm)', type=FLOAT, name='height'),
                           ]
                          )
        name = info['name']
        age = info['age']
        weight = info['weight']
        height = info['height']
        
        # BMI Calculation
        bmi = round(weight / (height/100)**2, 2)
        
        # BMI Interpretation
        if bmi < 18.5:
            interpretation = 'Underweight'
        elif bmi >= 18.5 and bmi <= 24.9:
            interpretation = 'Normal weight'
        elif bmi >= 25 and bmi <= 29.9:
            interpretation = 'Overweight'
        else:
            interpretation = 'Obese'
        
        # BMI Report
        put_markdown('# BMI Report')
        put_markdown('Name: `%s`' % name)
        put_markdown('Age: `%d`' % age)
        put_markdown('Weight: `%f kg`' % weight)
        put_markdown('Height: `%f cm`' % height)
        put_markdown('BMI: `%f`' % bmi)
        put_markdown('Interpretation: `%s`' % interpretation)

        action = select('Select an action', ['Calculate again', 'Quit'])
        if action == 'Quit':
            break

if __name__ == '__main__':
    start_server(bmi_calculator, port=80, debug=True)
