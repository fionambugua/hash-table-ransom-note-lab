def can_construct(ransomNote: str, magazine: str) -> bool:
    """
    Determines if ransomNote can be constructed using letters from magazine.
    Each letter in magazine can only be used once.

    Parameters:
        ransomNote (str): The target string to construct.
        magazine (str): The source string with available characters.

    Returns:
        bool: True if ransomNote can be constructed, False otherwise.
    """
    cleanMagazine = "".join(char for char in magazine if char.isalnum())
    cleanRansomeNote = "".join(char for char in ransomNote if char.isalnum())

    letterLog = {}

    for k in cleanMagazine:
        letterLog[k] = letterLog.get(k, 0) + 1

    print(letterLog)

    for k in cleanRansomeNote:
        val = letterLog.get(k, 0)
        if val == 0:
            return False
        else:
            letterLog[k] -= 1

    return True