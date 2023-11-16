# CS567 - Software Testing
As part of the CS567 course, I undertook a project that involved the application of mutation testing technique to evaluate simple Python code. Leveraging the testing tools TSTL, universalmutator and MutPy. This project only deepened my understanding of software testing methodologies.

## Author
- [Tung L. Nguyen] - Hello, my name is Tung Nguyen, and I am currently a Ph.D. student at NAU, where I am immersed in the dynamic world of artificial intelligence. My primary focus within this expansive field lies in the realm of natural language processing, specifically with a keen interest in large language models (LLM).

## Instructor
- [Alex Groce] - Associate professor of computer science, software testing researcher; "Thought is a labyrinth."

## Table of Contents
- [Repository Structure](#repository-structure)
- [How to Use](#how-to-use)

## Repository Structure
This repository is organized into two main folders:
1. **scr_code:**
    - Includes Python code and source files for testing.

2. **reports:**
    - Tracks my progress through reports.
    - Documents my experiments and learning.

## How to Use
1. **tstl and universalmutator**
Source files are inside the folder [src_code/tstl](./src_code/tstl)
- install tstl and universalmutator: ``` pip install tstl universalmutator ```
- in command line environment:
  - run ``` mkdir mutants ``` to create the directory named 'mutants' to store all of the mutant files.
  - run ```tstl test_myCode.tstl``` to generate harness core for testing.
  - run ```mutate myCode.py --mutantDir mutants``` to generates mutants for myCode.py and stores them inside directory 'mutants'
  - run ```analyze_mutants myCode.py "tstl_rt --timeout 120" --mutantDir mutants --verbose``` analyze all mutants from myCode.py

2. **mutpy**
Source files are inside the folder [src_code/tstl](./src_code/mutpy)
- install mutpy: ```pip install mutpy```
- in command line environment:
  - run ```mkdir -p report``` to create a directory to store all of the .html reports.
  - run ```mut.py --target myCode --unit-test test_myCode --show-mutants --report-html report --timeout-factor 30 --experimental-operators --colored-output``` to analyze all the mutants from myCode.py by using testing file test_myCode.py
  - all of the reports are stored in 'report' directory.
