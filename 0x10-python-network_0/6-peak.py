#!/usr/bin/python3
"""Find a peak in a list of unsorted integers."""

def find_peak(list_of_integers):
    """
    Find Biggest Number That Before and After Below This
    or Equals
    """
    
    current_max_peak = None
    for i in range (0,len(list_of_integers) - 1):
        if list_of_integers[i] >= list_of_integers[i+1]:
            if i == 0 or  list_of_integers[i] >= list_of_integers[i-1]:
                if not current_max_peak:
                    current_max_peak = list_of_integers[i]
                else:
                    current_max_peak = max(current_max_peak,list_of_integers[i])
    return current_max_peak

