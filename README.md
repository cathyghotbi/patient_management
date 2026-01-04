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


For the Behavior-Driven Development (BDD) tests, there are 2 folders:
.feature files → human-readable behavior (Plain English - in gherkin)
steps/*.py → Python code that executes behavior (Python logic)

pycharm configuration to run behave test:
<img width="326" height="162" alt="{DAC0479A-1F17-4517-B466-933879FD7D27}" src="https://github.com/user-attachments/assets/5bf22fc9-bfc8-4120-a001-3badce77b243" />


result of the behave test run:
<img width="694" height="479" alt="{9EB1DAAC-27A4-4FB9-A6C8-BCBCEABD5A61}" src="https://github.com/user-attachments/assets/f427e178-f1d2-442e-a0d3-69f739323492" />
