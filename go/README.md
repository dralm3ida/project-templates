# Go:
Go project using go 1.23. Change the project naming at your convenience.

#### Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation

Download source code and run the following commands to init the module:
```console
go mod init [module_name]
go mod tidy
go list -f '{{.Target}}' # Discover the install path
go install # Add install path executable in path before installing
```

## Usage

Run in console:
```console
go build -o [executable_name]
go run .
```