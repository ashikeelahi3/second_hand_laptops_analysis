import time
def chunker(lst, n):
  return [lst[i:i+n] for i in range(0, len(lst), n)]

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
