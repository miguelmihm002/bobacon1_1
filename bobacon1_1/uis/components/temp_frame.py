from typing import Optional
import gradio

import bobacon1_1.globals
import bobacon1_1.choices
from bobacon1_1 import wording
from bobacon1_1.typing import TempFrameFormat
from bobacon1_1.filesystem import is_video
from bobacon1_1.uis.core import get_ui_component

TEMP_FRAME_FORMAT_DROPDOWN : Optional[gradio.Dropdown] = None


def render() -> None:
	global TEMP_FRAME_FORMAT_DROPDOWN

	TEMP_FRAME_FORMAT_DROPDOWN = gradio.Dropdown(
		label = wording.get('uis.temp_frame_format_dropdown'),
		choices = bobacon1_1.choices.temp_frame_formats,
		value = bobacon1_1.globals.temp_frame_format,
		visible = is_video(bobacon1_1.globals.target_path)
	)


def listen() -> None:
	TEMP_FRAME_FORMAT_DROPDOWN.change(update_temp_frame_format, inputs = TEMP_FRAME_FORMAT_DROPDOWN)
	target_video = get_ui_component('target_video')
	if target_video:
		for method in [ 'upload', 'change', 'clear' ]:
			getattr(target_video, method)(remote_update, outputs = TEMP_FRAME_FORMAT_DROPDOWN)


def remote_update() -> gradio.Dropdown:
	if is_video(bobacon1_1.globals.target_path):
		return gradio.Dropdown(visible = True)
	return gradio.Dropdown(visible = False)


def update_temp_frame_format(temp_frame_format : TempFrameFormat) -> None:
	bobacon1_1.globals.temp_frame_format = temp_frame_format

