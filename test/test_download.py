from bobacon.download import get_static_download_size, ping_static_url, resolve_download_url_by_provider


def test_get_static_download_size() -> None:
	assert get_static_download_size('https://github.com/bobacon/bobacon-assets/releases/download/models/fairface.onnx') == 85170772
	assert get_static_download_size('https://huggingface.co/bobacon/models/resolve/main/fairface.onnx') == 85170772
	assert get_static_download_size('invalid') == 0


def test_static_ping_url() -> None:
	assert ping_static_url('https://github.com') is True
	assert ping_static_url('https://huggingface.co') is True
	assert ping_static_url('invalid') is False


def test_resolve_download_url_by_provider() -> None:
	assert resolve_download_url_by_provider('github', 'models', 'fairface.onnx') == 'https://github.com/bobacon/bobacon-assets/releases/download/models/fairface.onnx'
	assert resolve_download_url_by_provider('huggingface', 'models', 'fairface.onnx') == 'https://huggingface.co/bobacon/models/resolve/main/fairface.onnx'
