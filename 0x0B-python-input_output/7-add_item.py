#!/usr/bin/python3
"""7-add_item module"""
import sys
"""sys module"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
"""importing the 5-save_to_json_file module"""
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""importing the 6-load_from_json_file module"""


filename = "add_item.json"
try:
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    my_list = []

n = len(sys.argv)
for i in range(1, n):
    my_list.append(sys.argv[i])

save_to_json_file(my_list, filename)
