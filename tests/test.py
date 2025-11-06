import time

# max = 4
# timeout_int = 2
# a = time.time()
# i = 0
# for j in range(100):
#     print(f'{j} hello!')
#     i+=1
#     b = time.time()
#     if i == max:
#         if (a-b) < timeout_int: time.sleep(timeout_int-(a-b))
#         a = time.time()
#         i = 0

# import time

def throttled_list_iterator(items, max_per_interval, interval_seconds):
    """
    Creates a generator that yields items from a list with a rate limit.
    It ensures that no more than `max_per_interval` items are yielded within any `interval_seconds` period.

    Args:
        items: The list of items to iterate over.
        max_per_interval: The maximum number of items to yield per interval.
        interval_seconds: The duration of the time interval in seconds.
    """
    if not isinstance(items, list):
        raise TypeError("'items' must be a list.")
    if max_per_interval <= 0:
        raise ValueError("max_per_interval must be a positive integer.")
    if interval_seconds <= 0:
        raise ValueError("interval_seconds must be a positive number.")

    interval_start_time = time.time()
    iteration_in_interval = 0

    for item in items:
        yield item

        iteration_in_interval += 1
        if iteration_in_interval >= max_per_interval:
            current_time = time.time()
            elapsed_time = current_time - interval_start_time

            if elapsed_time < interval_seconds:
                sleep_duration = interval_seconds - elapsed_time
                time.sleep(sleep_duration)

            # Reset for the next interval
            interval_start_time = time.time()
            iteration_in_interval = 0

# Example of how to use the generator with a list:
# my_list = [f'item_{i}' for i in range(100)]
# for item in throttled_list_iterator(items=my_list, max_per_interval=4, interval_seconds=2):
#     print(f'Processing {item}')


for j in throttled_list_iterator(list(range(100)), 15, 5):
    print(j)
