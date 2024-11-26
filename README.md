# Tasks solutions for Concepts of Programming's class
by: Mohamed Ehab Ahmed Mohamed
**Problem 1: Daily Steps Tracker**

<b>Description:</b>
 You have a list of the number of steps taken each day in a month. Your task is to write a
 program that performs the following:
 1. Accepts the number of steps taken each day in the month as numbers separated by
 spaces.
 2. Calculates the highest and lowest step counts.
 3. Calculates the average daily step count.
 4. Sorts the step counts in descending order

<b>Solution</b>:
1. Input step data in form of string then convert it into list using split() function</ul>
2. Determine highest and lowest step counts by:
    - using ___sorted()__ function to sort the list and take the first element as the least step count and the last element as the highest count
    - using ___max()___ and ___min()___ functions
3. Take average count by dividing summation result of list elements by size of the list and rounding up the division result to 3 decimal places
4. Sort the list descendingly by ___Sorted()___ function or by ___manual looping___ over elements

   --------------------------------------------------------------------------------------------------------------------------
 **Problem 2: Library Book Borrowing Analysis**

<b>Description:</b>
 You have a record of books borrowed from a library for a month. Each record includes the book
 title and the number of days it was borrowed. Your task is to write a program that performs the
 following:
 1. Accepts a list of borrowed books with the format: "Book Title- Days Borrowed".
 2. Calculates the most and least borrowed book based on the number of days.
 3. Calculates the average number of days books were borrowed.
 4. Finds the unique titles of all borrowed books.
 5. Sorts the books by the number of days borrowed in descending order.

<b>Requirements:</b>

 ● Use a dictionary to store book titles as keys and their total borrowed days as values.
 
 ● Use a set to find unique titles of books borrowed.
 
 ● Calculate the most and least borrowed book, the average borrowing time, and sort books
 by borrowing duration.

<b>Solution:</b>
1. Input books in a certain format and then split them as items in list
2. Loop over list to split each book into title and borrowed days and store them in a dictionary ___book_data___ with certain conditions
3. Store borrowed days as ___book_data values___ in list and calculate average borrowed days by taking summation of the values of list over its size
4. Store ___book_data keys___ in a set to print unique titles
6. Loop over ___sorted()___ function with its parameter ___key___ being the <u>values of the dictionary</u> to sort the dictionary by <u>number of borrowed days</u> and ___reverse___ the sorting to obtain a descending order for the dictionary

   --------------------------------------------------------------------------------------------------------------------------
 **Problem 3: Word Scramble Game**
 
__Description:__
 Create a word scramble game where the program randomly scrambles a word and gives the
 player a set number of attempts to guess the original word.
 
 __Requirements:__
 1. The program should start by selecting a random word from a predefined list of words.
 2. The selected word should be scrambled (characters shuffled in a random order).
 3. Display the scrambled word to the player and ask them to guess the original word.
 4. The player should have 5 attempts to guess the word correctly.
 5. For each incorrect guess, the player should be informed how many attempts they have
 left.
 6. If the player guesses correctly within the attempts, display a congratulatory message.
 7. If the player runs out of attempts, reveal the original word.
 8. Handle invalid input gracefully (e.g., empty input).

__Solution:__
1. Import random library to use ___randint()__ and ___shuffle()___
2. Initialize a list with some words
3. pick a random word from list by randomizing the index by which we access the list of word using ___randint()___
4. Cast the random word into list and using ___shuffle()__ on it to shuffle its letters then joining the list items into a string after shuffling using ___join()___
5. Initialize a for loop to loop over attempts with 3 conditions:
   - in case of guessing right, break the loop and display congrats message
   - in case of guessing wrong and there are attempts left, display message and continue
   - in case of guessing wrong and there are no attempts left, display a message and show correct answer
6. Display custom error message if input is:
   - empty
   - contains characters that are not alphabetical
   - contains numbers
--------------------------------------------------------------------------------------------------------------------------

link to solutions explanation videos: [Click Here](https://drive.google.com/drive/folders/1UnczXuOADRuBy7P5ovW0hKnQ2nzqXKpa?usp=sharing)
