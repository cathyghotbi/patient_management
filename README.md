The program starts by loading patient data from a JSON file, then repeatedly displays a menu.
Based on the user’s choice, it performs actions such as searching, filtering, grouping, or saving data.
The loop continues until the user selects Exit.

The project is organized into folders based on responsibility: 
models store data structures, 
services handle logic, 
UI handles input/output, 
and the main file controls the program flow.


example of how it works:

<img width="609" height="412" alt="{C7627AFA-0FC5-4DD6-9867-FDC0526B29B8}" src="https://github.com/user-attachments/assets/19f6fc3a-83a8-4851-8ae6-ef09c9105a2d" />


<img width="616" height="467" alt="{FE3090CD-A2E2-48F6-AA2F-3A6DAB66F88B}" src="https://github.com/user-attachments/assets/38d234a8-87ee-4410-96a6-dccc5df2f006" />


There are also unit tests. In order to run the test, Python needs to know where the project root is, so:
In PyCharm, right-click the patient_management folder
Click “Mark Directory as”
Click “Sources Root”

<img width="736" height="435" alt="{7088E8A0-ECB4-440A-AABA-C9AD372C274D}" src="https://github.com/user-attachments/assets/ff670dcc-3e78-43f7-98dc-63f2776a9689" />


Behavior-Driven Development (BDD) are used to to validate system behavior using Given–When–Then scenarios.
In BDD tests, there are 2 folders:
.feature files → human-readable behavior (Plain English - in gherkin)
steps/*.py → Python code that executes behavior (Python logic)

pycharm configuration to run behave test:

<img width="326" height="162" alt="{DAC0479A-1F17-4517-B466-933879FD7D27}" src="https://github.com/user-attachments/assets/5bf22fc9-bfc8-4120-a001-3badce77b243" />


result of the behave test run:

<img width="694" height="479" alt="{9EB1DAAC-27A4-4FB9-A6C8-BCBCEABD5A61}" src="https://github.com/user-attachments/assets/f427e178-f1d2-442e-a0d3-69f739323492" />


If you would like to tag the tests and run only those, to have to set the configuration to run only those 

--tags=smoke -f pretty features

<img width="360" height="148" alt="{1DFBE492-7805-46CF-A3F2-506309A0DE52}" src="https://github.com/user-attachments/assets/4c96f883-13b0-4b61-9d70-d53565d78449" />


<img width="471" height="458" alt="{7BFE27D7-E3C0-4310-B8E7-E7422E82BEE7}" src="https://github.com/user-attachments/assets/3d0ce657-8655-4486-8441-6d186dbec425" />

COVERAGE REPORTS (Unit + BDD):
in pycharm terminal:

directory: C:\Users\Cathy\PycharmProjects\pythonProject1\patient_management>

pip install coverage

coverage run -m unittest discover
coverage report

<img width="336" height="241" alt="{8F544803-27E6-4663-979A-7FA78C1758C5}" src="https://github.com/user-attachments/assets/ab54f05c-55e1-4ab1-9dae-596a4d2d6b41" />


coverage run -m behave
coverage report



coverage html

htmlcov/index.html

<img width="506" height="385" alt="{1B5D2793-165E-4BA3-AC16-7E49045E7D57}" src="https://github.com/user-attachments/assets/8f3af6bd-d0fe-487c-bd8d-bcd47f4e7e2b" />


<img width="426" height="472" alt="{8F8742AD-9018-4B9F-BDF7-DB3027978879}" src="https://github.com/user-attachments/assets/000d3d6e-207b-4be3-980a-ff3ea8bc8bad" />
