def all(numbers, target):
    if not numbers:
        return False
    
    for number in numbers:
        # If any number does not match the target, return False
        if number != target:
            return False
    
    # If we reached this point, it means all numbers match the target
    return True