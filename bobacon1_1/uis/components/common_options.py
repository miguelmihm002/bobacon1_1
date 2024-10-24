from typing import Optional, List
import gradio

import bobacon1_1.globals
from bobacon1_1 import wording
from bobacon1_1.uis import choices as uis_choices

COMMON_OPTIONS_CHECKBOX_GROUP : Optional[gradio.Checkboxgroup] = None


def render() -> None:
	global COMMON_OPTIONS_CHECKBOX_GROUP

	value = []
	if bobacon1_1.globals.keep_temp:
		value.append('keep-temp')
	if bobacon1_1.globals.skip_audio:
		value.append('skip-audio')
	if bobacon1_1.globals.skip_download:
		value.append('skip-download')
	COMMON_OPTIONS_CHECKBOX_GROUP = gradio.Checkboxgroup(
		label = wording.get('uis.common_options_checkbox_group'),
		choices = uis_choices.common_options,
		value = value
	)


def listen() -> None:
	COMMON_OPTIONS_CHECKBOX_GROUP.change(update, inputs = COMMON_OPTIONS_CHECKBOX_GROUP)


def update(common_options : List[str]) -> None:
	bobacon1_1.globals.keep_temp = 'keep-temp' in common_options
	bobacon1_1.globals.skip_audio = 'skip-audio' in common_options
	bobacon1_1.globals.skip_download = 'skip-download' in common_options
