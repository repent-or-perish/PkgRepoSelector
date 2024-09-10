# PkgRepoSelector

PkgRepoSelector is a simple graphical and command-line application to manage and select package repositories for GhostBSD. It provides a user-friendly interface for switching between different repository mirrors, making it easy to update and configure the system's package sources.

## Features

- **Graphical Interface**: Easy-to-use GTK-based GUI for selecting package repositories.
- **Command-line Interface**: Allows repository management directly from the CLI.
- **Validation**: Ensures the configuration file is valid after updating the repository.
- **Logging**: Logs actions and errors for troubleshooting.

## Requirements

- Python 3.11
- GTK 3.0
- GhostBSD

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/repent-or-perish/PkgRepoSelector.git
   cd PkgRepoSelector
   ```

2. Ensure you have the required dependencies installed:
   ```
   sudo pkg install gtk3
   ```

3. Make the scripts executable:
   ```
   chmod +x PkgRepoSelector repo_manager.py config.py ui.py
   ```

## Usage

### Graphical Interface

1. Run the application:
   ```
   sudo ./PkgRepoSelector
   ```

2. Select the desired repository from the list.
3. Confirm the selection when prompted.
4. The application will update the repository URLs and validate the new configuration.

### Command-line Interface

1. List available repositories:
   ```
   sudo ./PkgRepoSelector --list
   ```

2. Show the current repository:
   ```
   sudo ./PkgRepoSelector --current
   ```

3. Select a repository:
   ```
   sudo ./PkgRepoSelector <repo_name>
   ```
   Replace `<repo_name>` with the name of the repository you want to select, such as `GhostBSD_FR`.

## Configuration

The configuration file is located at `/etc/pkg/GhostBSD.conf`.

## Logging

Logs are written to `~/pkg_repo_selector.log`. Check this file for any errors or information about the application's operations.

