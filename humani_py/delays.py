import random
import time

def random_delay(min_seconds: float = 1, max_seconds: float = 5) -> None:
    """Introduce a random delay between min_seconds and max_seconds to mimic human behavior."""
    delay = random.uniform(min_seconds, max_seconds)
    time.sleep(delay)
