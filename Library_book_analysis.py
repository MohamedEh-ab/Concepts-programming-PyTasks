# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 14:31:29 2024

@author: Moham
"""
#1
records_input = input("Enter books in format: \"Book Title - Days Borrowed\" and seperate them by \",\":\n\t>>> ")
records = records_input.split(", ")
book_data = dict()
for record in records:
    title, days = record.split('-')
    title = title.strip()
    days = int(days)
    if title in book_data:
        book_data[title] += days
    else:
        book_data[title] = days

#2
for key, value in book_data.items():
    if value == max(book_data.values()):
        grossing_title = key
    if value == min(book_data.values()):
        least_title = key

#3
days_list = list(book_data.values())
avg_days = round(sum(days_list) / len(days_list))

#4
unique_titles = set(book_data.keys())

#5
sorted_dict = {}
for i in sorted(book_data, key=book_data.get, reverse=True):
    sorted_dict[i] = book_data[i]

# Results
print('------------------------------------')
print(f"Most borrowed book is {grossing_title}\nLeast borrowed book is {least_title}")
print(f"Average number of days books were borrowed: {avg_days}")
print(f"Unique Titles: {unique_titles}")
print(f"Library Books after being sorted in Desc. order: {list(sorted_dict.keys())}")
