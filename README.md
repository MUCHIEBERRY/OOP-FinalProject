# OOP-FinalProject
**Build and Publish a Python Library for Data Science**

**Objective**

Create and publish a Python library (package) that applies Object-Oriented Programming (OOP) principles to a data science application. You will collaborate as a group, manage your project on GitHub, and publish your package to PyPI, complete with documentation.

## Folders
- **Proposals/** — all concept drafts (datamood, datahabit, etc.)
- **Reports/** — weekly narrative reports and peer evaluations
- **Final Project/** — chosen library implementation
- **Docs/** — UML, screenshots, and design materials

## Members — Role — Task 
| **Name**                     | **Role/Position**             | **Main Contribution**                    |
| ---------------------------- | ----------------------------- | ---------------------------------------- |
| **Dahe, Aira Grettel C.**    | Project Lead / GitHub Manager | Repository setup, documentation, testing |
| **Dellosa, Karylle L.**      | Concept Proposer / Main Coder | Core functions for analysis              |
| **Hayag, Carmel Mariane T.** | Documentation Writer          | README and narrative reports             |
| **Java, Armisty Genia L.**   | Visualization                 | Graphs and plots                         |
| **Trillo, Rodney G.**        | Data Handler                  | Timestamp and data cleaning module       |


## Project Overview
**DataHabit** is a Python library designed to analyze academic behavior and productivity patterns based on students’ task timestamps. It reads submission records, detects time-based habits, and classifies users according to their working style—such as procrastinator, steady worker, or early finisher. By using data-driven insights, the library helps students and educators understand academic performance trends and improve time-management strategies.

## Objectives

The main goal of **DataHabit** is to provide a simple yet powerful tool for analyzing and visualizing study habits through timestamp data.
Specifically, it aims to:
1. Process and interpret task submission timestamps to identify behavioral patterns.
2. Classify students according to their productivity and consistency levels.
3. Generate summary reports and visualizations that reflect weekly academic activity.
4. Encourage self-reflection and better academic planning through data analytics.
5. Offer a reusable, open-source Python package that demonstrates Object-Oriented Programming (OOP) concepts applied to real-world data science.

## Planned Features

**Timestamp Analyzer** — classifies early, on-time, or late submissions.

**Behavior Classifier** — categorizes students (e.g., Procrastinator, Consistent Worker, etc.) based on submission trends.

**Productivity Summary** — computes weekly activity levels (average submission gap, count, etc.).

**Visualizer** — generates simple graphs for time patterns (optional but nice!).

**Data Cleaner/Utility** — handles missing timestamps or incorrect date formats.

## Initial Class Design
The **DataHabit** library is built using Object-Oriented Programming (OOP) principles.
It consists of several interconnected classes that handle data parsing, behavior classification, and visualization.

**TaskData** – The base class responsible for handling and parsing timestamp data from student submissions.

**Attributes:**

**_student_id** — unique identifier for each student

**_task_name** — name or title of the task

**_submission_time** — timestamp of when the task was submitted

**Methods:**

**parse_timestamp()** — converts string timestamps to datetime objects

**get_delay()** — computes delay or earliness based on due date

**__repr__()** — returns a readable representation of task data

**BehaviorAnalyzer (inherits from TaskData)** – Handles classification of academic behavior based on patterns observed in submission times.

**Attributes:**

**_behavior_label** — stores the classification result (e.g., “Procrastinator”)

**Methods:**

**classify_behavior()** — determines student type using submission trends

**get_statistics()** — summarizes average submission delay and consistency

**__str__()** — displays behavior summary in a human-readable format

**Visualizer** – Uses composition by accepting processed data from the BehaviorAnalyzer class to create charts and summaries.

**Attributes:**

**_data** — reference to a list or dataframe of analyzed records

**Methods:**

**plot_timeline()** — visualizes submission trends per student

**plot_summary()** — shows weekly productivity levels

**__eq__()** — compares productivity between two students or datasets

## Class Relationship Diagram 

        ┌────────────────────┐
        │     TaskData       │
        │--------------------│
        │ - _student_id      │
        │ - _task_name       │
        │ - _submission_time │
        │--------------------│
        │ + parse_timestamp()│
        │ + get_delay()      │
        │ + __repr__()       │
        └─────────▲──────────┘
                  │
                  │ Inheritance
                  │
        ┌────────────────────────┐
        │   BehaviorAnalyzer     │
        │------------------------│
        │ - _behavior_label      │
        │------------------------│
        │ + classify_behavior()  │
        │ + get_statistics()     │
        │ + __str__()            │
        └─────────┬──────────────┘
                  │ Composition
                  ▼
        ┌────────────────────────┐
        │      Visualizer        │
        │------------------------│
        │ - _data                │
        │------------------------│
        │ + plot_timeline()      │
        │ + plot_summary()       │
        │ + __eq__()             │
        └────────────────────────┘


