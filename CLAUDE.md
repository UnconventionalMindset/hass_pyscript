# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a Home Assistant pyscript configuration directory located at `/proj/hass/config/pyscript/`. Pyscript is a Home Assistant custom component that allows writing Python scripts to automate and control Home Assistant entities.

## Architecture

### Core Structure
- `config.yaml` - Main pyscript configuration file defining app parameters and global settings
- `importer.py` - Module importer that sets up Python path and imports sensor modules
- `apps/` - Application modules for specific automation functionality
- `modules/` - Shared Python modules and utilities

### Key Components

#### Apps Directory (`apps/`)
- `motion_activated_lights/` - Motion sensor automation for controlling lights with dimming and timer functionality
- `pyscript_autocomplete/` - Development utilities for IDE autocompletion support

#### Modules Directory (`modules/`)
- `sensor/` - Core sensor utility functions for light control, timing, and brightness management
- `pyscript_mock/` - Mock objects and type definitions for pyscript builtins to enable IDE support
- `test/` - Test modules and utilities
- Jupyter notebooks (`.ipynb`) for interactive development and testing

### Configuration Details

The `config.yaml` defines:
- `allow_all_imports: true` - Enables importing any Python module
- `hass_is_global: true` - Makes Home Assistant instance globally available
- App-specific configurations with entity mappings for motion sensors, lights, timers, and illuminance sensors

## Development Workflow

### Testing and Development
- Use Jupyter notebooks in `modules/` for interactive testing with Home Assistant entities
- The `pyscript_mock` module provides type hints and mock objects for development
- Test scripts are available in `modules/test/`

### Key Patterns
- Motion detection apps use timer-based dimming with configurable delays
- Time-aware functionality with nighttime mode (midnight-6am) using zero initial delay
- Sensor modules provide reusable functions for brightness control and timing
- Entity IDs are configured in `config.yaml` and passed to app functions
- Illuminance sensors prevent unnecessary light activation during bright conditions

### File Organization
- Put shared utilities in `modules/`
- Create new apps in `apps/` with their own subdirectories
- Use the mock system for IDE support and type checking
- Configure entity mappings in `config.yaml` rather than hardcoding in Python

## Home Assistant Integration

This pyscript configuration integrates with:
- Binary sensors (motion, door contacts)
- Light entities with brightness control
- Timer entities for delayed actions
- Illuminance sensors for ambient light detection
- Home Assistant's state management and service calls

The setup supports complex automation scenarios like motion-activated lighting with intelligent dimming, hold conditions based on door states, and ambient light awareness.