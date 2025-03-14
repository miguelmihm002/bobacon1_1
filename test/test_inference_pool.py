from unittest.mock import patch

import pytest
from onnxruntime import InferenceSession

from bobacon import content_analyser, state_manager
from bobacon.inference_manager import INFERENCE_POOLS, get_inference_pool


@pytest.fixture(scope = 'module', autouse = True)
def before_all() -> None:
	state_manager.init_item('execution_device_id', 0)
	state_manager.init_item('execution_providers', [ 'cpu' ])
	state_manager.init_item('download_providers', [ 'github' ])
	content_analyser.pre_check()


def test_get_inference_pool() -> None:
	model_sources = content_analyser.get_model_options().get('sources')

	with patch('bobacon.inference_manager.detect_app_context', return_value = 'cli'):
		get_inference_pool('test', model_sources)

		assert isinstance(INFERENCE_POOLS.get('cli').get('test.cpu').get('content_analyser'), InferenceSession)

	with patch('bobacon.inference_manager.detect_app_context', return_value = 'ui'):
		get_inference_pool('test', model_sources)

		assert isinstance(INFERENCE_POOLS.get('ui').get('test.cpu').get('content_analyser'), InferenceSession)

	assert INFERENCE_POOLS.get('cli').get('test.cpu').get('content_analyser') == INFERENCE_POOLS.get('ui').get('test.cpu').get('content_analyser')
