def best_fit(blocks, request_size, start_index):
    """
    Allocates memory using a modified best-fit approach.
    
    :param blocks: List of tuples representing memory blocks (start_address, size)
    :param request_size: Integer representing the requested memory size
    :param start_index: Integer index to begin searching
    :return: Updated memory list, assigned start address, allocated block size, and next search index
    """
    
    # Edge case: Empty memory list or invalid request
    if not blocks or request_size <= 0:
        return None

    num_blocks = len(blocks)
    chosen_index = -1
    allocated_address = -1
    smallest_fit = float('inf')  # Track the smallest available block that fits

    # Iterate through memory blocks in a circular fashion
    for shift in range(num_blocks):
        check_index = (start_index + shift) % num_blocks
        address, size = blocks[check_index]

        # Identify the smallest block that can accommodate the request
        if size >= request_size and size < smallest_fit:
            chosen_index = check_index
            allocated_address = address
            smallest_fit = size

    # If no suitable block was found, return failure
    if chosen_index == -1:
        return None

    updated_blocks = blocks[:]

    # If the block is exactly the requested size, remove it from available memory
    if smallest_fit == request_size:
        updated_blocks.pop(chosen_index)
        next_search_index = 0 if chosen_index == len(blocks) - 1 else chosen_index
    else:
        # Otherwise, shrink the block and adjust its starting address
        new_address = allocated_address + request_size
        remaining_size = smallest_fit - request_size
        updated_blocks[chosen_index] = (new_address, remaining_size)
        next_search_index = chosen_index

    return updated_blocks, allocated_address, smallest_fit, next_search_index
