def minOperations(n):
    if n == 1:
        return 0  # Base case: only one H character already exists

    operations = 0
    clipboard = 1  # Initially, we have one H character in the clipboard
    file_contents = 1  # Initially, the file contains one H character

    while file_contents < n:
        if n % file_contents == 0:
            clipboard = file_contents
        file_contents += clipboard
        operations += 1

    return operations if file_contents == n else 0
