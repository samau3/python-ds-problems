def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """
    """ 
        if command not in [add, remove] or location not in [beginning, end] return none

        If command = remove
        - find out if location is beginning or end
            - if beginning return lst.pop(0). 
            - if end return lst.pop
        if command = add
            - if end lst.append(value) return lst
            - if beginning lst.insert(0, value) return lst
    """
    #global constants so should move to top
    COMMANDS = ["add", "remove"]
    LOCATIONS = ["beginning", "end"]

    def command_add(): # move the function definitions outside of the function
        if location == "end":
            lst.append(value)
        else:
            lst.insert(0, value)
        return lst


    def command_remove():
        if location == "end":
            return lst.pop()
        else:
            return lst.pop(0)

    if not (command in COMMANDS) or not (location in LOCATIONS):
        return None
    
    if command == "add":
        return command_add()
    else:
        return command_remove()