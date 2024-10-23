from typing import Optional
import gradio

import bobacon1_1.globals
import bobacon1_1.choices
from bobacon1_1 import wording

EXECUTION_QUEUE_COUNT_SLIDER : Optional[gradio.Slider] = None


def render() -> None:
	global EXECUTION_QUEUE_COUNT_SLIDER

	EXECUTION_QUEUE_COUNT_SLIDER = gradio.Slider(
		label = wording.get('uis.execution_queue_count_slider'),
		value = bobacon1_1.globals.execution_queue_count,
		step = bobacon1_1.choices.execution_queue_count_range[1] - bobacon1_1.choices.execution_queue_count_range[0],
		minimum = bobacon1_1.choices.execution_queue_count_range[0],
		maximum = bobacon1_1.choices.execution_queue_count_range[-1]
	)


def listen() -> None:
	EXECUTION_QUEUE_COUNT_SLIDER.release(update_execution_queue_count, inputs = EXECUTION_QUEUE_COUNT_SLIDER)


def update_execution_queue_count(execution_queue_count : int = 1) -> None:
	bobacon1_1.globals.execution_queue_count = execution_queue_count
