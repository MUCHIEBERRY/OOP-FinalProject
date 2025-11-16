## Development Progress and Collaboration Setup 

This week focused on establishing the complete development workflow for our project, setting up the environment for all members, creating the initial class structure, and ensuring that everyone could collaborate smoothly within the repository.

## 1. Initial Struggles With Environment Setup

The process began with several difficulties in finding a consistent workspace that all group members could use. My first approach was to set up a collaborative environment using Visual Studio Code. However, this turned out to be more complicated than expected. I encountered problems with Python interpreters not being detected, Jupyter not connecting, and VSCode not resetting even after uninstalling and reinstalling it.

At this stage, I was stuck switching between different solutions, trying to fix kernels, interpreter paths, Git integration, and extensions that refused to load. These issues consumed a lot of time and caused delays because I couldn't proceed with building the project structure until the coding environment was stable.

<img width="1417" height="328" alt="vscode-error" src="https://github.com/user-attachments/assets/2402e100-2dc6-4e87-8713-16a869eaab90" />

## 2. Transitioning to Jupyter Notebook as the Main Workspace

After hours of trying to fix Visual Studio Code, I realized it was more efficient to return to something the group was already comfortable with: Jupyter Notebook using Anaconda.

I reorganized the repository so that:

- Each member had their own Jupyter Notebook inside the notebooks/ folder

- The main OOP library (DataHabit/) remained separate with the .py files

- Everyone could write and test code without breaking the main structure

This made the workflow clear and beginner-friendly while still following proper modular coding.

<img width="1862" height="849" alt="Screenshot 2025-11-14 122716" src="https://github.com/user-attachments/assets/f2754e0a-c43e-4760-b029-3b92dddad692" />

<img width="1874" height="865" alt="Screenshot 2025-11-09 124300" src="https://github.com/user-attachments/assets/70b348e7-c161-4cbd-bd1c-c50aea658ea9" />

## 3. Setting Up Collaboration Through GitHub

The next challenge was enabling real collaboration. Since I am the repository owner, I added all members as collaborators. However, simply being collaborators doesn't show their contribution logs unless they commit through their own accounts.

To solve this, I instructed everyone to fork the main repository so their names would appear in GitHub Insights when they contributed.

I even created a second GitHub account and added it as a collaborator to test the workflow from their point of view. I used that account to record a full video tutorial so my groupmates would clearly understand how to:

- Fork the repo

- Open their Jupyter Notebook

- Edit and save

- Commit changes

- Push updates

- Make pull requests back to the main repo

- This ensured that everyone could contribute individually while keeping the main project organized.

<img width="1919" height="695" alt="Screenshot 2025-11-16 005029" src="https://github.com/user-attachments/assets/29cf841f-d175-4074-b31f-d990a0645e92" />

<img width="1390" height="924" alt="Screenshot 2025-11-16 005153" src="https://github.com/user-attachments/assets/c8caccae-c478-4617-b4af-3e406cca9389" />

## 4. Building the Main OOP Structure

As group leader, I took responsibility for setting up the entire backbone of the project. I created the full folder structure, the __init__.py file, and the initial .py scripts inside the DataHabit/ directory:

task_data.py, behavior_analyzer.py, visualizer.py

I wrote the docstrings, imports, and base validations so the rest of the group could build their assigned parts. This included ensuring everything matched our UML diagram, deciding naming conventions, and implementing protected attributes for clarity and professionalism.

I also prepared a testing notebook to verify that the imports worked and the module structure was correct.

<img width="1916" height="936" alt="Screenshot 2025-11-09 114331" src="https://github.com/user-attachments/assets/f59f7a37-19ce-4b05-b6d2-94772e699810" />

<img width="1916" height="1198" alt="Screenshot 2025-11-09 124651" src="https://github.com/user-attachments/assets/5945b433-6623-43b7-a07c-b9f1b9f2bc53" />

## 5. TaskData Class Development

This week focused on developing the internal logic of the TaskData class that our leader had prepared. The backbone of the file — its attributes, basic method structure, and documentation was already in place. My main responsibility was to implement the full functionality, test each behavior, and resolve the issues that appeared as I made the class operational.

When I opened the file, the TaskData class contained the basic constructor and empty methods that served as the foundation for my work. Using this structure, I started implementing the logic for handling submission timestamps, computing delays, and producing readable output for testing. The first version I created focused on converting timestamp strings into datetime objects. I implemented the constructor, wrote the initial parse_timestamp() method, added a get_delay() calculation, and created a simple __repr__() method to check if the values were stored correctly.

<img width="842" height="496" alt="Screenshot 2025-11-14 130048" src="https://github.com/user-attachments/assets/8719532c-9b10-41ed-87f5-5a7cc0ae0566" />

#### **Testing the First Working Version**
After completing the initial implementation, I ran tests to verify whether the class worked as intended. I created a sample TaskData object, printed the representation, called the parsing method, and checked if the delay computation produced the correct number of hours. The class performed correctly when the timestamp followed the format "YYYY-MM-DD HH:MM:SS", and the outputs matched the calculations I expected.

