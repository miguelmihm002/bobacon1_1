from typing import Optional
import gradio

import bobacon1_1.globals
import bobacon1_1.choices
from bobacon1_1.typing import VideoMemoryStrategy
from bobacon1_1 import wording

VIDEO_MEMORY_STRATEGY_DROPDOWN : Optional[gradio.Dropdown] = None
SYSTEM_MEMORY_LIMIT_SLIDER : Optional[gradio.Slider] = None


def render() -> None:
	global VIDEO_MEMORY_STRATEGY_DROPDOWN
	global SYSTEM_MEMORY_LIMIT_SLIDER

	VIDEO_MEMORY_STRATEGY_DROPDOWN = gradio.Dropdown(
		label = wording.get('uis.video_memory_strategy_dropdown'),
		choices = bobacon1_1.choices.video_memory_strategies,
		value = bobacon1_1.globals.video_memory_strategy
	)
	SYSTEM_MEMORY_LIMIT_SLIDER = gradio.Slider(
		label = wording.get('uis.system_memory_limit_slider'),
		step =bobacon1_1.choices.system_memory_limit_range[1] - bobacon1_1.choices.system_memory_limit_range[0],
		minimum = bobacon1_1.choices.system_memory_limit_range[0],
		maximum = bobacon1_1.choices.system_memory_limit_range[-1],
		value = bobacon1_1.globals.system_memory_limit
	)


def listen() -> None:
	VIDEO_MEMORY_STRATEGY_DROPDOWN.change(update_video_memory_strategy, inputs = VIDEO_MEMORY_STRATEGY_DROPDOWN)
	SYSTEM_MEMORY_LIMIT_SLIDER.release(update_system_memory_limit, inputs = SYSTEM_MEMORY_LIMIT_SLIDER)


def update_video_memory_strategy(video_memory_strategy : VideoMemoryStrategy) -> None:
	bobacon1_1.globals.video_memory_strategy = video_memory_strategy


def update_system_memory_limit(system_memory_limit : int) -> None:
	bobacon1_1.globals.system_memory_limit = system_memory_limit
