# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in InquirerPrompt, please report it
responsibly:

1. **Do not open a public GitHub issue.**
2. Email the maintainer at **tobias.hochguertel@googlemail.com** with a
   description of the vulnerability and steps to reproduce.
3. You will receive an acknowledgment within 48 hours.
4. A fix will be prepared and a security advisory published on GitHub once
   the fix is released.

## Supported Versions

| Version | Supported |
|---------|-----------|
| latest `main` / `dev` | Yes |
| tagged releases on `main` | Yes |
| older versions | No — please upgrade |

## Scope

This policy covers the `InquirerPrompt` package (PyPI) and the
`tobiashochguertel/InquirerPrompt` repository. It does not cover the
upstream `kazhala/InquirerPy` project — report upstream vulnerabilities
through their channels.

## Security Features Enabled

- Secret scanning (with push protection)
- Dependabot security alerts and automated security updates
- CodeQL code scanning (on `main` and `dev`)
- Branch protection on `main` (no force pushes, no deletions)
