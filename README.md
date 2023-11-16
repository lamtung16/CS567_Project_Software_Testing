# CS567 - Software Testing
As part of the CS567 course, I undertook a project that involved the application of mutation testing technique to evaluate simple Python code. Leveraging the testing tools TSTL, universalmutator and MutPy, I aimed to enhance the reliability and robustness of the software. This project only deepened my understanding of software testing methodologies.

## Author
- [Tung L. Nguyen] - Hello, my name is Tung Nguyen, and I am currently a Ph.D. student at NAU, where I am immersed in the dynamic world of artificial intelligence. My primary focus within this expansive field lies in the realm of natural language processing, specifically with a keen interest in large language models (LLM).

## Instructor
- [Alex Groce] - Associate professor of computer science, software testing researcher; "Thought is a labyrinth."

## Table of Contents
- [Repository Structure](#repository-structure)
- [How to Use](#how-to-use)
- [Tools](#tools)
  - [TSTL](#tstl)
  - [MutPy](#mutpy)

## Repository Structure
This repository is organized into two main folders:
1. **scr_code:**
    - Includes Python code and source files for testing.

2. **reports:**
    - Tracks my progress through reports.
    - Documents my experiments and learning.

## How to Use
1. **tstl and universalmutator**
Inside the folder [scr_code/tstl](./scr_code/tstl)
- install tstl and universalmutator: ``` pip install tstl universalmutator ```
- in command line, run
- !mkdir mutants
- run tstl test_myCode.tstl
- run mutate myCode.py --mutantDir mutants
- run analyze_mutants myCode.py "tstl_rt --timeout 120" --mutantDir mutants --verbose

2. **mutpy**


### Prerequisites

List any prerequisites or dependencies that users need to install before using your project.

```bash
# Example:
pip install -r requirements.txt
```
