import subprocess

import pytest


def _execute_command(*args: str, returncode: int | None = None) -> str | None:
    result = subprocess.run(args, check=False, encoding="utf-8", stderr=subprocess.DEVNULL, stdout=subprocess.PIPE)  # noqa: S603
    if (returncode is None and result.returncode != 0) or (returncode is not None and result.returncode != returncode):
        return None
    return result.stdout.strip()


@pytest.fixture
def temp_git_dir(tmpdir):
    git_dir = tmpdir.join("gits")
    git_dir.mkdir()
    _execute_command("git", "init", "--initial-branch=main", "--", str(git_dir))
    return git_dir


@pytest.fixture
def temp_merge_conflict(temp_git_dir):
    with temp_git_dir.as_cwd():
        path = temp_git_dir.join("file")
        path.write("")
        _execute_command("git", "config", "user.name", "tester")
        _execute_command("git", "config", "user.email", "tester@local")
        _execute_command("git", "add", "file")
        _execute_command("git", "commit", "-am", "inital")
        path.write("first")
        _execute_command("git", "commit", "-am", "first")
        _execute_command("git", "checkout", "-b", "develop", "HEAD~1")
        path.write("second")
        _execute_command("git", "commit", "-am", "second")

        _execute_command("git", "merge", "main")
        assert "<<<<<<< HEAD" in path.read()
    return temp_git_dir


@pytest.fixture
def temp_rebase_conflict(temp_git_dir):
    with temp_git_dir.as_cwd():
        path = temp_git_dir.join("file")
        path.write("")
        _execute_command("git", "config", "user.name", "tester")
        _execute_command("git", "config", "user.email", "tester@local")
        _execute_command("git", "add", "file")
        _execute_command("git", "commit", "-am", "inital")
        path.write("first")
        _execute_command("git", "commit", "-am", "first")
        _execute_command("git", "checkout", "-b", "develop", "HEAD~1")
        path.write("second")
        _execute_command("git", "commit", "-am", "second")

        _execute_command("git", "rebase", "main")
        assert "<<<<<<< HEAD" in path.read()

    return temp_git_dir