<img width="604" height="273" alt="Screenshot 2025-11-14 130056" src="https://github.com/user-attachments/assets/38d639f8-b08b-4805-92ac-fc47fce8db4d" />

#### **Issue Encountered**

As soon as the early tests succeeded, we noticed a potential issue: the class depended entirely on the correctness of the timestamp string. If a user entered even a small formatting error, parsing would fail and stop the program. Additionally, this version did not support cases where timestamps are already in datetime form, such as using datetime.now() in real-time submissions.

Our leader pointed out that relying on strict formatting could eventually cause errors once other modules interact with this class. This gave me the direction to improve the method further.

#### **Improving Flexibility**
To address these concerns, I redesigned the parsing logic to make the class more flexible and safer to use. I updated parse_timestamp() so that it can now recognize two types of inputs:
- A string following the correct timestamp format
- A datetime object, including values generated using datetime.now()

The revised version begins by checking what type of data the user passed. If the submission time is already a datetime, the class keeps it as-is. If it is a string, the method attempts to parse it safely. This prevents unnecessary errors, and makes the class compatible with both manual inputs and automated timestamps. This improvement ensures that the class is durable enough to be used throughout the project without breaking when different modules feed it data.

#### **Encountering Another Set of Errors**
During another testing of the class, several errors appeared. These errors were important because they helped me understand which parts of the logic needed refinement. The first issue occurred when creating a TaskData object:

<img width="1027" height="498" alt="Screenshot 2025-11-14 132131" src="https://github.com/user-attachments/assets/02e322ce-47c2-4821-bdfd-008e786bfe51" />

**TypeError:** “parse_timestamp() takes 1 positional argument but 2 were given”

This error happened because the constructor passed the submission time into the method, but my method definition did not accept any parameters besides self. This mismatch caused Python to treat the extra value as an unexpected argument. Fixing this required updating my method to properly accept and handle the timestamp value. After correcting the method signature, a second error appeared when I tried parsing the timestamp. This occurred because the variable timestamp_str had not been assigned inside the method. The issue reminded me that every variable used inside a function must be explicitly defined before it can be processed. Once I assigned the value correctly, the method worked as intended. These errors were helpful checkpoints as they showed which parts of the logic needed clearer structure and which values needed proper handling before they could be parsed.

#### **Progress and Reflection** 

By the end of the week, the TaskData class became fully functional and more resilient than the initial version. It now accepts both string-based and automatically generated timestamps, supports parsing, and computes delays accurately.

<img width="1042" height="383" alt="Screenshot 2025-11-16 183008" src="https://github.com/user-attachments/assets/d407eeb0-9753-4888-9413-a2154be29242" />

Working on this part helped me understand how small decisions can affect the reliability of the entire system. It also showed me the importance of planning ahead for potential user errors.

## 6. Data Cleaning and Support Functions

## 7. Visualizer Structure and Plot Placeholders
**Development Updates**
This week, I was assigned by our task leader to develop the Visualizer class, which is responsible for generating graphs that show submission patterns and productivity levels of each student. When I opened the Jupyter notebook stored in our GitHub repository, I saw that a basic constructor and placeholder methods were already prepared. This initial structure helped me understand how the visualizer should function and what outputs it should produce.

The primary functions I worked on were:
	•	**plot_timeline()** – This method visualizes the trend of submissions over time using a line graph.
	•	**plot_summary()** – This summarizes weekly productivity using a bar chart.
	•	**__eq__()** – A comparison method that checks whether two datasets have the same total productivity score.

After completing the initial code, I tested my visulaizer class using a sample dataset:


## 8. BehaviorAnalyzer Development

## 9. Use of Resources and Research Transparency

As part of the development process, we made use of several online resources to understand the concepts, troubleshoot errors, and refine our implementation. Our goal was to learn effectively and apply the principles correctly, not to copy solutions blindly.

We practiced honesty throughout the development by acknowledging the tools that helped us:

**ChatGPT (as a Learning Assistant)**

We used ChatGPT mainly for:

- Clarifying OOP concepts

- Understanding Python syntax and module structure

- Troubleshooting errors (e.g., import paths, environment setup, Jupyter issues)

- Getting explanations or breakdowns of ideas we wanted to implement

The code written in the project was created manually by the group, based on our understanding. ChatGPT served as a guide to help us learn faster and avoid confusion, especially when dealing with imports, class relationships, and file organization.

**Google (Documentation & Error Research)**

We also searched through Google to explore:

- Python documentation for datetime, classes, and modules

- GitHub workflow explanations

- Common solutions to ModuleNotFoundError and path issues

These helped us understand technical details better.

**YouTube Tutorials**

Some members also referred to YouTube videos for:

- How to use GitHub (forking, pull requests, commits)

- Basic Python OOP tutorials

- How to structure Python packages

These videos supported our individual learning, especially for those who were new to Git, GitHub, or Python modules.

**Class Resources & Provided Materials**

We followed the rubric, UML diagram, and OOP requirements provided by our instructor, ensuring the project stayed aligned with the expected outcomes.







