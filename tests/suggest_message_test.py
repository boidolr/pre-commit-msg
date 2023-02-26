from unittest import mock

import pytest

from pre_commit_msg.suggest_message import main


@pytest.fixture()
def mock_urlopen(request):
    with mock.patch("urllib.request.urlopen") as response_mock:
        response_mock.read.return_value = request.param.encode("utf-8")
        response_mock.__enter__.return_value = response_mock
        response_mock.return_value = response_mock
        yield response_mock


@pytest.mark.parametrize("mock_urlopen", ["empty"], indirect=True)
def test_abort_on_failed_request(tmp_path, mock_urlopen):
    content = "# existing message content"
    path = tmp_path / "message"
    path.write_text(content)
    mock_urlopen.return_value.read.side_effect = Exception("Test")

    assert main((str(path),)) == 1
    assert path.read_text() == content


@pytest.mark.parametrize("mock_urlopen", ["some message"], indirect=True)
def test_prepend_suggestion(tmp_path, mock_urlopen):
    content = "# existing message content"
    path = tmp_path / "message"
    path.write_text(content)

    assert main((str(path),)) == 0
    assert path.read_text() == f"# some message\n{content}"
