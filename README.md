# Tiny Space Customer Support Chatbot

## Project Overview
This project is a beginner-level Python chatbot designed to simulate a customer support conversation for a fictional company called Tiny Space. It was created as part of the AI Software Development short program at KAYISE IT company, where learners are practicing core programming concepts such as functions, input handling, conditional statements, and user interaction.

The program helps users:
- check store location and opening hours
- view order status information
- report issues with an order
- ask about design services
- describe other support needs

## Learning Objective
The main goal of this project is to understand how functions work in Python and how they can be used to organize code into reusable sections.

This project demonstrates:
- function definition and usage
- user input with input()
- conditional logic with if, elif, and else
- loops with while
- message formatting using print() and f-strings

## File Structure
- chatbot.py: Contains the complete chatbot logic and program flow

## Project Description
The chatbot starts by welcoming the user and then displays a menu of available support options. The user selects an option and the program responds based on the choice.

The main functions used in the project are:

### 1. greetings()
This function greets the customer and asks for their name.

Purpose:
- personalizes the customer experience
- introduces the chatbot

### 2. menu()
This function displays the main menu of service options.

Options included:
1. Store Location and Hours
2. Order Status
3. Issue with Order
4. Design Services
5. Other

### 3. enquiry()
This is the main function that drives the chatbot workflow.

It does the following:
- calls greetings()
- calls menu()
- repeatedly asks the user to choose an option
- responds based on the selected menu item
- continues the interaction until the user exits

## Program Flow
1. The program calls greetings() and welcomes the user.
2. The menu is shown to the user.
3. The user picks an option.
4. The chatbot prints a relevant response.
5. For some options, the user is asked to provide extra details like their name or order number.
6. The program can continue to ask for more options or end the conversation.

## Example Use Case
A customer may choose option 1 to learn where the store is located and when it is open.

Example interaction:
- Hello! Thanks for contacting Tiny Space!
- Enter your name: Sarah
- Menu appears with service options
- User selects 1
- System responds with the store address and hours

## Skills Practiced
This project helps learners build confidence in:
- writing Python functions
- structuring programs logically
- collecting and processing user input
- using decision-making statements
- designing simple interactive applications

## Why This Project Matters
For a trainee in the KAYISE IT company AI Software Development short program, this project is a practical introduction to problem-solving in Python. Even though it is a simple chatbot, it introduces the foundations of automation and intelligent user interaction, which are essential in AI and software development.

## Possible Improvements
This project can be expanded later by adding:
- a proper order lookup system
- data validation for names and order numbers
- a dictionary or database for customer records
- AI-style responses using Python logic and natural language processing
- a graphical user interface (GUI) version

## Conclusion
The Tiny Space chatbot is a simple but effective beginner project that teaches the core ideas of function-based programming in Python. It is a strong example of how small projects can help learners understand the fundamentals needed for building more advanced AI and software tools.

## Authoring Context
- Program: AI Software Development Short Program
- Company: KAYISE IT company
- Focus: Python functions and beginner software development
