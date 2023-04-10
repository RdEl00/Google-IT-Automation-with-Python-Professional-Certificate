# Getting Your Python On

In this module, you’ll learn about the different types of operating systems, and how you can get your python code ready to interact with the operating system. We’ll learn about getting your environment set up and installing additional Python modules that will help you along the way. We’ll rundown interpreted versus compiled language, and how they differ from each other. We’ll dive into the benefits of automation, and point out common pitfalls so you can avoid them. Finally, we’ll learn about Qwiklabs, which will be used for graded assessments.

## Learning Objectives

- Identify the components and functions of an operating system
- Describe the difference between interpreted and compiled programming languages
- Explain what an IDE (integrated development environment) is
- Install and run Python on a local machine
- List the benefits and pitfalls of automation

## Assessments

- [Practice Quiz - Getting Ready for Python](#Practice-Quiz---Getting-Ready-for-Python)
- [Practice Quiz - Running Python Locally](#Practice-Quiz---Running-Python-Locally)
- [Practice Quiz - Automation](#Practice-Quiz---Automation)

### Practice Quiz - Getting Ready for Python

1. Which of the following is the most modern, up-to-date version of Python?

> Python 3

2. Which of the following operating systems is compatible with Python 3?

> All of the above

3. Which of the following operating systems does not run on a Linux kernel?

> Mac OS

4. If we want to check to see  what version of Python is installed, what would we type into the command line? Select all that apply.

> python -V

> python --version

5. What is pip an example of?

> A Python package manager

[ :arrow_up: Back to top](#Getting-Your-Python-On)

### Practice Quiz - Running Python Locally

1. When your IDE automatically creates an indent for you, this is known as what?

> Code completion

2. Can you identify the error in the following code?

```python
#!/usr/bin/env python3
import numpy as np

def numpyArray():
    x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
    y = numpy.array([[3, 6, 2], [9, 12, 8]], np.int32)
    return x*y
print(numpyArray())

```

> The y variable is not calling the numpy module properly.

3. Which type of programming language is read and converted to machine code before runtime, allowing for more efficient code?

> Compiled language

4. Which of the following is not an IDE or code editor?

> pip

5. What does the PATH variable do?

> Tells the operating system where to find executables

[ :arrow_up: Back to top](#Getting-Your-Python-On)

### Practice Quiz - Automation

1. At a manufacturing plant, an employee spends several minutes each hour noting uptime and downtime for each of the machines they are running. Which of the following ideas would best automate this process?

> Add an analog Internet of Things (IoT) module to each machine, in order to detect their power states, and write a script that records uptime and downtime, reporting hourly

2. One important aspect of automation is forensic value. Which of the following statements describes this term correctly?

> It is important for automated processes to leave extensive logs so when errors occur, they can be properly investigated.

3. An employee at a technical support company is required to collate reports into a single file and send that file via email three times a day, five days a week for one month, on top of his other duties. It takes him about 15 minutes each time. He has discovered a way to automate the process, but it will take him at least 10 hours to code the automation script. Which of the following equations will help them decide whether it's worth automating the process?

> if [10 hours to automate < (15 minutes * 60 times per month)] then automate

4. A company is looking at automating one of their internal processes and wants to determine if automating a process would save labor time this year. The company uses the formula [time_to_automate < (time_to_perform * amount_of_times_done)] to decide whether automation is worthwhile. The process normally takes about 10 minutes every week. The automation process itself will take 40 hours total to complete. Using the formula, how many weeks will it be before the company starts saving time on the process?

> 240 weeks

5. Which of the following are valid methods to prevent silent automation errors? (Check all that apply)

> Email notifications about errors

> Internal issue tracker entries

> Regular consistency checks

[ :arrow_up: Back to top](#Getting-Your-Python-On)




