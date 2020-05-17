import threading
import time
import ack


class Timer352:
    SLEEP_INTERVAL = 0.1
    def __init__(self, socket, seq, timeout=100):
        self._socket = socket
        self.sequence_no = seq
        self._timeout = timeout
        self._current_time = 0.0
        self._is_thread_alive = True

    def start_timer(self):
        self._is_thread_alive = True
        self._thread = threading.Thread(target=self._run)
        self._thread.start()

    def _run(self):
        while self._current_time < self._timeout and self._is_thread_alive:
            time.sleep(Timer352.SLEEP_INTERVAL)
            self._current_time += Timer352.SLEEP_INTERVAL

        if self._is_thread_alive:
            self._socket._resend(self.sequence_no)

    def stop_timer(self):
        self._is_thread_alive = False
    

    def reset_timer(self):
        self._current_time = 0.0
        self._is_thread_alive = True
    