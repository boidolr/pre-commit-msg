pre-commit-msg [![tag](https://img.shields.io/github/v/tag/boidolr/pre-commit-msg?sort=semver)](https://github.com/boidolr/pre-commit-msg/tags) [![Build](https://github.com/boidolr/pre-commit-msg/actions/workflows/continous-integration.yml/badge.svg)](https://github.com/boidolr/pre-commit-msg/actions/workflows/continous-integration.yml) [![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
================

A collection of prepare message and commit message git hooks for use with the [pre-commit](https://github.com/pre-commit/pre-commit) framework. For details see the list of available hooks below.

## Using pre-commit-msg with pre-commit

Add this to your `.pre-commit-config.yaml`:
```
    -   repo: https://github.com/boidolr/pre-commit-msg
        rev: v1.0.0  # Use the ref you want to point at
        hooks:
        -   id: format-message
        # -   id: ...
```
For an extended example see [`.pre-commit-config.yaml`](.pre-commit-config.yaml).

## Available hooks

- **`prepare-message`**: Change commit messages to include a prefix.
    - `--ignore-branch` will lead to the branch not being checked.
    - `--pattern` can be used to change the feature branch pattern to take the message prefix from.
        Needs to match with `--prefix-pattern`. Defaults to `feature/(\w+-\d+)`.
    - `--prefix-pattern` should match the prefix of the message to normalize it.
        Needs to match with `--pattern`. Defaults to `^\s*\w+-\d+\s*:`
- **`format-message`**: Ensure commit message conforms to format of headline followed by two empty lines.
    - `--capitalize` if the subject line should be capitalized. Other lines remain unchanged.
