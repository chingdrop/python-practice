# To Do List

## Infrastructure

## Code

- [ ] Prepare to use click
  - [ ] Create pyproject.toml and setup.py
  - [ ] Abstract functions inside the large holding modules
  - [ ] Create the click command functions

## Completed

- [x] Combine similar code together into directories
  - [x] Move dependency code into its own directory
  - [x] Combine similar code together into their own modules
  - [x] Combine similar code into the larger holding modules, calc, convert, graph and text
  - [x] Remove redundant directories
- [x] Refactor the final versions of the book code
  - [x] Use black formatting
  - [x] Snake case all functions, variables and parameters
  - [x] Add context managers where needed
  - [x] Change print statements to use f strings
- [x] Get the most up to date version of each function used in the book
- [x] Find the original source code used in the programming concepts book

## Rejected

- Originally, I was going to separate each practice course into their own directory.
  - Now, I want all practice functions to be available as commands in Click
