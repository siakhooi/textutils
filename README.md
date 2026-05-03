# textutils

Package `siakhooi-textutils` to transform or evaluate text.

## Commands

| Command             | Description                          | Doc                       |
| ------------------- | ------------------------------------ | ------------------------- |
| `prefix` prefixText | prepend each line with `prefixText`  | [📗Doc](docs/prefix.md)   |
| `suffix` suffixText | append each line with `suffixText`   | [📗Doc](docs/suffix.md)   |
| `is-true` value     | Evaluate `value` if is a true value  | [📗Doc](docs/is-true.md)  |
| `is-false` value    | Evaluate `value` if is a false value | [📗Doc](docs/is-false.md) |
| `make-table` columns| Print CSV data from stdin into table using `columns` as headers||

## Quick Start

### Ubuntu/Debian

```bash
$ sudo curl -L https://siakhooi.github.io/apt/siakhooi-apt.list | sudo tee /etc/apt/sources.list.d/siakhooi-apt.list > /dev/null
$ sudo curl -L https://siakhooi.github.io/apt/siakhooi-apt.gpg  | sudo tee /usr/share/keyrings/siakhooi-apt.gpg > /dev/null
$ sudo apt update

$ sudo apt install siakhooi-textutils
```
### Fedora/Red Hat

```bash
$ sudo curl -L https://siakhooi.github.io/rpms/siakhooi-rpms.repo | sudo tee /etc/yum.repos.d/siakhooi-rpms.repo > /dev/null

$ sudo dnf install siakhooi-textutils
# or
$ sudo yum install siakhooi-textutils
```

## Deployments

- <https://siakhooi.github.io/apt/>

## Badges

![GitHub](https://img.shields.io/github/license/siakhooi/textutils?logo=github)
![GitHub last commit](https://img.shields.io/github/last-commit/siakhooi/textutils?logo=github)
![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/siakhooi/textutils?logo=github)
![GitHub issues](https://img.shields.io/github/issues/siakhooi/textutils?logo=github)
![GitHub closed issues](https://img.shields.io/github/issues-closed/siakhooi/textutils?logo=github)
![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/siakhooi/textutils?logo=github)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed-raw/siakhooi/textutils?logo=github)
![GitHub top language](https://img.shields.io/github/languages/top/siakhooi/textutils?logo=github)
![GitHub language count](https://img.shields.io/github/languages/count/siakhooi/textutils?logo=github)
![GitHub repo size](https://img.shields.io/github/repo-size/siakhooi/textutils?logo=github)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/siakhooi/textutils?logo=github)
![Workflow](https://img.shields.io/badge/Workflow-github-purple)
![workflow](https://github.com/siakhooi/textutils/actions/workflows/workflow-build-with-quality-checks.yml/badge.svg)
![workflow](https://github.com/siakhooi/textutils/actions/workflows/workflow-deployments.yml/badge.svg)
![Release](https://img.shields.io/badge/Release-github-purple)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/siakhooi/textutils?label=GPR%20release&logo=github)
![GitHub all releases](https://img.shields.io/github/downloads/siakhooi/textutils/total?color=33cb56&logo=github)
![GitHub Release Date](https://img.shields.io/github/release-date/siakhooi/textutils?logo=github)

[![Wise](https://img.shields.io/badge/Funding-Wise-33cb56.svg?logo=wise)](https://wise.com/pay/me/siakn3)
![visitors](https://hit-tztugwlsja-uc.a.run.app/?outputtype=badge&counter=ghmd-textutils)
