# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- Packaging with `pyproject.toml` and Flit.
- `InferenceRunner` high-level API.
- Sphinx documentation skeleton.
- GitHub Actions for tests and docs.

### Changed
- Modules moved to `src/placer` with absolute imports.

### Removed
- Legacy `examples` directory replaced with simplified `example` data.

### Fixed
- Device handling generalized beyond CUDA.
