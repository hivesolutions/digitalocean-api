# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

*

### Changed

*

### Fixed

*

## [0.1.4] - 2026-01-08

### Added

* Add AGENTS.md with development guidelines and contribution rules
* Add CHANGELOG.md for tracking project changes
* Add CLAUDE.md for AI assistant context

### Changed

* Update deploy workflow to use Python 3.12 instead of Python 2.7
* Update deploy workflow to use pytest as primary test runner
* Update deploy workflow to upgrade setuptools during installation
* Improve workflow conditionals using contains() for Python version checks
* Update main workflow conditionals for consistent Python version handling

### Fixed

* Fix package name from `digitalocean-api_python` to `digitalocean-api-python` in setup.py
