import signal
import sys
from time import sleep

from bobacon import process_manager, state_manager
from bobacon.temp_helper import clear_temp_directory
from bobacon.typing import ErrorCode


def hard_exit(error_code : ErrorCode) -> None:
	signal.signal(signal.SIGINT, signal.SIG_IGN)
	sys.exit(error_code)


def conditional_exit(error_code : ErrorCode) -> None:
	if state_manager.get_item('command') == 'headless-run':
		hard_exit(error_code)


def graceful_exit(error_code : ErrorCode) -> None:
	process_manager.stop()
	while process_manager.is_processing():
		sleep(0.5)
	if state_manager.get_item('target_path'):
		clear_temp_directory(state_manager.get_item('target_path'))
	hard_exit(error_code)
