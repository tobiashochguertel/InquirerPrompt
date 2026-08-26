# CHANGELOG


## v0.3.4 (2026-03-14)

### Bug Fixes

- Correct GIF URL to raw format, add fork copyright to LICENSE, rename master to main in workflows
  ([`5cde6ce`](https://github.com/tobiashochguertel/InquirerPrompt/commit/5cde6ce92d99168c7a0e2f0f5355c6c43a864b1a))


## v0.3.1 (2026-03-14)

### Bug Fixes

- Only auto-commit compat report on schedule/dispatch (not push) to avoid CD race
  ([`c31238f`](https://github.com/tobiashochguertel/InquirerPrompt/commit/c31238ff3cd159595550c4432ad4b46c02bcb9f8))

- Rewrite compat_check to use pip install + griffe.load (no pypi extra)
  ([`b899aca`](https://github.com/tobiashochguertel/InquirerPrompt/commit/b899aca9d146fd2f6f6bb8b500f7ffea810bac0b))

- Use griffe CLI subprocess for PyPI comparison
  ([`d8f7c96`](https://github.com/tobiashochguertel/InquirerPrompt/commit/d8f7c962914630a58401f9ec33754cf2c6c98356))

### Chores

- Update poetry.lock after adding griffe[pypi] dev dependency
  ([`3faf5c7`](https://github.com/tobiashochguertel/InquirerPrompt/commit/3faf5c7b62f2637ac41e88c2570e5fa95b01ce71))

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>

### Continuous Integration

- Add workflow_dispatch trigger to CI workflow
  ([`826d2c4`](https://github.com/tobiashochguertel/InquirerPrompt/commit/826d2c44997c86362098bb635cbb9a56168d6787))

Allows manually triggering CI runs from GitHub UI or gh CLI, useful for verifying secret changes
  without code commits.

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>

### Documentation

- Fix install instructions, add upstream compatibility report
  ([`3477ae1`](https://github.com/tobiashochguertel/InquirerPrompt/commit/3477ae1ff5a690b50c55c74bc8f645a8bce579b3))

- README.md: fix pip3 install InquirerPy -> InquirerPrompt - README.md: fix python >= 3.7 -> >= 3.9
  (reflect actual CI matrix) - README.md: update PyPI badges with style params to bust CDN cache -
  README.md: add kazhala/InquirerPy as primary credit in Credits section - docs/index.md: fix python
  >= 3.7 -> >= 3.9 - docs/pages/faq.md: add FAQ entry about upstream compatibility -
  docs/pages/compatibility.md: new page explaining drop-in compatibility -
  docs/pages/compat_report.md: stub, populated by CI compat workflow - .github/workflows/compat.yml:
  griffe-based API diff workflow, auto-commits report - scripts/compat_check.py: generates markdown
  compat report using griffe[pypi] - pyproject.toml: add griffe[pypi] dev dependency - Taskfile.yml:
  add compat and compat:check tasks

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>

- Update upstream compatibility report [skip ci]
  ([`e2ea945`](https://github.com/tobiashochguertel/InquirerPrompt/commit/e2ea945f8af2520972e2376926c51ec9e5e0f747))

- Update upstream compatibility report [skip ci]
  ([`423d667`](https://github.com/tobiashochguertel/InquirerPrompt/commit/423d6673c76126685c27152835985dfdf5005624))


## v0.3.0 (2026-03-14)

### Bug Fixes

- Always run poetry install regardless of cache hit
  ([`34937c1`](https://github.com/tobiashochguertel/InquirerPrompt/commit/34937c16b8d1659fbcf92417680183f4b469ba9c))

The conditional poetry install was causing CI failures: when the venv cache exists but is broken
  (wrong Python version, stale), poetry recreates an empty venv but the install step is skipped.
  poetry install is idempotent so running it unconditionally is safe and ensures the env is always
  complete.

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>

- Checkbox icon display error #22
  ([`44ba059`](https://github.com/tobiashochguertel/InquirerPrompt/commit/44ba059f3f45b6763f514366dc6fe4017650bef6))

- Correct PSR v9 config, readthedocs build, and CD install
  ([`29cb9ed`](https://github.com/tobiashochguertel/InquirerPrompt/commit/29cb9ed67839819f0ef94dc69b6900ec7120ebca))

python-semantic-release v9 breaking changes: - commit_parser: 'conventional_commits' →
  'conventional' - Restructure config: branch/upload_to_pypi/upload_to_release/changelog_sections
  removed; replaced with sub-sections branches/changelog/publish - major_on_zero = false added

readthedocs: switch from custom poetry commands to standard python.install using
  docs/requirements.txt (myst-parser lives there, not in pyproject extras)

cd.yml: remove conditional poetry install (same fix as CI)

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>

- Default argument callable raise InvalidArgument
  ([`11f1c51`](https://github.com/tobiashochguertel/InquirerPrompt/commit/11f1c512f8b1276d9d6632bbcf10fed8dba39286))

- Don't adjust priority for processing `raise_keyboard_interrupt` in
  ([`eaba616`](https://github.com/tobiashochguertel/InquirerPrompt/commit/eaba616ad7755bea2f661acda0f2372361139fca))

- Force re-render on choices retrieval finish
  ([`4bce4df`](https://github.com/tobiashochguertel/InquirerPrompt/commit/4bce4df1b58d023ed4fbf9184688ad247fa1a16a))

- Green CI — update pre-commit hooks, fix tests in CI, drop EOL Py 3.9
  ([`d144cbb`](https://github.com/tobiashochguertel/InquirerPrompt/commit/d144cbb46bba7cce1f834227e79466706ddc20cc))

- Update .pre-commit-config.yaml: black 22→24.8, isort 5.10→5.13.2, pydocstyle 6.1→6.3 (fixes
  poetry-core validation failure in CI) - Add tests/conftest.py: use create_app_session(PipeInput,
  DummyOutput) as autouse fixture to avoid 'Stdin is not a terminal' in CI (all 209 tests now pass
  without a real TTY) - Apply black 24.8 reformatting to 19 source files - Drop Python 3.9 from CI
  matrix (EOL Oct 2025; Poetry 2.3.x fails to install on 3.9 runners) - Add pyyaml>=6.0.1 to dev
  deps; poetry.lock resolves to 6.0.3 (fixes PEP 517 build failure on Python 3.12)

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>

- Inconsistant color background for long_instruction
  ([`b947f78`](https://github.com/tobiashochguertel/InquirerPrompt/commit/b947f78c9bb74f7b8a4fafc9c1a33c8075660b78))

- Multiselect #25
  ([`a35ca26`](https://github.com/tobiashochguertel/InquirerPrompt/commit/a35ca26e73024c853a96ea75301866ce535dadd9))

- No error thrown when invalid argument is provided
  ([`8f52a16`](https://github.com/tobiashochguertel/InquirerPrompt/commit/8f52a16ebe939de85bf5c849bedec6dfc492a841))

- Suppress pre-existing pyright override errors from upstream
  ([`8147b28`](https://github.com/tobiashochguertel/InquirerPrompt/commit/8147b28f18398649ba9a91c9ab649ef8f46ece4b))

Suppress reportIncompatibleMethodOverride, reportIncompatibleVariableOverride, and
  reportGeneralTypeIssues in pyrightconfig.json. These 19 errors are pre-existing in the upstream
  codebase (method signature mismatches, return type inconsistencies). They are tracked for future
  cleanup but should not block CI green.

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>

- Typing
  ([`6915996`](https://github.com/tobiashochguertel/InquirerPrompt/commit/691599601511ed1e2e760129b1c744acdb2405be))

- Undefined movement
  ([`6451af5`](https://github.com/tobiashochguertel/InquirerPrompt/commit/6451af5a90217489c9dbacd3761ff6c9774df1a8))

- Update poetry.lock, use dev group syntax, add pyright dep
  ([`21b20eb`](https://github.com/tobiashochguertel/InquirerPrompt/commit/21b20eb71be10b375d4aa35f4f8d6bde7d7e0cbb))

- Regenerate poetry.lock with updated dev dependencies - Migrate [tool.poetry.dev-dependencies] →
  [tool.poetry.group.dev.dependencies] (poetry 2.x syntax, silences deprecation warning) - Add
  pyright ^1.1 as dev dependency (was previously installed via npm in CI) - Add pytest, pytest-cov,
  python-semantic-release as dev dependencies - CI now installs everything via poetry install (no
  npm needed)

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>

- Validation window not staying at the bottom
  ([`01ee6aa`](https://github.com/tobiashochguertel/InquirerPrompt/commit/01ee6aac54aa5db2f6ca5be9947b7b35cf4b3e76))

- **base**: Filter combining raises error
  ([`401b720`](https://github.com/tobiashochguertel/InquirerPrompt/commit/401b720b28c6487e42aeb3d35b85572674645e9a))

- **expand**: Kb not applied
  ([`6b5bbdc`](https://github.com/tobiashochguertel/InquirerPrompt/commit/6b5bbdccd24c21bcabd26b202f8671baaa3c66c6))

- **filepath**: Windows completion #32
  ([`473f22c`](https://github.com/tobiashochguertel/InquirerPrompt/commit/473f22c5bde76329de5144cf5c0b952dd7c6f67b))

- **fuzzy**: Multiselection cannot type space #20
  ([`f07f8e7`](https://github.com/tobiashochguertel/InquirerPrompt/commit/f07f8e7fe819ec060d6b16ddd8eec6e5dbacb000))

- **fuzzy**: Toggle_all #18
  ([`f907c59`](https://github.com/tobiashochguertel/InquirerPrompt/commit/f907c590c3b2da56ef13236bbc071a0402a66a44))

- **number**: Empty input
  ([`79990a1`](https://github.com/tobiashochguertel/InquirerPrompt/commit/79990a195ae1a854158214040cedab4cdb4ab47e))

- **number**: Empty toggle error
  ([`a628087`](https://github.com/tobiashochguertel/InquirerPrompt/commit/a628087a8875f4dbb0168e582cdbc806779b9ecb))

- **number**: Ending zero and adjust cursor position
  ([`a306f26`](https://github.com/tobiashochguertel/InquirerPrompt/commit/a306f26047a7039a1b3e276ba119e7b7d47c0bd7))

- **number**: Exception if max/min is set for float
  ([`3670630`](https://github.com/tobiashochguertel/InquirerPrompt/commit/3670630f44df38fa3f3133e01f4639b68aa2bc25))

- **number**: Negative decimal
  ([`33d622d`](https://github.com/tobiashochguertel/InquirerPrompt/commit/33d622de0a5a54d256d36fd46abaf2f29082fd86))

- **number**: No zero input
  ([`41b9b5e`](https://github.com/tobiashochguertel/InquirerPrompt/commit/41b9b5ef05bb475d5cf95d411347dd2d8db0f8f7))

- **number**: Reset floating number starting at 0
  ([`79da5f8`](https://github.com/tobiashochguertel/InquirerPrompt/commit/79da5f87bd407db8c96a0c5ae92e3fab4600de9b))

- **rawlist**: Index range issue
  ([`2c68d25`](https://github.com/tobiashochguertel/InquirerPrompt/commit/2c68d2560f211f9e999f879c87974fbfc9472062))

- **resolver**: Keybinding not registered
  ([`d220ec5`](https://github.com/tobiashochguertel/InquirerPrompt/commit/d220ec5dd44d76297aa78751357687ba05a9b09a))

- **utils**: Style
  ([`c8452e0`](https://github.com/tobiashochguertel/InquirerPrompt/commit/c8452e01a32a722ef70fc0cec00d3e3e13ca13ee))

### Chores

- Add doc dependencies
  ([`5761613`](https://github.com/tobiashochguertel/InquirerPrompt/commit/57616134a3ef60c3b44a6dabbc3fc4b4b32569cb))

- Added requirements.txt for examples
  ([`dab7055`](https://github.com/tobiashochguertel/InquirerPrompt/commit/dab705544afb87887cd35f896e6ca8fa0d069894))

- Complete Phase 1 fork setup — rename to InquirerPrompt
  ([`799b3f0`](https://github.com/tobiashochguertel/InquirerPrompt/commit/799b3f03e2389d12ef1b08803665e77ce27c3fde))

- Rename PyPI package from InquirerPy to InquirerPrompt - Update repository/documentation URLs to
  fork URLs - Drop Python 3.7/3.8 (EOL), support 3.9–3.12 - Update dev dependencies: bump black,
  isort, pre-commit; add pytest, pytest-cov, python-semantic-release; remove coveralls - Enable
  upload_to_pypi in semantic_release config - Remove superseded lint.yml and test.yml (replaced by
  ci.yml) - Update .readthedocs.yaml with Poetry-based build commands - Update docs/conf.py: project
  name InquirerPrompt, add fork co-maintainer - Update docs/index.md: fork clone URL, pip install
  InquirerPrompt - Update README: correct PyPI package name and RTD docs URL - Fix Codecov action to
  v5

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>

- Reformat
  ([`9966597`](https://github.com/tobiashochguertel/InquirerPrompt/commit/996659700caebff8fceac9d3d2c4781719f77381))

- Removing tooling config for fzy file
  ([`ea734e2`](https://github.com/tobiashochguertel/InquirerPrompt/commit/ea734e279a4215c4d44a5a2d49589d8b613660a7))

- Set up community fork infrastructure
  ([`e07e2dd`](https://github.com/tobiashochguertel/InquirerPrompt/commit/e07e2dd4af8334782d45afaef85f564e27078a4f))

- Add modernized CI workflow (Python 3.9-3.12, Codecov, caching) - Add CD workflow with
  python-semantic-release and PyPI publish - Add Taskfile.yml with lint, format, test, coverage,
  release, docs tasks - Add fork preamble to README.md with upstream attribution - Add
  FORK_SETUP_NOTES.md to .gitignore (contains credentials/setup info) - Add python-semantic-release
  config to pyproject.toml

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>

- Todo
  ([`7003923`](https://github.com/tobiashochguertel/InquirerPrompt/commit/70039236e9e49b7de991f30e3b1f5869a38ee7c1))

- Typo
  ([`a829a4c`](https://github.com/tobiashochguertel/InquirerPrompt/commit/a829a4c84110661cf0502a4382b22137da6dcfbe))

- Udpate dev dependencies
  ([`616168d`](https://github.com/tobiashochguertel/InquirerPrompt/commit/616168df855d7e7e1ca4c9cbb16c7edcb8547238))

- Udpate dev dependencies
  ([`801ba77`](https://github.com/tobiashochguertel/InquirerPrompt/commit/801ba77763045276d036f91227f75f884d4df141))

- Update dependency
  ([`99c436a`](https://github.com/tobiashochguertel/InquirerPrompt/commit/99c436aa47d03dc14bd046047ba5b6f0d4e251c0))

- Update dependency
  ([`e19e4cd`](https://github.com/tobiashochguertel/InquirerPrompt/commit/e19e4cdcaba1f09c67e9bbd338f91ec9f223a63a))

- Update dev dependencies
  ([`abf78ce`](https://github.com/tobiashochguertel/InquirerPrompt/commit/abf78ce37adf1c33acb5edb7ea08c0fd91578127))

- Update dev dependencies
  ([`3664634`](https://github.com/tobiashochguertel/InquirerPrompt/commit/3664634d9e3090b45c05ae196e3e9d9128f89ce3))

- Update dev dependencies
  ([`1738b58`](https://github.com/tobiashochguertel/InquirerPrompt/commit/1738b589fafbb6e335526a3146980e5370338ca1))

- Update dev dependency
  ([`a36dccd`](https://github.com/tobiashochguertel/InquirerPrompt/commit/a36dccdecf3d73ca80899c2414e4fd86a8fd4033))

- Update example
  ([`40c3fd4`](https://github.com/tobiashochguertel/InquirerPrompt/commit/40c3fd4f098f0f0d1a132044a17a964f2b19ad06))

- Update example
  ([`fdad99a`](https://github.com/tobiashochguertel/InquirerPrompt/commit/fdad99a440f1433a222a69dcdaf2d8918f35b4aa))

- Update example folder structure
  ([`aa65412`](https://github.com/tobiashochguertel/InquirerPrompt/commit/aa6541213a25fd923f2f1dd7ecebe16c2aa89276))

- Update exception message
  ([`1adfb93`](https://github.com/tobiashochguertel/InquirerPrompt/commit/1adfb93cc261acf11f87e8bb2b79ef1024fed3d8))

- Update pre-commit hooks version
  ([`987906a`](https://github.com/tobiashochguertel/InquirerPrompt/commit/987906ac65f83fb9f1883b34ba8a0123d17ee132))

- Update secret example to have more hints
  ([`fed0ffe`](https://github.com/tobiashochguertel/InquirerPrompt/commit/fed0ffec66ac6b71942a19e341150b96c3466c63))

- Update typing
  ([`3f72079`](https://github.com/tobiashochguertel/InquirerPrompt/commit/3f72079ea71ccd2445d51db5f76e735d318cdc89))

- Updated fuzzy examples for powershell
  ([`b4de186`](https://github.com/tobiashochguertel/InquirerPrompt/commit/b4de1862f78998a08ca506e6a2757dfd557cbc98))

- Use pfzy
  ([`cbf6487`](https://github.com/tobiashochguertel/InquirerPrompt/commit/cbf64872d07635fa168b9be24893223596cbf8df))

- **examples**: Added number examples
  ([`7f8c97d`](https://github.com/tobiashochguertel/InquirerPrompt/commit/7f8c97daf4c8b410b33fa02deb72eb662c00713d))

- **examples**: Update example wording
  ([`4df3fbb`](https://github.com/tobiashochguertel/InquirerPrompt/commit/4df3fbb847b0795b70450a402b8bff4e5227c105))

### Code Style

- Change the wording from argument to parameter when it make sense
  ([`65511f3`](https://github.com/tobiashochguertel/InquirerPrompt/commit/65511f3dafa8af5d86eda7f3d65ad31011ba770e))

### Continuous Integration

- Fix
  ([`5a0e893`](https://github.com/tobiashochguertel/InquirerPrompt/commit/5a0e8933374c7fe5a312c5d02bc6959d0ae67db9))

- Poetry version update
  ([`187c256`](https://github.com/tobiashochguertel/InquirerPrompt/commit/187c2565e765fba359fa014947c062671e6b8ec5))

### Documentation

- Added docs for choices in dynamic section
  ([`b70198f`](https://github.com/tobiashochguertel/InquirerPrompt/commit/b70198fc2fc90be5e36912f92558335f205d4550))

- Added FAQ
  ([`1722619`](https://github.com/tobiashochguertel/InquirerPrompt/commit/17226190a84cffa5a449e0cd81bd6db0719d23f0))

- Added keybinding documentation to all list type prompts. Closes
  ([`e748d21`](https://github.com/tobiashochguertel/InquirerPrompt/commit/e748d21846ae91553cfb78f61464e35432e04bea))

- Adjust toctree order and more details on keybindings
  ([`be082ce`](https://github.com/tobiashochguertel/InquirerPrompt/commit/be082cee0bd8125f4e7dcb8c819bceebc824860a))

- Api docs
  ([`c0605ed`](https://github.com/tobiashochguertel/InquirerPrompt/commit/c0605edeb18e8d4c7a8ec472ee14887d3004891b))

- Async
  ([`1f80cde`](https://github.com/tobiashochguertel/InquirerPrompt/commit/1f80cde68d3b9e1d38daf0d0bdcf7e47e2e9044b))

- Autodoc level
  ([`57aff27`](https://github.com/tobiashochguertel/InquirerPrompt/commit/57aff2763960261ac2e97d3df89d1013e3fb4737))

- Badge and changelog
  ([`0c58527`](https://github.com/tobiashochguertel/InquirerPrompt/commit/0c58527ede438ce0917ec6049f4f4a904c5d5b04))

- Changelog
  ([`e83ddc0`](https://github.com/tobiashochguertel/InquirerPrompt/commit/e83ddc04dc4082b1a853b038195383e56c56326f))

- Changelog update
  ([`68e9334`](https://github.com/tobiashochguertel/InquirerPrompt/commit/68e9334dc2bae16504dbe65db4ef9c17a4dfab0a))

- Classic syntax async
  ([`a909161`](https://github.com/tobiashochguertel/InquirerPrompt/commit/a9091617adbf6e629b9d8b1bf4604c09777c4f95))

- Dedicated doc for height
  ([`a556a3e`](https://github.com/tobiashochguertel/InquirerPrompt/commit/a556a3e0dbe815c77cf6f70c7c42b227f323d033))

- Docstring update for new _keybinding_factory
  ([`5a3efe1`](https://github.com/tobiashochguertel/InquirerPrompt/commit/5a3efe1380cff834c5109d1d4f078cbace9d9dfc))

- Document inquirer usage and added example
  ([`8a67984`](https://github.com/tobiashochguertel/InquirerPrompt/commit/8a679845b55c04681b6244a5808f716a4a5d2a57))

- Examples on using keypress event within keybinding functions #27
  ([`7194939`](https://github.com/tobiashochguertel/InquirerPrompt/commit/71949392cae2459edebb5663453793f93160907b))

- Filepath doc migrated to sphinx and handle todo
  ([`3fe8a29`](https://github.com/tobiashochguertel/InquirerPrompt/commit/3fe8a29c007b6ab52685ab9c9eb396111a6bdbd2))

- Fix autodata
  ([`ba93611`](https://github.com/tobiashochguertel/InquirerPrompt/commit/ba93611aafc39c225f98e9630f8e241acc867c41))

- Fix build
  ([`745fb15`](https://github.com/tobiashochguertel/InquirerPrompt/commit/745fb152c318ae292ced79207902db5e294c28b1))

- Fix duplicate tags
  ([`4e7cda3`](https://github.com/tobiashochguertel/InquirerPrompt/commit/4e7cda3e5ee481dbdfd32a65f0ff89e83b8c425b))

- Fix README quick start instruction
  ([`048cb8a`](https://github.com/tobiashochguertel/InquirerPrompt/commit/048cb8a321f835b4780f06b3a01737e9a16b9cef))

- Init
  ([`fabb25b`](https://github.com/tobiashochguertel/InquirerPrompt/commit/fabb25b47a91b844a807cbb4bdbe636d884ff778))

- Init number doc
  ([`91ea3c6`](https://github.com/tobiashochguertel/InquirerPrompt/commit/91ea3c6ebc2af0337e9f8d6003cb75350c06e91f))

- Migrate expand prompt docs to sphinx
  ([`b5f02a5`](https://github.com/tobiashochguertel/InquirerPrompt/commit/b5f02a51752fb682566cb2fa8d9a16e3a4affae7))

- Migrate fuzzy doc to sphinx
  ([`d9e662d`](https://github.com/tobiashochguertel/InquirerPrompt/commit/d9e662d3a8660ef122da1fa69a48e6c6fa9e0dcb))

- Migrate input prompt to sphinx
  ([`cf98d5a`](https://github.com/tobiashochguertel/InquirerPrompt/commit/cf98d5af74d05a811a132a8c79b992e330ad89be))

- Migrate list docs to sphinx
  ([`2874035`](https://github.com/tobiashochguertel/InquirerPrompt/commit/2874035a6b982b49e5d8a04e9c7d053d76c412e6))

- Migrate secret docs to sphinx
  ([`01c1867`](https://github.com/tobiashochguertel/InquirerPrompt/commit/01c1867f4862c6b5d8d4a313787f3541b530dc2d))

- Migrated checkbox doc to sphinx
  ([`ed78e8d`](https://github.com/tobiashochguertel/InquirerPrompt/commit/ed78e8d96e4183f510fc3a552a77c9c1b6c336af))

- Migrated confirm doc to sphinx
  ([`94c07a0`](https://github.com/tobiashochguertel/InquirerPrompt/commit/94c07a0f940144c4373695622fe4848e0164dad7))

- Migrated docs for rawlist to sphinx
  ([`2f7a3e2`](https://github.com/tobiashochguertel/InquirerPrompt/commit/2f7a3e2057947af6d873a12cfd5e15e9a1c1a885))

- Migrated misc section
  ([`7106be5`](https://github.com/tobiashochguertel/InquirerPrompt/commit/7106be5f863eb1c651c053989f550dd12eb8d59a))

- Migrated prompt doc
  ([`c5d6d74`](https://github.com/tobiashochguertel/InquirerPrompt/commit/c5d6d7430117903c24c5f1a3f684b1bc2a299e93))

- Missing doc for magic method
  ([`855abb3`](https://github.com/tobiashochguertel/InquirerPrompt/commit/855abb3c5ff028e535a04bd99d73369ccd2915d8))

- Multiselect
  ([`363a6d7`](https://github.com/tobiashochguertel/InquirerPrompt/commit/363a6d779fb9b2bd3f1d08cd178c15c4eeabeded))

- Readthedocs build config
  ([`7b07ce8`](https://github.com/tobiashochguertel/InquirerPrompt/commit/7b07ce8eb3736180e8a73d1e148b5aa9d076916e))

- Remove s3 demo code
  ([`61ccdf0`](https://github.com/tobiashochguertel/InquirerPrompt/commit/61ccdf0ef0a0966f0d618dbc3db7561087d634f4))

- Toctree refactor
  ([`ec44a4c`](https://github.com/tobiashochguertel/InquirerPrompt/commit/ec44a4c88989ef657890af26b340d51b2c05ac05))

- Typing
  ([`f04c249`](https://github.com/tobiashochguertel/InquirerPrompt/commit/f04c249b423ef742550f46449c26346e2a4cb8f2))

- Typo
  ([`a057572`](https://github.com/tobiashochguertel/InquirerPrompt/commit/a057572fdb645f3d11de55c010ddabf52c06be00))

- Typo
  ([`f576d20`](https://github.com/tobiashochguertel/InquirerPrompt/commit/f576d20843e15c6a6220060424a3ea4a016c08ad))

- Udpate doc link
  ([`8649b6f`](https://github.com/tobiashochguertel/InquirerPrompt/commit/8649b6f20f1f8f04476efa9ed2ceb81954518845))

- Update
  ([`fb93e14`](https://github.com/tobiashochguertel/InquirerPrompt/commit/fb93e14dcb869082d7c2c803ff08cb5cebf5c443))

- Update
  ([`15ae44a`](https://github.com/tobiashochguertel/InquirerPrompt/commit/15ae44abd6c5f1767e72b5143c781ad776cdae2b))

- Update CHANGELOG
  ([`093f54c`](https://github.com/tobiashochguertel/InquirerPrompt/commit/093f54c89e05dbcde65d0ebacb579070bbbf48b6))

- Update changelog
  ([`801b3af`](https://github.com/tobiashochguertel/InquirerPrompt/commit/801b3aff491c8863239b09425e615fd7aef62a3a))

- Update changelog
  ([`13d689f`](https://github.com/tobiashochguertel/InquirerPrompt/commit/13d689f1010df44d516dd9123cebbbdc1c8b123a))

- Update doc to use `Choice` over dictionary choices
  ([`a504ca0`](https://github.com/tobiashochguertel/InquirerPrompt/commit/a504ca0148f63c518f0ab19b86c1798510760ea6))

- Update docstring
  ([`6cc6e70`](https://github.com/tobiashochguertel/InquirerPrompt/commit/6cc6e70003ee6ead39cfd3320144bb6653c17136))

- Update docstring
  ([`9257616`](https://github.com/tobiashochguertel/InquirerPrompt/commit/9257616e5571c132f03b80228769a7fe71f236be))

- Update docstring base simple
  ([`a8f00b1`](https://github.com/tobiashochguertel/InquirerPrompt/commit/a8f00b1f30319126c2119b0c835ea133060116fa))

- Update example and readme
  ([`2e4b181`](https://github.com/tobiashochguertel/InquirerPrompt/commit/2e4b1812af7b96978bcddff41a2c36933b1b62f8))

- Update examples using `Choice` and `ExpandChoice`
  ([`2bae8d3`](https://github.com/tobiashochguertel/InquirerPrompt/commit/2bae8d36b32c2684ce3b756a109340b57fa2b340))

- Update kb doc
  ([`c0b3d04`](https://github.com/tobiashochguertel/InquirerPrompt/commit/c0b3d044d4453c80cda17b864935444fd065e9dc))

- Update kbi doc and links
  ([`1742295`](https://github.com/tobiashochguertel/InquirerPrompt/commit/1742295b46d47d66d79661160007d592e704b484))

- Update keybinding documentation
  ([`5b81703`](https://github.com/tobiashochguertel/InquirerPrompt/commit/5b81703b2ab577f6b489e6456ec44c7e4088aaa5))

- Update links
  ([`fe3e32f`](https://github.com/tobiashochguertel/InquirerPrompt/commit/fe3e32fc0d036546a51e3ad181d7d51cc97d9f8b))

- Update readme
  ([`ecb9a33`](https://github.com/tobiashochguertel/InquirerPrompt/commit/ecb9a3338fe19d0f3e7cc287ffcbca025677f098))

- Update remaining readthedocs URLs to InquirerPrompt
  ([`04381d7`](https://github.com/tobiashochguertel/InquirerPrompt/commit/04381d72ae318fe3829ec98c830d2a104d88b687))

Replace leftover inquirerpy.readthedocs.io links with InquirerPrompt.readthedocs.io throughout
  README.md.

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>

- Update style doc
  ([`d8ee146`](https://github.com/tobiashochguertel/InquirerPrompt/commit/d8ee146c3169e73cb2420b6526d749f79b50d80d))

- Update titles and added dynamic page
  ([`1aea5b4`](https://github.com/tobiashochguertel/InquirerPrompt/commit/1aea5b43f694c749e1162d0c73dd84c97196f269))

- Update titles and kb doc
  ([`07633a6`](https://github.com/tobiashochguertel/InquirerPrompt/commit/07633a6642f579134af17a5838c739f068e46b87))

- Use literal import
  ([`2b1b38d`](https://github.com/tobiashochguertel/InquirerPrompt/commit/2b1b38defe7de1c77590c501eeef24ace0535522))

- Validator documentation
  ([`4269000`](https://github.com/tobiashochguertel/InquirerPrompt/commit/4269000425b91e1eb0b5897a0712cc84f87b9589))

- **base**: Update complex prompt doc
  ([`11dbdd2`](https://github.com/tobiashochguertel/InquirerPrompt/commit/11dbdd2cc7ea004088148bcfe5e99475cac78e90))

- **changelog**: `raise_keyboard_interrupt`
  ([`135d0ae`](https://github.com/tobiashochguertel/InquirerPrompt/commit/135d0ae0d5da30711fccf4bd296d6129d37318ad))

- **changelog**: Added reasons for checkbox prompt icon spacing changes
  ([`e84f3b9`](https://github.com/tobiashochguertel/InquirerPrompt/commit/e84f3b95b317cbcca8fe014829aad18c985c9d1f))

- **changelog**: Choice and ExpandChoice
  ([`289970c`](https://github.com/tobiashochguertel/InquirerPrompt/commit/289970cf698bc2d91d8e79ce74bbe5620f5d8838))

- **exceptions**: Docstring
  ([`013251b`](https://github.com/tobiashochguertel/InquirerPrompt/commit/013251bcec4c47859283da9c02d0d312001f95ba))

- **expand**: Document the new parameter `expand_help`
  ([`0c048f5`](https://github.com/tobiashochguertel/InquirerPrompt/commit/0c048f54d5f0cbffa030628eda539085d27ab66b))

- **expand**: New choice doc
  ([`6ab1dbe`](https://github.com/tobiashochguertel/InquirerPrompt/commit/6ab1dbef6f2bc6f9ffaab54b08629b7e234fc9d7))

- **fuzzy**: Exact match
  ([`35c879e`](https://github.com/tobiashochguertel/InquirerPrompt/commit/35c879effe4e27cf0b3791ef5f3af7c11deb02f2))

- **fuzzy**: Toggle-exact keybinding #34
  ([`1adb55b`](https://github.com/tobiashochguertel/InquirerPrompt/commit/1adb55b371d592c2d6c5c23187f4594f05237f30))

- **number**: Added examples and demo
  ([`d8b34c0`](https://github.com/tobiashochguertel/InquirerPrompt/commit/d8b34c06681d3308fcd78348acc059c3705da3c8))

- **number**: Docstring
  ([`e6dd3a4`](https://github.com/tobiashochguertel/InquirerPrompt/commit/e6dd3a448e6646a7b195e926938f7c9765b9e871))

- **number**: Empty default value
  ([`cf04f9a`](https://github.com/tobiashochguertel/InquirerPrompt/commit/cf04f9ae3a4e264cd4dc3f6eb45faa43a70d60c8))

- **number**: Include dot kb
  ([`d93accf`](https://github.com/tobiashochguertel/InquirerPrompt/commit/d93accf05a7cf5253df68fff814feaae3d495c3d))

- **number**: Internal docs
  ([`6eab367`](https://github.com/tobiashochguertel/InquirerPrompt/commit/6eab36722650d3227c4f3843a1402975f25afd16))

- **number**: Note that its not yet released
  ([`13f0a2e`](https://github.com/tobiashochguertel/InquirerPrompt/commit/13f0a2e3411b1d2d6e2cc7f4879edeb4022086a0))

- **number**: Replace mode
  ([`1d9d578`](https://github.com/tobiashochguertel/InquirerPrompt/commit/1d9d5782d2fef53e7cfd33c0e51286adba371b72))

- **number**: Replace_mode
  ([`0382ac9`](https://github.com/tobiashochguertel/InquirerPrompt/commit/0382ac9cfca2ae9e791f40c1c579065c59c96483))

- **readme**: Fix example
  ([`27ba8e2`](https://github.com/tobiashochguertel/InquirerPrompt/commit/27ba8e20a818dc2db915feed7e8c0771f016433a))

- **resolver**: Docstring
  ([`8a8fc0f`](https://github.com/tobiashochguertel/InquirerPrompt/commit/8a8fc0f717bd619c603cb630fcdf40e39d405646))

- **separator**: Docstring style
  ([`a3dcc1b`](https://github.com/tobiashochguertel/InquirerPrompt/commit/a3dcc1b6854e60336325da777c6313a0dc03cedb))

- **utils**: Fix example
  ([`5a71825`](https://github.com/tobiashochguertel/InquirerPrompt/commit/5a718259df475e68e71b5e0eaa85a80f4c064bcc))

- **utils**: Update docstring
  ([`802d911`](https://github.com/tobiashochguertel/InquirerPrompt/commit/802d91145bcc03690972057e206f3585825594b9))

### Features

- Add formatter config files
  ([`9c70434`](https://github.com/tobiashochguertel/InquirerPrompt/commit/9c7043479d5b60df12614a0d2391113093cc192c))

- Added `long_instruction` parameter for input prompts
  ([`28ef1fc`](https://github.com/tobiashochguertel/InquirerPrompt/commit/28ef1fc2029936647aab15c0bf0e6c74b4f6c002))

- Added ability to set error for PromptSession based propts
  ([`db7c5aa`](https://github.com/tobiashochguertel/InquirerPrompt/commit/db7c5aabc718b0e75676c4e5e01e8b104acd0290))

- Added async support for alternate syntax #30
  ([`75070c3`](https://github.com/tobiashochguertel/InquirerPrompt/commit/75070c3c40dcf7b0ef7a53e27cd32a7a811e1713))

- Added async support for classic syntax
  ([`c4296ce`](https://github.com/tobiashochguertel/InquirerPrompt/commit/c4296ceb802d031b3f9cddc0b762ca8507516ee9))

- Added Choice and ExpandChoice class for more pythonic way of
  ([`ceaa161`](https://github.com/tobiashochguertel/InquirerPrompt/commit/ceaa1618749db4b63eb60b41b1c383bb60e7ddf9))

- Added keybinding customisation option for all prompts now
  ([`08eaec1`](https://github.com/tobiashochguertel/InquirerPrompt/commit/08eaec1c694691804b307899065f26f668fdf55d))

- Added option `mandatory` to control if a prompt can be skipped #10
  ([`be3576d`](https://github.com/tobiashochguertel/InquirerPrompt/commit/be3576d2b3d54cf9055f4c9a5d4402a32ab95859))

- Allow movement
  ([`edc6f16`](https://github.com/tobiashochguertel/InquirerPrompt/commit/edc6f1682937d6ef2d91592b9644ce4a55ae81ad))

- Allow single dictionary keybinding binds
  ([`3cf99e6`](https://github.com/tobiashochguertel/InquirerPrompt/commit/3cf99e618924e2ce294579eb2b6490df06bd8060))

- Border for list, rawlist, expand and checkbox prompt
  ([`7f97c62`](https://github.com/tobiashochguertel/InquirerPrompt/commit/7f97c6235f85ed3992c6e540722a4e1ba384855e))

- Dedicated instruction area (tips). #7
  ([`e59548c`](https://github.com/tobiashochguertel/InquirerPrompt/commit/e59548cf0df7490eb59ab89b2d6989403b812190))

- Enable number prompt for the classic syntax
  ([`52a51cf`](https://github.com/tobiashochguertel/InquirerPrompt/commit/52a51cfd01c9855a3360ebf5b5b49e3fc953989e))

- Hide integral window if not float
  ([`c12daed`](https://github.com/tobiashochguertel/InquirerPrompt/commit/c12daed9af93bf126ca488455fbde2a30aa0eec5))

- Init number prompt
  ([`a34b920`](https://github.com/tobiashochguertel/InquirerPrompt/commit/a34b9202f5e1223e87c983f38acca05b2c4f94d3))

- Option to configure event loop exception handler
  ([`bc1a29e`](https://github.com/tobiashochguertel/InquirerPrompt/commit/bc1a29e0267ca54ab4dfd9c03554347a8d9b501c))

- Raise_keyboard_interrupt=false also checks mandatory
  ([`c7ce641`](https://github.com/tobiashochguertel/InquirerPrompt/commit/c7ce641f4d0c874b6933431696f538b6aa57a12b))

- Support dynamic invalid_message in list type prompts while using Validator
  ([`03e176d`](https://github.com/tobiashochguertel/InquirerPrompt/commit/03e176d862ebec338d78f7ccdc8e877d3847b81d))

- Support spinner in all list prompts
  ([`b81ebe9`](https://github.com/tobiashochguertel/InquirerPrompt/commit/b81ebe947f48de9a6ce8836a5e966afd24894ea7))

- **base**: Add _choices_callback function
  ([`e38fa39`](https://github.com/tobiashochguertel/InquirerPrompt/commit/e38fa39c1a3bf8a67e44c98660e26c30001dc32d))

- **base**: Added option to skip question #10
  ([`2abeaad`](https://github.com/tobiashochguertel/InquirerPrompt/commit/2abeaad93e3c179bbc6396ed60f05c14b9d98c7a))

- **base**: Added optional spinner
  ([`4f03870`](https://github.com/tobiashochguertel/InquirerPrompt/commit/4f03870e59836e97789774b9f5c25de8a4625e40))

- **base**: Transform_async on the blocking choice_func
  ([`07a40b9`](https://github.com/tobiashochguertel/InquirerPrompt/commit/07a40b9bd3e62adad13264b7068cda99477b36c0))

- **base**: Update control class to handle async
  ([`6ac5e4e`](https://github.com/tobiashochguertel/InquirerPrompt/commit/6ac5e4e3dd66b09f6bfbb652ce1b927f908545a7))

- **expand**: Added option `expand_help` to customise expand key and
  ([`74c6f13`](https://github.com/tobiashochguertel/InquirerPrompt/commit/74c6f135ff04b199c4ded441a4cde8dde48c0ad1))

- **fuzzy**: Added kb to toggle exact match
  ([`cd8450c`](https://github.com/tobiashochguertel/InquirerPrompt/commit/cd8450ce67d61c141481759f22803002fedf89a8))

- **fuzzy**: Support exact match
  ([`a8cd060`](https://github.com/tobiashochguertel/InquirerPrompt/commit/a8cd06033b62bcd9c5d95027675fbbf642722cd1))

- **fuzzy**: Support optional spinner
  ([`8736b7a`](https://github.com/tobiashochguertel/InquirerPrompt/commit/8736b7aa4327ac7233a1577df39b72282f99a281))

- **kb**: Grant more access to `prompt_toolkit` features
  ([`984bfca`](https://github.com/tobiashochguertel/InquirerPrompt/commit/984bfcaf402c3b1724a378f28d7b0d60f10d27ef))

- **number**: Added additional kb for dot
  ([`67036f9`](https://github.com/tobiashochguertel/InquirerPrompt/commit/67036f9d661796f97ca6b5ebb620f41df7304ae7))

- **number**: Added input buffers
  ([`c918cb0`](https://github.com/tobiashochguertel/InquirerPrompt/commit/c918cb0c1f21718af9a722abdad2042c63a0ae9c))

- **number**: Additional customisation around replace mode
  ([`1b81023`](https://github.com/tobiashochguertel/InquirerPrompt/commit/1b810239abbc639e2ad97ae052086c0eeb78dd16))

- **number**: Allow customisation on decimal symbol
  ([`b0bde41`](https://github.com/tobiashochguertel/InquirerPrompt/commit/b0bde419922d9cb4aee2c1952c8723c70d17ee9a))

- **number**: Allow empty buffer default
  ([`adf9f93`](https://github.com/tobiashochguertel/InquirerPrompt/commit/adf9f93a60ac5efd6fa716d7878a6bc57ba18ad0))

- **number**: Allow zero decimal input
  ([`9d09a0f`](https://github.com/tobiashochguertel/InquirerPrompt/commit/9d09a0f30c96a3e56d7c02f2148c0ad5600a970c))

- **number**: Auto adjust cursor position for negative toggle
  ([`318b2bf`](https://github.com/tobiashochguertel/InquirerPrompt/commit/318b2bf791ff13d273cd0bc342dbdd2bd7b1aa30))

- **number**: Enable full vi mode
  ([`bce0f00`](https://github.com/tobiashochguertel/InquirerPrompt/commit/bce0f001875e420862347ad52d37938a6db55492))

- **number**: Fix sciencetific notation
  ([`da6ade3`](https://github.com/tobiashochguertel/InquirerPrompt/commit/da6ade384a3405b9c08ea0657f96ed5c1bded22e))

- **number**: Force empty result when empty input
  ([`8536691`](https://github.com/tobiashochguertel/InquirerPrompt/commit/85366918f93292d09e4f2a9339ba469be6919f07))

- **number**: Handle answer
  ([`108b134`](https://github.com/tobiashochguertel/InquirerPrompt/commit/108b134128d7ae08066b4e3427aabea16407a90a))

- **number**: Handle increase and decrease
  ([`32a77b2`](https://github.com/tobiashochguertel/InquirerPrompt/commit/32a77b275174881d8fde1c46072bbde92d075662))

- **number**: Handle number input
  ([`f4103b9`](https://github.com/tobiashochguertel/InquirerPrompt/commit/f4103b94483e634a22e00b98615cc425cd8148e1))

- **number**: Handle sn on text change
  ([`a2175f4`](https://github.com/tobiashochguertel/InquirerPrompt/commit/a2175f45783daa80212a0309d42585d8dec97a85))

- **number**: Replace mode by default if value is zero
  ([`8145c80`](https://github.com/tobiashochguertel/InquirerPrompt/commit/8145c80e3bb581badd0fa255b9d712c3cceb406a))

- **number**: Set default value
  ([`ab5a2ae`](https://github.com/tobiashochguertel/InquirerPrompt/commit/ab5a2ae6d80770820b69d9e67941b7d39c000c09))

- **number**: Toggle negative
  ([`c7216bc`](https://github.com/tobiashochguertel/InquirerPrompt/commit/c7216bc3208ab924b3d55f064218c3cca878408f))

- **style**: Added long_instruction class
  ([`011586b`](https://github.com/tobiashochguertel/InquirerPrompt/commit/011586b444e65deeb8e77d56e9cd49e91f37b44b))

- **utils**: Added transform_async and ListChoices alias
  ([`1a4cb46`](https://github.com/tobiashochguertel/InquirerPrompt/commit/1a4cb4651c8a3c89c8e12327aace41c6247d4559))

### Refactoring

- Added raise_keyboard_interrupt to prompt initialisation option
  ([`1ac6314`](https://github.com/tobiashochguertel/InquirerPrompt/commit/1ac63146f81368a3f18a609991fa96ed2cb5efef))

- Adjust default keybinding for toggle multiple choices
  ([`0213079`](https://github.com/tobiashochguertel/InquirerPrompt/commit/0213079bc6e561b143fa7c48e49b861750eee496))

- Dedicated container module
  ([`2234e8b`](https://github.com/tobiashochguertel/InquirerPrompt/commit/2234e8bb06f70fc67d708bb9f05a87dbec9aea7c))

- Have tips window stay at the bottom, don't float #7
  ([`51d113b`](https://github.com/tobiashochguertel/InquirerPrompt/commit/51d113b207091c6af9c6a0e81264806cfbce1a65))

- Internal class args
  ([`5aaa092`](https://github.com/tobiashochguertel/InquirerPrompt/commit/5aaa09265e395c5de99024952e8708f0eb92b69f))

- Keybinding typing alias
  ([`4558f9b`](https://github.com/tobiashochguertel/InquirerPrompt/commit/4558f9b982bad646f100a33fc23292bc498c8209))

- Mirgrate to pfzy
  ([`ba215d1`](https://github.com/tobiashochguertel/InquirerPrompt/commit/ba215d10fb3fe8157c18cb4f25b28ee90b885f6b))

- Move instruction window out of floating layout
  ([`5a7500a`](https://github.com/tobiashochguertel/InquirerPrompt/commit/5a7500a49b8c02809a487ed7324b4a36c296377e))

- Move spinner to dedicated module
  ([`356a2ab`](https://github.com/tobiashochguertel/InquirerPrompt/commit/356a2ab35badae9fed6f3e9cdf70d58bae2659a9))

- Overload register_kb instead of creating new methods
  ([`42aa7f4`](https://github.com/tobiashochguertel/InquirerPrompt/commit/42aa7f4b4c8f6687d6fdf9b5b7075d7e520b81eb))

- Private attr
  ([`e1513ee`](https://github.com/tobiashochguertel/InquirerPrompt/commit/e1513ee8b176ec785134bd4a286e0f5a954f5b3b))

- Remove unused util function
  ([`4db519b`](https://github.com/tobiashochguertel/InquirerPrompt/commit/4db519b4355d852abf0a0c2e2378352d7d4f124c))

- Rename `tips` argument to `long_instruction` #7
  ([`df4119e`](https://github.com/tobiashochguertel/InquirerPrompt/commit/df4119e6beaafb1b461a1f369f6cb725ba839c5d))

- Rename InquirerPyUIControl to InquirerPyUIListControl
  ([`f2d4262`](https://github.com/tobiashochguertel/InquirerPrompt/commit/f2d42623ded3747b301ba1c8628540668fefe06b))

- Rename typing alias
  ([`75266bf`](https://github.com/tobiashochguertel/InquirerPrompt/commit/75266bfb1e4413b6bf4fe2ec9fffc42535d0f3b6))

- Validation window
  ([`848564b`](https://github.com/tobiashochguertel/InquirerPrompt/commit/848564bfcfa81c83936e62388a50c88b17176e1b))

- Validation window
  ([`caef887`](https://github.com/tobiashochguertel/InquirerPrompt/commit/caef88706c1349815c4bfe527bcd6d0162c5bf3f))

- **base**: Remove abstraction for _format_choices
  ([`9c0ab42`](https://github.com/tobiashochguertel/InquirerPrompt/commit/9c0ab42bcdbc210f11ecfa01f28979d6c1821077))

- **base**: Remove unused kb bind
  ([`91661ae`](https://github.com/tobiashochguertel/InquirerPrompt/commit/91661ae45b02a19c8379f7cb51d5570acad01910))

- **checkbox**: Use new unicode sequence and remove default spacing
  ([`164ad5f`](https://github.com/tobiashochguertel/InquirerPrompt/commit/164ad5fd5206eed1b8faa4c5462006d879036008))

- **filepath**: Typing alias and update test
  ([`f604321`](https://github.com/tobiashochguertel/InquirerPrompt/commit/f604321ab3ca115008e9c32ee1d409185075cb4c))

- **fuzzy**: No border by default
  ([`88501fe`](https://github.com/tobiashochguertel/InquirerPrompt/commit/88501fe93c7ec7515ab2a14201848ab08d0c6c06))

- **fuzzy**: Use _on_rendered instead of after_render
  ([`5e9dd52`](https://github.com/tobiashochguertel/InquirerPrompt/commit/5e9dd5295845b5be308def4d6ee634a8ba014096))

- **input**: Better kb registration
  ([`5b712a1`](https://github.com/tobiashochguertel/InquirerPrompt/commit/5b712a1b89d0029ba72aa2fe318fd42964c7e3e8))

- **number**: Disable replace_mode by default
  ([`e493793`](https://github.com/tobiashochguertel/InquirerPrompt/commit/e493793cdf79c30e61622fb4d504ae4d3e30b558))

- **number**: Move buffer detection logic
  ([`d2df65c`](https://github.com/tobiashochguertel/InquirerPrompt/commit/d2df65c6e5e70abb631e20e3e78cf747fa3c716c))

- **number**: On render
  ([`0052fc9`](https://github.com/tobiashochguertel/InquirerPrompt/commit/0052fc9c56f8fe491db4795f883f4256dca4157a))

- **number**: Rename to replace mode
  ([`3b9d27c`](https://github.com/tobiashochguertel/InquirerPrompt/commit/3b9d27c52285b923b4620c123aeaf972a3e087a2))

- **number**: Use Decimal over float
  ([`7546971`](https://github.com/tobiashochguertel/InquirerPrompt/commit/75469710a2a63dfe6c1eab86efdceca9bf44e371))

- **rawlist**: Typings
  ([`37ebdde`](https://github.com/tobiashochguertel/InquirerPrompt/commit/37ebddeb1dfbadab77b20b4b670d377f8a0247ca))

- **style**: Color update
  ([`e38579b`](https://github.com/tobiashochguertel/InquirerPrompt/commit/e38579bc93a3b295603a90ece4406ffbe40386fe))

- **validator**: Update validator attrs to private
  ([`30cbe7e`](https://github.com/tobiashochguertel/InquirerPrompt/commit/30cbe7e246b9cd1222ac383c0d16c10b880aa693))

### Testing

- Added tests for new raise_keyboard_interrupt option
  ([`e6d2b78`](https://github.com/tobiashochguertel/InquirerPrompt/commit/e6d2b787fa953ca7e8291938c79eba179181f8e1))

- Async execution
  ([`c944eaa`](https://github.com/tobiashochguertel/InquirerPrompt/commit/c944eaa565df26f4ba36af3eafa333c479f6eed1))

- Callable default
  ([`8c17cc0`](https://github.com/tobiashochguertel/InquirerPrompt/commit/8c17cc0f8bdfb70925b17d364ec43a6f856e597e))

- Check pkg avaialble in both classic and alternaive
  ([`56ddbc9`](https://github.com/tobiashochguertel/InquirerPrompt/commit/56ddbc9fa92ef39cb548d38cc9debf21fafe5b43))

- Height calculation adjustment
  ([`29864c1`](https://github.com/tobiashochguertel/InquirerPrompt/commit/29864c145210a195e674e67faaa6d49f0998a10a))

- Kbi
  ([`1421e94`](https://github.com/tobiashochguertel/InquirerPrompt/commit/1421e94b8772f5dc1f348279ab9741848e869443))

- Long_instruction
  ([`3bf13fc`](https://github.com/tobiashochguertel/InquirerPrompt/commit/3bf13fc1ac41179a8de1971d02ba65bf8f33e746))

- More coverage
  ([`56b227a`](https://github.com/tobiashochguertel/InquirerPrompt/commit/56b227ac8a654f3af96667544a1acfb02f805d23))

- Multiselect & kb
  ([`fb46d86`](https://github.com/tobiashochguertel/InquirerPrompt/commit/fb46d866d7899d7537aae8d129d232c5ab773661))

- Refactor
  ([`4305f60`](https://github.com/tobiashochguertel/InquirerPrompt/commit/4305f60db4c666e995da3978004cd43ac44e9113))

- Refactor
  ([`11b1107`](https://github.com/tobiashochguertel/InquirerPrompt/commit/11b11074aa3cc8a7e3230a45a972a9aa5ae67fd2))

- Refactor
  ([`fc08357`](https://github.com/tobiashochguertel/InquirerPrompt/commit/fc08357e8e24b5464d6a094c43e52c195c5ef86c))

- Remove test for transform_async
  ([`e95dde5`](https://github.com/tobiashochguertel/InquirerPrompt/commit/e95dde5b76361bca53d3d22762001e4307af66a8))

- Setup base class tests
  ([`4ad8375`](https://github.com/tobiashochguertel/InquirerPrompt/commit/4ad83758a59119907280e946689802eacc6c9530))

- Style test update
  ([`4723978`](https://github.com/tobiashochguertel/InquirerPrompt/commit/47239789ecdf0cea93be38b8a70464d873c4134f))

- Tips
  ([`56a3557`](https://github.com/tobiashochguertel/InquirerPrompt/commit/56a3557c9130e8d90e5bf01972d5312dcfb916a6))

- Update `long_instruction` tests
  ([`2fc7ae3`](https://github.com/tobiashochguertel/InquirerPrompt/commit/2fc7ae311c2f76e4c86d5d765791d7c271740236))

- Update due to refactor
  ([`db66090`](https://github.com/tobiashochguertel/InquirerPrompt/commit/db66090af4276a1195ed6d9b5785d23807a5afb7))

- Update height calculation tests
  ([`4a4b53b`](https://github.com/tobiashochguertel/InquirerPrompt/commit/4a4b53b58ed935c09f4bfd1914b64019feb469f2))

- Update kb and style test
  ([`8437068`](https://github.com/tobiashochguertel/InquirerPrompt/commit/84370684ca285982c75a3fd777d7ffc185d4fa59))

- Update mocking target
  ([`2fd5d41`](https://github.com/tobiashochguertel/InquirerPrompt/commit/2fd5d412d786d57b90e98a42cb63ca8b390df983))

- Update test to handle new async cases
  ([`be5b194`](https://github.com/tobiashochguertel/InquirerPrompt/commit/be5b194986ec65eaa3f1d0b91727c54b49953a09))

- Update test to handle new skipped state
  ([`391d89e`](https://github.com/tobiashochguertel/InquirerPrompt/commit/391d89eaf4b7d71b7c129212476696afdcec8962))

- **base**: _keybinding_factory
  ([`e011dbe`](https://github.com/tobiashochguertel/InquirerPrompt/commit/e011dbe6ad08f2d83242e867e8d16290d0cc5fd8))

- **base**: Exception handler
  ([`1752036`](https://github.com/tobiashochguertel/InquirerPrompt/commit/1752036da3b60f8dc3de006d74c38734d9ec4f96))

- **base**: Handle_skip
  ([`903e737`](https://github.com/tobiashochguertel/InquirerPrompt/commit/903e73741504591b1f57a8ffa7c8f8811ea0e9a8))

- **base**: Long_instruction height offset calculation
  ([`7c0b86d`](https://github.com/tobiashochguertel/InquirerPrompt/commit/7c0b86d80f1e9b9a652123b2ead5c9aee989dab1))

- **base**: More coverage
  ([`10c96f0`](https://github.com/tobiashochguertel/InquirerPrompt/commit/10c96f0f06aecf651b6d45f4d173bd5a94b7f164))

- **checkbox**: Adjust test for last refactor commit
  ([`c4faadc`](https://github.com/tobiashochguertel/InquirerPrompt/commit/c4faadc74ea7958798e48290c9701fe55210cc39))

- **filepath**: Windows completion
  ([`4828e90`](https://github.com/tobiashochguertel/InquirerPrompt/commit/4828e9056839a50a5f686deade2068c10fda977e))

- **fuzzy**: Add test for #20
  ([`faec808`](https://github.com/tobiashochguertel/InquirerPrompt/commit/faec808b08f0993e4af4e2abb30e4723d7dd8526))

- **fuzzy**: Exact match
  ([`9faaed8`](https://github.com/tobiashochguertel/InquirerPrompt/commit/9faaed89038edac8a0bc8b3ee606f8faf3cb652e))

- **fuzzy**: Height adjustment
  ([`b7df510`](https://github.com/tobiashochguertel/InquirerPrompt/commit/b7df510149ccb97242fcf7b011fa63b50d7c027d))

- **fuzzy**: Toggle exact
  ([`36b7c57`](https://github.com/tobiashochguertel/InquirerPrompt/commit/36b7c57127e2eea4bba6516e9ed3164145eb6c35))

- **fuzzy**: Toggle_all and filter choice interaction
  ([`7779fd8`](https://github.com/tobiashochguertel/InquirerPrompt/commit/7779fd81313f84c9612c3d07cad643176c64d649))

- **input**: _handle_completion
  ([`90369a5`](https://github.com/tobiashochguertel/InquirerPrompt/commit/90369a5e3e61fde83127c3e53ae3743f9149f666))

- **number**: Additional customisation on replace mode
  ([`cb9d792`](https://github.com/tobiashochguertel/InquirerPrompt/commit/cb9d792b30052075bb57e06b4549c8f3ab2e00f1))

- **number**: Decimal
  ([`9af2fef`](https://github.com/tobiashochguertel/InquirerPrompt/commit/9af2fef76b758ca352a3ba6b472df2e2dca03a73))

- **number**: Fix_sn
  ([`a54384f`](https://github.com/tobiashochguertel/InquirerPrompt/commit/a54384f011a2a1697e0173c3ea5d164124c35b8b))

- **number**: Handle input and answer
  ([`79ef0dd`](https://github.com/tobiashochguertel/InquirerPrompt/commit/79ef0dd0565f6523348908058900bde05a90ba06))

- **number**: Handle sn
  ([`93bae9f`](https://github.com/tobiashochguertel/InquirerPrompt/commit/93bae9fc20a31dac705b5591bc720282213d1b45))

- **number**: Handle sn on text change
  ([`b45ce2e`](https://github.com/tobiashochguertel/InquirerPrompt/commit/b45ce2e56794173fca2f6bff71c8592c7c53c32d))

- **number**: Handle text change
  ([`8146c67`](https://github.com/tobiashochguertel/InquirerPrompt/commit/8146c678b275293569fadf6c38fcbfe7fb41526e))

- **number**: Handle_dot
  ([`a27668f`](https://github.com/tobiashochguertel/InquirerPrompt/commit/a27668ffb9f76b4904b8f148a03900437780996d))

- **number**: Handle_left handle_down
  ([`7e40e8b`](https://github.com/tobiashochguertel/InquirerPrompt/commit/7e40e8b6168292598ffa4bee13923a187f73e1bd))

- **number**: Handle_number
  ([`2444881`](https://github.com/tobiashochguertel/InquirerPrompt/commit/24448810640172eb20dd3f6192228535f9f1fd32))

- **number**: Handle_right
  ([`19c7cb8`](https://github.com/tobiashochguertel/InquirerPrompt/commit/19c7cb8ba9148847578c7accdc3e2a58960a50d6))

- **number**: Init
  ([`2bd573a`](https://github.com/tobiashochguertel/InquirerPrompt/commit/2bd573ac9c14d4c8d827e138a8a9f1323f18ad1e))

- **number**: More coverage
  ([`a5fda50`](https://github.com/tobiashochguertel/InquirerPrompt/commit/a5fda504e4ba8d4efce9fdac5dba594eeeca19a2))

- **number**: Negative toggle
  ([`7fa9432`](https://github.com/tobiashochguertel/InquirerPrompt/commit/7fa94323f30188dc8e4fd99c5ff21f8cf6624341))

- **number**: No default
  ([`065ce68`](https://github.com/tobiashochguertel/InquirerPrompt/commit/065ce6870cbcd8d4c5c03de68511b8636f94aac5))

- **number**: Replace
  ([`8a80ffd`](https://github.com/tobiashochguertel/InquirerPrompt/commit/8a80ffd0b409d54547132ee53fb758f69d0d69be))

- **resolver**: Async
  ([`d43fdcb`](https://github.com/tobiashochguertel/InquirerPrompt/commit/d43fdcbd184c83229a1917c09c4c508cf4985ae6))

- **resolver**: Keybinding registration
  ([`3bc5e1b`](https://github.com/tobiashochguertel/InquirerPrompt/commit/3bc5e1b49dacfe9ac95cb77dcf4b10705eb3c0a9))

- **resolver**: Skip 3.7 for async for now
  ([`1c030f1`](https://github.com/tobiashochguertel/InquirerPrompt/commit/1c030f1a3b5915274ce9be5452c3699103841ca1))

- **spinner**: Added new test
  ([`9c97a97`](https://github.com/tobiashochguertel/InquirerPrompt/commit/9c97a970626b465cb96c70469f477cce23c5ead5))


## v0.2.4 (2021-08-12)

### Bug Fixes

- **fuzzy**: Choices are centered
  ([`4bfb410`](https://github.com/tobiashochguertel/InquirerPrompt/commit/4bfb4103d8988b8c396b860f1f52ba8eb2d745e2))

### Documentation

- Changelog update
  ([`24d341f`](https://github.com/tobiashochguertel/InquirerPrompt/commit/24d341f30d9cdfdf8dd08f17ec6a78581e3435b8))

- Update CHANGELOG
  ([`51efeba`](https://github.com/tobiashochguertel/InquirerPrompt/commit/51efeba281c58392e1ac2fe1c474793b51d6d05d))


## v0.2.3 (2021-08-04)

### Bug Fixes

- Answered question spacing should depends on amark
  ([`a684713`](https://github.com/tobiashochguertel/InquirerPrompt/commit/a684713553f28649eb9d7635c17439bbd0b6c723))

- Cursor offset
  ([`36177e4`](https://github.com/tobiashochguertel/InquirerPrompt/commit/36177e463d3f6c58d05e029c0a3819485a44642e))

- Spacing
  ([`b2f83fe`](https://github.com/tobiashochguertel/InquirerPrompt/commit/b2f83fe67dd55361816f41a5c6bd25876e145ecc))

- **base**: Height extension
  ([`d37fcf1`](https://github.com/tobiashochguertel/InquirerPrompt/commit/d37fcf1de6578a78446da80975236781e52e8251))

- **base**: Line wrapping # #11
  ([`9f040e4`](https://github.com/tobiashochguertel/InquirerPrompt/commit/9f040e41bbe9e3667df6b9f6a3dce85c3bb0cc21))

- **confirm**: Spacing after instruction
  ([`ae02b41`](https://github.com/tobiashochguertel/InquirerPrompt/commit/ae02b41a2ebe9e663eec32709c1e1f3a7fe5dfb5))

### Chores

- Poetry explicit packaging
  ([`aa19df7`](https://github.com/tobiashochguertel/InquirerPrompt/commit/aa19df7a429672baf3f3c07d7031bf9c0b91ec31))

- Update dependencies
  ([`be35afd`](https://github.com/tobiashochguertel/InquirerPrompt/commit/be35afd7b6920200c0dd4549dadbb9c3af0a13c8))

### Continuous Integration

- **codebuild**: Fix poetry
  ([`464fa81`](https://github.com/tobiashochguertel/InquirerPrompt/commit/464fa818f4d01825812863ff43bb6a2f812c2dd3))

### Documentation

- Changelog
  ([`778e163`](https://github.com/tobiashochguertel/InquirerPrompt/commit/778e163e1f7b1aa1680d7cd930f1a85c64eaf583))

- Changelog
  ([`1d1950c`](https://github.com/tobiashochguertel/InquirerPrompt/commit/1d1950c3fe2a504da2fc8a8de4d83fa5ce1c9b52))

- Changelog
  ([`766224c`](https://github.com/tobiashochguertel/InquirerPrompt/commit/766224c730966450afc6b87f3b0b66297cc651be))

### Features

- Calculate wrap lines offset if wrap_lines is configured #11
  ([`0700711`](https://github.com/tobiashochguertel/InquirerPrompt/commit/070071133c7c7ccdc53e616820ceb21a95502a2f))

- Enable instruction for non-list type prompts #7
  ([`3edfd4b`](https://github.com/tobiashochguertel/InquirerPrompt/commit/3edfd4bb180e6ac943e2ad20f45d540b7a036ebb))

- Support wrap lines configuration via argument #11
  ([`916b607`](https://github.com/tobiashochguertel/InquirerPrompt/commit/916b607814f3a95d515373311f78cc25ba70e292))

- Support wrap_lines arguments for list type prompts #11
  ([`8e4621a`](https://github.com/tobiashochguertel/InquirerPrompt/commit/8e4621a6dca1dbc8f03480d12c3718b7eec7ffed))

- **confirm**: Allow to customize confirm letter and reject letter #13
  ([`b3764af`](https://github.com/tobiashochguertel/InquirerPrompt/commit/b3764affb6f18bc019a5e69da85a30654ca67966))

### Refactoring

- Merge execute method
  ([`769a96e`](https://github.com/tobiashochguertel/InquirerPrompt/commit/769a96e1b210262ca0868f0eca0da239000a55b4))

- Separate base to a dedicated module
  ([`0d292af`](https://github.com/tobiashochguertel/InquirerPrompt/commit/0d292af0e6f15e733f8f8a8ab253e8caf1aed2d3))

### Testing

- Execute
  ([`64b7499`](https://github.com/tobiashochguertel/InquirerPrompt/commit/64b749948e2d781958c6b8092791257e298437c4))

- Test instruction for non list type prompt
  ([`6ef321a`](https://github.com/tobiashochguertel/InquirerPrompt/commit/6ef321a09cf6d6b55b2ff944befc36482eed8f2f))

- Update test spacing
  ([`d62e201`](https://github.com/tobiashochguertel/InquirerPrompt/commit/d62e2015488f127f2d3b20cde561601a2f329a8d))

- Wrap lines configuration via arguments
  ([`3c9f924`](https://github.com/tobiashochguertel/InquirerPrompt/commit/3c9f924423b10dfe6d25227a065cc1d318d95da5))

- Wrap_lines_offset
  ([`85b5aad`](https://github.com/tobiashochguertel/InquirerPrompt/commit/85b5aad9c54b7ccd9af290b5a85168ed000d9906))

- **confirm**: Custom confirm/reject letter
  ([`578ef68`](https://github.com/tobiashochguertel/InquirerPrompt/commit/578ef68a1c44d44c1904a9a3bd770f15b9b2e4d2))

- **fuzzy**: Fix inconsistent result due to height
  ([`d4f485e`](https://github.com/tobiashochguertel/InquirerPrompt/commit/d4f485e85cda0f549f371abced6dcf97e3d2ecd3))

- **fuzzy**: Wrap_lines_offset
  ([`facdfe5`](https://github.com/tobiashochguertel/InquirerPrompt/commit/facdfe50c7c48da0e4e92c7ce33a33b6e31f46db))

- **list**: Wrap_lines_offset
  ([`a073c1f`](https://github.com/tobiashochguertel/InquirerPrompt/commit/a073c1f7e41d3677c8404673706e224125bec829))


## v0.2.2 (2021-07-03)

### Chores

- Migrate to poetry
  ([`315878d`](https://github.com/tobiashochguertel/InquirerPrompt/commit/315878d4ff1c2b617e3f9fd53056b977bd41856f))

### Continuous Integration

- **codebuild**: Use poetry
  ([`3d45493`](https://github.com/tobiashochguertel/InquirerPrompt/commit/3d4549390dc04587870db76d0b43cca5670f00ee))

### Documentation

- **changelog**: Fix heading
  ([`8904881`](https://github.com/tobiashochguertel/InquirerPrompt/commit/89048810454a311dad52024bf8c2754c5ee3390b))


## v0.2.1 (2021-07-03)

### Bug Fixes

- **example**: Pizza example fix. Closes #5
  ([`5a369d6`](https://github.com/tobiashochguertel/InquirerPrompt/commit/5a369d6d6fc31b6d4cde1c16bc4370132c6bec6d))

### Chores

- **pre-commit**: Update pre-commit hooks version
  ([`8b2f0e2`](https://github.com/tobiashochguertel/InquirerPrompt/commit/8b2f0e2d31b87c5da092eca309aa5fd4825e0d4a))

### Documentation

- Update inline LICENSE for fzy logic
  ([`0a0d792`](https://github.com/tobiashochguertel/InquirerPrompt/commit/0a0d7923fe60eb2fed99d2637154c59ead4edf4a))

- **base**: Update docstring
  ([`b2513d6`](https://github.com/tobiashochguertel/InquirerPrompt/commit/b2513d6b13f644d81dcf5e7d6effeb4f0ff7042e))

- **changelog**: 0.2.1 changes
  ([`e6c9f72`](https://github.com/tobiashochguertel/InquirerPrompt/commit/e6c9f72a8c895d63ac16d8dd3bf0739d24119bed))

- **changelog**: Typo
  ([`cff560f`](https://github.com/tobiashochguertel/InquirerPrompt/commit/cff560fe5e7b13eb903341d8e2c1ea4d025304b3))

### Features

- Added parameter to disable the cycle behavior
  ([`00b2fa0`](https://github.com/tobiashochguertel/InquirerPrompt/commit/00b2fa0efae9689474121702fbe04a58e547f3eb))

- Allow disable cycle in list type prompts #9
  ([`5f1a610`](https://github.com/tobiashochguertel/InquirerPrompt/commit/5f1a610dad94ac2760d5075992f043f4226993e3))

- Configure amark and style for answered questions
  ([`f7fee40`](https://github.com/tobiashochguertel/InquirerPrompt/commit/f7fee40f099e91f06ddfc2baea919e8ce53c1f30))

- **checkbox**: Customize amark
  ([`d6136b1`](https://github.com/tobiashochguertel/InquirerPrompt/commit/d6136b1edfab1aa3b1519a4d8512232e532c50e4))

- **confirm**: Custom style for answered questions
  ([`d02e413`](https://github.com/tobiashochguertel/InquirerPrompt/commit/d02e413dcd2d234ec67cf4f0f90044392b196349))

- **expand**: Customize style for answered question
  ([`b2d7b52`](https://github.com/tobiashochguertel/InquirerPrompt/commit/b2d7b52733444ebdaf4d4554abb4e5f294f663af))

- **filepath**: Customize answered question style
  ([`9b78eaa`](https://github.com/tobiashochguertel/InquirerPrompt/commit/9b78eaab4856f2a42c7fd5608122f0b47aff1ce4))

- **fuzzy**: Customize answered question style
  ([`2058cfc`](https://github.com/tobiashochguertel/InquirerPrompt/commit/2058cfc160e4de545c3e58397721caea092b9cbe))

- **input**: Customize answered question style
  ([`25105b0`](https://github.com/tobiashochguertel/InquirerPrompt/commit/25105b06c2cc0ee42826d01ffa7c8531c4dbcca7))

- **list**: Customize answered question style
  ([`50d38a4`](https://github.com/tobiashochguertel/InquirerPrompt/commit/50d38a496fff0613e922d98ec4a78b4b442ee4e6))

- **rawlist**: Customize answered questions style
  ([`30ad09e`](https://github.com/tobiashochguertel/InquirerPrompt/commit/30ad09eab18e0d5f4235743b938f88b3df0f276d))

- **test**: Customize answered question style
  ([`40dbc2e`](https://github.com/tobiashochguertel/InquirerPrompt/commit/40dbc2eb6d6c8f6d33de997fd65ab9c5e2368201))

### Testing

- **confirm**: Update test
  ([`b452df6`](https://github.com/tobiashochguertel/InquirerPrompt/commit/b452df61ad9673607ff59076f7357d6a27a10fbf))

- **expand**: Disable cycle
  ([`e8dc09a`](https://github.com/tobiashochguertel/InquirerPrompt/commit/e8dc09a06d69e9461832455482b28da68f798d1e))

- **expand**: Update
  ([`d6f2c4f`](https://github.com/tobiashochguertel/InquirerPrompt/commit/d6f2c4f34a72272f1c84e43c37e6de506312d079))

- **filepath**: Update test
  ([`9b2be59`](https://github.com/tobiashochguertel/InquirerPrompt/commit/9b2be594f362b0e69f664ef16f1579930d63fd54))

- **fuzzy**: Update test
  ([`5e9a2e6`](https://github.com/tobiashochguertel/InquirerPrompt/commit/5e9a2e65bc033348c7d8d10abed175e1a7c9644a))

- **input**: Update test
  ([`c63ff17`](https://github.com/tobiashochguertel/InquirerPrompt/commit/c63ff17df2b2cbde3aa64809037a1dfb44e4a596))

- **list**: Disable cycle
  ([`1b1598f`](https://github.com/tobiashochguertel/InquirerPrompt/commit/1b1598f958fc4613709ed53c8947c097edf97497))

- **list**: Update test
  ([`da0f05d`](https://github.com/tobiashochguertel/InquirerPrompt/commit/da0f05db4ca92ac2ccd3dd36e47e3e9c02fa8dab))

- **rawlist**: Update test
  ([`802bc69`](https://github.com/tobiashochguertel/InquirerPrompt/commit/802bc69b577046af2be3f60ef59262a40a0c5b04))

- **resolver**: Update
  ([`984c549`](https://github.com/tobiashochguertel/InquirerPrompt/commit/984c5492de7dac06360f14cfc3fed31269bcea50))

- **secret**: Update
  ([`f8de346`](https://github.com/tobiashochguertel/InquirerPrompt/commit/f8de3469a2b225c41fa48c5ac5c5240c22e3978c))

- **utils**: Update test
  ([`be9b4f8`](https://github.com/tobiashochguertel/InquirerPrompt/commit/be9b4f8e6205acab9789cd83f5978c656fb4039c))


## v0.2.0 (2021-05-01)

### Bug Fixes

- **base**: Change the behaviour to handle empty qmark string
  ([`10fe4b4`](https://github.com/tobiashochguertel/InquirerPrompt/commit/10fe4b4f6a984f30e12cee1d2223278b5d958e5b))

Co-authored-by: Kevin Zhuang <kevin7441@gmail.com>

- **base**: Remove question var
  ([`bb94a1d`](https://github.com/tobiashochguertel/InquirerPrompt/commit/bb94a1d7128dc5c09df586526da36085f2c3f2e9))

### Documentation

- **changelog**: Update changelog for 0.2.0
  ([`8daddba`](https://github.com/tobiashochguertel/InquirerPrompt/commit/8daddba4fb5bc223d627bed8826e55b6b105b842))

### Features

- Added multiselect attr to InquirerPyUIControl class
  ([`8cdc12f`](https://github.com/tobiashochguertel/InquirerPrompt/commit/8cdc12fcae350e3c5b4bfbcbe0906fa4b091eea7))

- Allow default enable for lists #2
  ([`7165b70`](https://github.com/tobiashochguertel/InquirerPrompt/commit/7165b70f4a2948eab6cbe31a9c485cfccd43b43c))

- Configure marker placeholder
  ([`6ea85d5`](https://github.com/tobiashochguertel/InquirerPrompt/commit/6ea85d56c16343b28cb559779e7ca0e303aa13f1))

- **base**: Optional qmark
  ([`725af41`](https://github.com/tobiashochguertel/InquirerPrompt/commit/725af41b10eb7cf2f7c247a46ad3b4665d2d48f8))

### Performance Improvements

- Add __all__ to prompts
  ([`2d5ce80`](https://github.com/tobiashochguertel/InquirerPrompt/commit/2d5ce807b86a49ec9454698ecc6493e58575f0a6))

### Refactoring

- **base**: Move empty qmark check to message line for test to pass
  ([`6bb4687`](https://github.com/tobiashochguertel/InquirerPrompt/commit/6bb4687d3b7e4c7bce433596efb978bf91bff82b))

### Testing

- List value default enabled
  ([`02d0453`](https://github.com/tobiashochguertel/InquirerPrompt/commit/02d04535c992c07a2efd4eef015d304553820efe))

- Update rawlist and expand test for space changes
  ([`236abc1`](https://github.com/tobiashochguertel/InquirerPrompt/commit/236abc17e802c0c43a9e02bbd540a0e21f8c3266))

- Update test to cover multiselect attr for InquirerPyUIControl
  ([`c633750`](https://github.com/tobiashochguertel/InquirerPrompt/commit/c633750235e6909ad2a2c1a26cf7df2b60211487))

- **checkbox**: Fix arg
  ([`09b109c`](https://github.com/tobiashochguertel/InquirerPrompt/commit/09b109c508e966190bbb2be9229561b67d72ea92))


## v0.1.1 (2021-04-03)

### Bug Fixes

- Pyright lint
  ([`0e79b10`](https://github.com/tobiashochguertel/InquirerPrompt/commit/0e79b102c78fe4b79eeeb408db13438402b3c5f2))

- **fuzzy**: Application redraw after filter
  ([`fd2eb69`](https://github.com/tobiashochguertel/InquirerPrompt/commit/fd2eb6909ac846838bb33c29a1048d9d6897c870))

- **fuzzy**: Height calculation
  ([`6851ff1`](https://github.com/tobiashochguertel/InquirerPrompt/commit/6851ff1975c0d9f595cd0998e9e9a3e1c34d4e69))

### Chores

- Tooling and dependency
  ([`4475a99`](https://github.com/tobiashochguertel/InquirerPrompt/commit/4475a9976dd9d97ce6f1990167823bf27a6f9b9b))

### Continuous Integration

- **github**: Coverage
  ([`3683df6`](https://github.com/tobiashochguertel/InquirerPrompt/commit/3683df6d56c41306b897c5578400ed531da2e40e))

### Documentation

- Update fuzzy doc string
  ([`01b899f`](https://github.com/tobiashochguertel/InquirerPrompt/commit/01b899f2cbe1c8e8d9e514fd34f69fe7853545a0))

- **readme**: Coverage
  ([`a890964`](https://github.com/tobiashochguertel/InquirerPrompt/commit/a890964f10ebb68186870b3c02bcdbd27d11f47c))

- **readme**: Typo
  ([`8f66d6e`](https://github.com/tobiashochguertel/InquirerPrompt/commit/8f66d6efe5817a646e8a5df8023b8fff7e182302))

- **readme**: Update differences with PyInquirer
  ([`d7b192d`](https://github.com/tobiashochguertel/InquirerPrompt/commit/d7b192df1d991582f5be5c44e52b8dfc09aebe2c))

### Testing

- **fuzzy**: Update height test
  ([`df838e0`](https://github.com/tobiashochguertel/InquirerPrompt/commit/df838e0e1c7232caf0240a8da5ac5cde9bf5ba15))


## v0.1.0 (2021-01-17)

### Bug Fixes

- Apply choices based kb in the after_render call
  ([`d501b1f`](https://github.com/tobiashochguertel/InquirerPrompt/commit/d501b1f8e17babe457b292db8d61f4b90ba75e90))

- Class abstraction missing base ABC
  ([`8853380`](https://github.com/tobiashochguertel/InquirerPrompt/commit/885338095fa624899242f458c3b2f2694cc97495))

- Don't merge style by default
  ([`be351a5`](https://github.com/tobiashochguertel/InquirerPrompt/commit/be351a57984c76c1aa6eb6e74947dff3d6ad3134))

- Editing_mode should be param at prompt level not question level
  ([`06a382f`](https://github.com/tobiashochguertel/InquirerPrompt/commit/06a382fe56978f31068480b7a654bde169262a18))

- Height calculation
  ([`fca11e1`](https://github.com/tobiashochguertel/InquirerPrompt/commit/fca11e175ccdf816eb8ca53ab60674e57e9edfa3))

- Height offset
  ([`c12544a`](https://github.com/tobiashochguertel/InquirerPrompt/commit/c12544a3cc10817c5fe465a8f279881b97817795))

- Immutable param
  ([`0bc4dc7`](https://github.com/tobiashochguertel/InquirerPrompt/commit/0bc4dc768e4857bf73e701a1d9c70c21cd209160))

- Multi default value resolution is messed up by Separator
  ([`1ef3b37`](https://github.com/tobiashochguertel/InquirerPrompt/commit/1ef3b37b340430a422826f9749a40e18953814a5))

- Remove Literal typing to support 3.7
  ([`0a6b2f1`](https://github.com/tobiashochguertel/InquirerPrompt/commit/0a6b2f1f277d775f899dccdff7746a2e4af342e0))

- Sessionresult typing
  ([`aed5604`](https://github.com/tobiashochguertel/InquirerPrompt/commit/aed56049cde1012445ce20776ff92b37c5e76f39))

- Type hinting
  ([`5f8dc25`](https://github.com/tobiashochguertel/InquirerPrompt/commit/5f8dc2536c772da66dd695094c232e8ad85f103a))

- Typing and unnamed question
  ([`a7835f9`](https://github.com/tobiashochguertel/InquirerPrompt/commit/a7835f926786c0f3e2fa9ce5b549e4f08098aedf))

- Typing for keybindings
  ([`b762c3d`](https://github.com/tobiashochguertel/InquirerPrompt/commit/b762c3d677bce68783dc4e9d7c485eff212b3595))

- Typing of transformer and filter
  ([`063b70c`](https://github.com/tobiashochguertel/InquirerPrompt/commit/063b70c9dd345fe033a7ee02c0e6d9ca0f46d2d6))

- Typo
  ([`37f6b56`](https://github.com/tobiashochguertel/InquirerPrompt/commit/37f6b5667602055fd31b51972d0cb9601b7cbfc8))

- Update tests params
  ([`452b42a`](https://github.com/tobiashochguertel/InquirerPrompt/commit/452b42a6828362c2242e14d15a18f11f8a6b305c))

- Update validate type hinting
  ([`280c683`](https://github.com/tobiashochguertel/InquirerPrompt/commit/280c68305a0b87b170a74e1f07ffde690a6d820b))

- Validation toolbar position
  ([`324d80e`](https://github.com/tobiashochguertel/InquirerPrompt/commit/324d80e26c1d2a527c6dfaef3ba664c81afa2287))

- **base**: Fix value cannot be other type other then str
  ([`0a6baf3`](https://github.com/tobiashochguertel/InquirerPrompt/commit/0a6baf32f29ec6d84d61307dc7ce7296421d218a))

- **base**: List prompts validation toolbar position fix
  ([`ddc8247`](https://github.com/tobiashochguertel/InquirerPrompt/commit/ddc82477f4260fc3f7526a456b03a4edc2461287))

- **base**: Transformer wrong param
  ([`ebe0c52`](https://github.com/tobiashochguertel/InquirerPrompt/commit/ebe0c5299b3d856be90f2cbed95f94cfae5e1328))

- **checkbox**: Handle enter was not overrided
  ([`27ecf9d`](https://github.com/tobiashochguertel/InquirerPrompt/commit/27ecf9da835f8943629407b36ad96285bf5b7bfc))

- **confirm**: Kbi raise
  ([`5765286`](https://github.com/tobiashochguertel/InquirerPrompt/commit/57652866811317ee3d512b670496eee7a780685c))

- **expand**: Clear keys on re-render
  ([`c040fdd`](https://github.com/tobiashochguertel/InquirerPrompt/commit/c040fddce21feffcce22f72163eb078a65ea9bcf))

- **expand**: Default param should be key
  ([`5a8da18`](https://github.com/tobiashochguertel/InquirerPrompt/commit/5a8da18d126ae8b1a0fba6eb900ccc0c02c5e788))

- **expand**: Override toggle all to handle ExpandHelp
  ([`3a58590`](https://github.com/tobiashochguertel/InquirerPrompt/commit/3a58590ba09f0ef460afea9c29920937b23d30a9))

- **filepath**: Incosistent completion when starts with "./"
  ([`6c8214f`](https://github.com/tobiashochguertel/InquirerPrompt/commit/6c8214f987f63175805c8db0161c58da94df2d36))

- **fuzzy**: Cursor lost after transition of empty choice
  ([`e43516a`](https://github.com/tobiashochguertel/InquirerPrompt/commit/e43516ab9740b6c441e712d335ff917fcc4dc01b))

- **fuzzy**: Don't force async in normal application
  ([`0ea8be1`](https://github.com/tobiashochguertel/InquirerPrompt/commit/0ea8be12b152615b697e82a11c261f5dba847d6c))

- **fuzzy**: Frame color
  ([`ed7527a`](https://github.com/tobiashochguertel/InquirerPrompt/commit/ed7527a18cecb01ebf905e8725b0ba7073b33bf6))

- **fuzzy**: Inconsistent height
  ([`197daed`](https://github.com/tobiashochguertel/InquirerPrompt/commit/197daed02473e737310969490d8745313c35fc62))

- **fuzzy**: Index error for UIControl
  ([`1471c5e`](https://github.com/tobiashochguertel/InquirerPrompt/commit/1471c5ef2f8cef4a350d60bbf417be6e6ee93786))

- **fuzzy**: Index issue when running fitering
  ([`7b3588b`](https://github.com/tobiashochguertel/InquirerPrompt/commit/7b3588b386b2cf7d6e0213dd412c0675a9c7baa2))

- **fuzzy**: Marker style
  ([`7e6d2ae`](https://github.com/tobiashochguertel/InquirerPrompt/commit/7e6d2ae33e6201d66e0537e88b523a4dbad1e935))

- **fuzzy**: Prompt highlight
  ([`eb77343`](https://github.com/tobiashochguertel/InquirerPrompt/commit/eb7734394dac29a6c69a7f7d54b68e43c43ae3c7))

- **fuzzy**: Pyright fail
  ([`6a8b7f4`](https://github.com/tobiashochguertel/InquirerPrompt/commit/6a8b7f464e3b1ba5776c9f190ed346f89c004b96))

- **fuzzy**: Style issues, conditional wrapper not expected and index
  ([`a6c1b38`](https://github.com/tobiashochguertel/InquirerPrompt/commit/a6c1b38b21df01ec97130cb6d9cc92310c048dfc))

- **fuzzy**: Typo
  ([`00d69db`](https://github.com/tobiashochguertel/InquirerPrompt/commit/00d69db42f2e22276f54007457d19fdcdbb692fe))

- **fuzzy**: Validation exception when no filtered choices
  ([`6be7caf`](https://github.com/tobiashochguertel/InquirerPrompt/commit/6be7caf2c0ba7f69136c74ce1f24e889f6b31d3f))

- **list**: Default should not be required
  ([`185e23c`](https://github.com/tobiashochguertel/InquirerPrompt/commit/185e23c54ba4bf5d9ce146f3b5bd481f679d2b29))

- **list**: Remove unnecessary calls
  ([`41db089`](https://github.com/tobiashochguertel/InquirerPrompt/commit/41db089d8b7a06b7fdd6eff03ab92710b1a55f2c))

- **rawlist**: Limit choices to 9
  ([`ffe2fce`](https://github.com/tobiashochguertel/InquirerPrompt/commit/ffe2fcefa19edc2572a06bdbee75354b68c9f482))

- **rawlist**: Properly handle separator when applying keybindings
  ([`4e6fd83`](https://github.com/tobiashochguertel/InquirerPrompt/commit/4e6fd837638a3ffa4cfdac6c774d7f68a97ef6b3))

- **rawlist**: Spacing
  ([`bde8d40`](https://github.com/tobiashochguertel/InquirerPrompt/commit/bde8d40e3087c3e98661a99713c15fdb9df53c16))

- **resolver**: Don't alter original question dict
  ([`7a2574b`](https://github.com/tobiashochguertel/InquirerPrompt/commit/7a2574b0d6b2ef5e154e331102d1373028c12016))

- **resolver**: Properly parse env variable
  ([`6f9bbb7`](https://github.com/tobiashochguertel/InquirerPrompt/commit/6f9bbb73a75c103576d94fc4df2fda7c94fee0ef))

- **resolver**: When condition
  ([`b575ec6`](https://github.com/tobiashochguertel/InquirerPrompt/commit/b575ec69e557ae18632cb41efa277f6c1669f4b9))

- **secret**: Prompt token missing space
  ([`5a0d5c7`](https://github.com/tobiashochguertel/InquirerPrompt/commit/5a0d5c70db449b6eb4b92b979fab6eaf66a8324f))

- **secret**: Transformer not transforming value
  ([`ccd51ce`](https://github.com/tobiashochguertel/InquirerPrompt/commit/ccd51ce5a40e980f868ab87c78be570bbc92e00c))

- **secret**: Wrong default param value
  ([`ef769a2`](https://github.com/tobiashochguertel/InquirerPrompt/commit/ef769a2dd198fb77c1e895214b932167084b9894))

- **utils**: Height calculation avoid extra small size
  ([`5ac1863`](https://github.com/tobiashochguertel/InquirerPrompt/commit/5ac18632d08ab8f0c3a910bac8d286c8fb61303b))

- **validator**: Unused typing
  ([`ac9c598`](https://github.com/tobiashochguertel/InquirerPrompt/commit/ac9c598482534d49dbabef28dbaaea24829ec205))

### Chores

- Added coverage config
  ([`3f48617`](https://github.com/tobiashochguertel/InquirerPrompt/commit/3f486173bd76d4cec2416878c32d72cecf480100))

- Added isort spec
  ([`8f602a9`](https://github.com/tobiashochguertel/InquirerPrompt/commit/8f602a94dd4b8bb95598c5fe1b72b89efd813042))

- Added pre-commit
  ([`3111819`](https://github.com/tobiashochguertel/InquirerPrompt/commit/311181998eff057da6a640e61d5d462b8f7c282d))

- Ignore fzy in coverage
  ([`1ef22bc`](https://github.com/tobiashochguertel/InquirerPrompt/commit/1ef22bc75a9d3573e9e557630bb444602f7261b7))

- License
  ([`e82bf6c`](https://github.com/tobiashochguertel/InquirerPrompt/commit/e82bf6c253ef77d8c4843758aa7be7644ae7d2f7))

- Update requirements-dev.txt
  ([`7ba1bd6`](https://github.com/tobiashochguertel/InquirerPrompt/commit/7ba1bd68940b55121f76b860c64392ac0c9af6ac))

- Update requirements.txt
  ([`ef30a84`](https://github.com/tobiashochguertel/InquirerPrompt/commit/ef30a84ab4fc5ce70de24ea832cd58b766eb863e))

- Update requirements.txt
  ([`d71a1ea`](https://github.com/tobiashochguertel/InquirerPrompt/commit/d71a1eaf204ab830a21a334b983a02292a12559c))

- **example**: Added example for checkbox
  ([`959ce84`](https://github.com/tobiashochguertel/InquirerPrompt/commit/959ce84d1dac544ee89844592a6f80f5977f2004))

- **example**: Added example for expand
  ([`55daa49`](https://github.com/tobiashochguertel/InquirerPrompt/commit/55daa4947447ad93b0356843c2421522cd23d840))

- **example**: Added fuzzy example
  ([`3c8355a`](https://github.com/tobiashochguertel/InquirerPrompt/commit/3c8355a746068783956772cc1fbc23da64487312))

- **example**: Added more example
  ([`78d88d4`](https://github.com/tobiashochguertel/InquirerPrompt/commit/78d88d4ac1af45a77af83908e3a9c487fd2d1608))

- **example**: Added new example
  ([`c7e519c`](https://github.com/tobiashochguertel/InquirerPrompt/commit/c7e519c24074c6b897169efb140d93a7326d9fe2))

- **example**: Added rawlist example
  ([`ad0e614`](https://github.com/tobiashochguertel/InquirerPrompt/commit/ad0e6147aff40da9cd136cb17ead6581eda2521c))

- **example**: Enhance the case
  ([`89c61c8`](https://github.com/tobiashochguertel/InquirerPrompt/commit/89c61c8168ffd36726a560019fed71e5ed8dc4ac))

- **example**: Secret example update
  ([`6bcfa79`](https://github.com/tobiashochguertel/InquirerPrompt/commit/6bcfa797e8cb18bee558059cda4d0a543a4dfe77))

- **example**: Update checkbox example
  ([`9109f96`](https://github.com/tobiashochguertel/InquirerPrompt/commit/9109f96bfeccebc6c7f6fe7b10d0fdae88b2c89f))

- **example**: Update classic demo
  ([`75f3dd1`](https://github.com/tobiashochguertel/InquirerPrompt/commit/75f3dd15c2f5c413f5b61f12a32eddecf822d984))

- **example**: Update confirm example
  ([`845bac7`](https://github.com/tobiashochguertel/InquirerPrompt/commit/845bac731a78258b6befe50c7a1a3ae656b87331))

- **example**: Update examples
  ([`97c2ebc`](https://github.com/tobiashochguertel/InquirerPrompt/commit/97c2ebc2f9e67ff9098f6c68383c9fd95ad2251c))

- **example**: Update expand example
  ([`402579f`](https://github.com/tobiashochguertel/InquirerPrompt/commit/402579f3ac7fc0d7a140e37028d90e533ae3b944))

- **example**: Update filepath example
  ([`5fd6286`](https://github.com/tobiashochguertel/InquirerPrompt/commit/5fd62860f823533cdcc267c72fc76d84f6332d1c))

- **example**: Update fuzzy example
  ([`ee9f40a`](https://github.com/tobiashochguertel/InquirerPrompt/commit/ee9f40ababd44f25b17b3e9388c1657c4624362e))

- **example**: Update input example
  ([`8827ac0`](https://github.com/tobiashochguertel/InquirerPrompt/commit/8827ac003ac4eef611fec3350bc3cb79ae09e82a))

- **example**: Update list example
  ([`1cd4967`](https://github.com/tobiashochguertel/InquirerPrompt/commit/1cd49670ca9c91988eef0f0c9833cceda90823ac))

- **example**: Update rawlist example
  ([`4e0949b`](https://github.com/tobiashochguertel/InquirerPrompt/commit/4e0949b3d0ec170766dadf6a2d642d561e181ed4))

- **example**: Update sample code
  ([`aabda58`](https://github.com/tobiashochguertel/InquirerPrompt/commit/aabda58a5fe859b5cfce9d508358c6d670400b0f))

- **example**: Update sample file link
  ([`fd3e84c`](https://github.com/tobiashochguertel/InquirerPrompt/commit/fd3e84cf39eb466835bceade6880cc13ef2dadc1))

- **example**: Update sample file url
  ([`f57ae38`](https://github.com/tobiashochguertel/InquirerPrompt/commit/f57ae38a16c73564e7ce2fd13d3d26259ed2d0b5))

- **examples**: Fix example param
  ([`20e890a`](https://github.com/tobiashochguertel/InquirerPrompt/commit/20e890a9961755fd4da28dde7a4a4f2c588eabca))

- **examples**: Update list and fuzzy example
  ([`6bfa86a`](https://github.com/tobiashochguertel/InquirerPrompt/commit/6bfa86a2d82e0777db8b86bb68cb65dc08efde7c))

### Code Style

- Code style fix
  ([`473aae9`](https://github.com/tobiashochguertel/InquirerPrompt/commit/473aae9186e2e2c17f9c789c31ee5ad950b9327e))

- Isort
  ([`7605443`](https://github.com/tobiashochguertel/InquirerPrompt/commit/7605443b9365b79c0f16edebbadaff40dcb6895f))

### Continuous Integration

- **codebuild**: Config
  ([`89a9e6c`](https://github.com/tobiashochguertel/InquirerPrompt/commit/89a9e6c096832c6cb6d783037ba9127855a66f86))

- **github**: Added lint pipeline
  ([`eac1820`](https://github.com/tobiashochguertel/InquirerPrompt/commit/eac18207bf12f6d4a21b624f4d0e12adc5536146))

- **github**: Remove 3.6
  ([`ab97c9a`](https://github.com/tobiashochguertel/InquirerPrompt/commit/ab97c9a52e82fc79a30ed2f2f6929e8e3e2661bd))

- **github**: Unittest
  ([`be253aa`](https://github.com/tobiashochguertel/InquirerPrompt/commit/be253aafc7191ae7050d08db802b0ffa6798e9ba))

### Documentation

- Added docstring to use files
  ([`ef9dc8f`](https://github.com/tobiashochguertel/InquirerPrompt/commit/ef9dc8fa31cd49931dd305e8c5e1f16bef727e50))

- Fix demo code
  ([`c207eea`](https://github.com/tobiashochguertel/InquirerPrompt/commit/c207eea16e800b382ec4465343a9e5ea4e129a46))

- Update
  ([`280c59d`](https://github.com/tobiashochguertel/InquirerPrompt/commit/280c59dae1ffe2d312681878b8c8eeddcf0f3833))

- Update example
  ([`83988b5`](https://github.com/tobiashochguertel/InquirerPrompt/commit/83988b5e0ce619cca31421722c80808cda60e70b))

- Update param default type hinting
  ([`fbb61fb`](https://github.com/tobiashochguertel/InquirerPrompt/commit/fbb61fb905468b1b468d9d48b0ebcdd29660e6d7))

- Update some doc string for validator and resolver
  ([`24c042a`](https://github.com/tobiashochguertel/InquirerPrompt/commit/24c042a7f5e4bfce8e0b3e0db20a0ceec0c8dd6d))

- **base**: Document inheritance
  ([`0bad563`](https://github.com/tobiashochguertel/InquirerPrompt/commit/0bad563d4d9a464b0099353f22bfdd25d6a3f8f7))

- **base**: Update doc string
  ([`14a596c`](https://github.com/tobiashochguertel/InquirerPrompt/commit/14a596c8cf52b248b16b0644fde3eaeb3dfa89e8))

- **fuzzy**: Override kb
  ([`7817445`](https://github.com/tobiashochguertel/InquirerPrompt/commit/7817445e8abfff8c51cb0b50b1f995e42b5cade6))

- **readme**: Added links to wiki
  ([`a7ef9aa`](https://github.com/tobiashochguertel/InquirerPrompt/commit/a7ef9aab05d3f94e582c594285eaca0b009de766))

- **readme**: Added requirements
  ([`cdd43f2`](https://github.com/tobiashochguertel/InquirerPrompt/commit/cdd43f277dc0001cd843f773d02f6ed0a2fc2a17))

- **readme**: Badge
  ([`d7aca63`](https://github.com/tobiashochguertel/InquirerPrompt/commit/d7aca63103c2f0b4acabbb6e5632082beb2e2fb9))

- **readme**: Fix example
  ([`d23800c`](https://github.com/tobiashochguertel/InquirerPrompt/commit/d23800c61af54b7ffd99323654fa68d5cf87d67e))

- **readme**: Init
  ([`c5a8cad`](https://github.com/tobiashochguertel/InquirerPrompt/commit/c5a8cade4db57f396ed58b76cd5add6a18c55029))

- **readme**: Update
  ([`86c2b22`](https://github.com/tobiashochguertel/InquirerPrompt/commit/86c2b22c88fe7196682aca8c0c2f98cc57a454be))

- **readme**: Update example code snippet
  ([`151dabe`](https://github.com/tobiashochguertel/InquirerPrompt/commit/151dabe4777252f78fa3eb4add03efa0ca157287))

- **secret**: Document class
  ([`d3cecba`](https://github.com/tobiashochguertel/InquirerPrompt/commit/d3cecbac7efeab28765abfb99dcdd6a3f52dac19))

### Features

- Add customization option for validation toolbar
  ([`86867eb`](https://github.com/tobiashochguertel/InquirerPrompt/commit/86867eb9d990bfb0e3486f7baded0edc0e304332))

- Added another entrypoint to create prompts
  ([`0782124`](https://github.com/tobiashochguertel/InquirerPrompt/commit/0782124aaf6143f2f916128de8dd8b2137f2d509))

- Added base class for simple prompts
  ([`0e07ff2`](https://github.com/tobiashochguertel/InquirerPrompt/commit/0e07ff22d9854f1e85c15c30c1b952250de46f15))

- Added more style options
  ([`7fcea53`](https://github.com/tobiashochguertel/InquirerPrompt/commit/7fcea53c4dd7c505d6aeb2dad097858bdbbd8bab))

- Added multiline option for input prompt
  ([`b564342`](https://github.com/tobiashochguertel/InquirerPrompt/commit/b564342b57a5e046b12a4014558ac4d7c11e1ba5))

- Added offset to height calculation
  ([`4d5b67a`](https://github.com/tobiashochguertel/InquirerPrompt/commit/4d5b67aedae6429235a0db48e187667ea4d78ded))

- Added separator style class
  ([`fd0bd7a`](https://github.com/tobiashochguertel/InquirerPrompt/commit/fd0bd7ac0f5726bef491e0cdd318dcfdbcf58223))

- Added transformer
  ([`2d718a7`](https://github.com/tobiashochguertel/InquirerPrompt/commit/2d718a7cd52c8a35e75cc14e9e6313fda624059b))

- Added validate for ComplexPrompt
  ([`54b17c8`](https://github.com/tobiashochguertel/InquirerPrompt/commit/54b17c84bfb5852fbac091fbf4272f2be3e50f10))

- Adding height configuration for all complex prompts
  ([`8af03c2`](https://github.com/tobiashochguertel/InquirerPrompt/commit/8af03c2ca47afc47fe70e0f348c1b35932c3fb11))

- After_render retrieve callable choices
  ([`b46057c`](https://github.com/tobiashochguertel/InquirerPrompt/commit/b46057ce0faef7631589e1ad0729f4cc0615902f))

- Allow both behavior of setting default value for rawlist and
  ([`ef3c3b1`](https://github.com/tobiashochguertel/InquirerPrompt/commit/ef3c3b1f9d4e4c0576bc7d094d6df4e5d2e27c9d))

- Allow choices to be callable
  ([`8676c9c`](https://github.com/tobiashochguertel/InquirerPrompt/commit/8676c9cc3d1f423940245c50287fae80b622a43e))

- Customize keybindings
  ([`7767a05`](https://github.com/tobiashochguertel/InquirerPrompt/commit/7767a051698b85b4e5e96b9c339ca8bcf1da0406))

- Display validation toolbar in a float container
  ([`128e043`](https://github.com/tobiashochguertel/InquirerPrompt/commit/128e04373f33cc6fa29cbeb41cb4baffe15a51ea))

- Env configure raise kbi
  ([`c9175dc`](https://github.com/tobiashochguertel/InquirerPrompt/commit/c9175dcbf7f83321526b8b7dd1a31de58495a12b))

- Message callable
  ([`8df98cb`](https://github.com/tobiashochguertel/InquirerPrompt/commit/8df98cb49fa60215cc69da09a0c6659f11c83935))

- Multicolumn_complete
  ([`a628bb2`](https://github.com/tobiashochguertel/InquirerPrompt/commit/a628bb24a57a185f96c14b160233223619fd8fb3))

- Optional hide cursor
  ([`72f5c88`](https://github.com/tobiashochguertel/InquirerPrompt/commit/72f5c88986f3feda12a19406dcc6f2cab6527cb1))

- Optional keyboard interrupt
  ([`16521e4`](https://github.com/tobiashochguertel/InquirerPrompt/commit/16521e4551e65e75f67ff584e3673d39338975f7))

- Update default value behavior and lexers
  ([`37189e5`](https://github.com/tobiashochguertel/InquirerPrompt/commit/37189e500a959247863ad130588a68095e6b78d1))

- **base**: Public kb register function
  ([`49bf8f2`](https://github.com/tobiashochguertel/InquirerPrompt/commit/49bf8f246adba1d1e12106b3481968c7f475bcdf))

- **base**: Show cursor
  ([`2ee8c57`](https://github.com/tobiashochguertel/InquirerPrompt/commit/2ee8c5751b69fd47517dbcd84209bd8a27caedcf))

- **checkbox**: Added more key_bindings
  ([`5a63c7c`](https://github.com/tobiashochguertel/InquirerPrompt/commit/5a63c7c652a2fedc12e7648df405dc96fdf2f5ef))

- **checkbox**: Handle separator
  ([`7aa6201`](https://github.com/tobiashochguertel/InquirerPrompt/commit/7aa620194de992d8be1de7fd32a7b7068bb9f0b5))

- **checkbox**: Implemented basic functionality
  ([`e25cbea`](https://github.com/tobiashochguertel/InquirerPrompt/commit/e25cbea81124ae40df275cc0b808fc5e1793fa17))

- **checkbox**: Init
  ([`566ab37`](https://github.com/tobiashochguertel/InquirerPrompt/commit/566ab37060e5615b9b107c9800d5fdb24da58d55))

- **checkbox**: Update default pointer behavior
  ([`fcf4e98`](https://github.com/tobiashochguertel/InquirerPrompt/commit/fcf4e98ed931042b7e664730d5edd829a219ca54))

- **choice**: Update selected_choice_index when result count is less
  ([`0ea3d71`](https://github.com/tobiashochguertel/InquirerPrompt/commit/0ea3d7125d7a13d7c56cd5f3306450ebfe539aac))

- **confirm**: Init confirm prompt
  ([`515a2d2`](https://github.com/tobiashochguertel/InquirerPrompt/commit/515a2d2db8b5116c441f095258c8b2d94135cf8b))

- **confirm**: Safer parameter passing
  ([`bfde87d`](https://github.com/tobiashochguertel/InquirerPrompt/commit/bfde87dae3098d39f2f56ea327950657980c7523))

- **expand**: Allow instruction override
  ([`6f45d88`](https://github.com/tobiashochguertel/InquirerPrompt/commit/6f45d884d9aa01460948f17b5563828edcd5e086))

- **expand**: Deny key binding if not expanded
  ([`15cacac`](https://github.com/tobiashochguertel/InquirerPrompt/commit/15cacac1dcac02f7e309fcea098acbff119a7ec9))

- **expand**: Expand the prompt
  ([`7966d80`](https://github.com/tobiashochguertel/InquirerPrompt/commit/7966d801f79e1e5530e624e55bd502927002ce22))

- **expand**: Fix separator handling
  ([`6f4df9c`](https://github.com/tobiashochguertel/InquirerPrompt/commit/6f4df9cf9ae9d265ec0a4996d2e30de01f562628))

- **expand**: Init
  ([`7066bc4`](https://github.com/tobiashochguertel/InquirerPrompt/commit/7066bc4e9ce7170f1ffe7830e96d38d106275c2b))

- **expand**: Replicate behaviro of expand help option in Inquirer.js
  ([`8b0405f`](https://github.com/tobiashochguertel/InquirerPrompt/commit/8b0405f5202e6f1ebb1f46810a752e86dbed9608))

- **expand**: Setup keybinding_factory
  ([`f95d7da`](https://github.com/tobiashochguertel/InquirerPrompt/commit/f95d7da50d6d05b4d1c5817012eaa4aec0e28016))

- **filepath**: Allow custom validation
  ([`e30fffa`](https://github.com/tobiashochguertel/InquirerPrompt/commit/e30fffa7f45e80293242b8a659a13579e62ae58d))

- **filepath**: Complete in thread
  ([`d99b18d`](https://github.com/tobiashochguertel/InquirerPrompt/commit/d99b18dbecc75fa510e2088d17ed2455fc1b27b5))

- **filepath**: Complete only files
  ([`e500db0`](https://github.com/tobiashochguertel/InquirerPrompt/commit/e500db040f0d7957447f02f9594f18dc3aef6b14))

- **filepath**: Customise editing mode
  ([`f0c6357`](https://github.com/tobiashochguertel/InquirerPrompt/commit/f0c6357c6ea1a434a0975e2c62f94afc9c9ca6d0))

- **filepath**: Filter directories
  ([`41a8692`](https://github.com/tobiashochguertel/InquirerPrompt/commit/41a8692f6e46d6443de0a0976a4b65ec48f3f611))

- **filepath**: Implemented default functionality
  ([`1d9e12f`](https://github.com/tobiashochguertel/InquirerPrompt/commit/1d9e12f460a4fe1341524769da2d72ab76004ba7))

- **fuzzy**: Add validation toolbar to floating
  ([`a478b57`](https://github.com/tobiashochguertel/InquirerPrompt/commit/a478b57afabd7b95065698727fbcf5f421ddc637))

- **fuzzy**: Add validator
  ([`870de43`](https://github.com/tobiashochguertel/InquirerPrompt/commit/870de43ee20ab236c388d2e8093a66cb79a01e2c))

- **fuzzy**: Added fuzzy to resolver
  ([`59087ff`](https://github.com/tobiashochguertel/InquirerPrompt/commit/59087ff852fdf7008f8bf7dbe6697f70263d441b))

- **fuzzy**: Added more styling option and border
  ([`5993921`](https://github.com/tobiashochguertel/InquirerPrompt/commit/5993921e2cc84e77bb58129ca41dcd75674c4f70))

- **fuzzy**: Async filter
  ([`22d66ad`](https://github.com/tobiashochguertel/InquirerPrompt/commit/22d66adeecabc2801a86b409e33326cfa29ef540))

- **fuzzy**: Calcualte wait time
  ([`c53397f`](https://github.com/tobiashochguertel/InquirerPrompt/commit/c53397fd200b2febccd735abde635c0485805f0c))

- **fuzzy**: Customize height
  ([`70605b9`](https://github.com/tobiashochguertel/InquirerPrompt/commit/70605b916591ae236d5b4d721269a1c18825fe3d))

- **fuzzy**: Default lexer for the filter bar
  ([`1259079`](https://github.com/tobiashochguertel/InquirerPrompt/commit/12590794b3a159754f57cdfd69a56f72defcfef3))

- **fuzzy**: Display selected number as info
  ([`68ebfe5`](https://github.com/tobiashochguertel/InquirerPrompt/commit/68ebfe59b87a4c4effd205a183ce348979c2fe22))

- **fuzzy**: Filter choices
  ([`a86c8bf`](https://github.com/tobiashochguertel/InquirerPrompt/commit/a86c8bf031385c4f1ac3c6eed49de567b54db5a8))

- **fuzzy**: Filter in async
  ([`c551f19`](https://github.com/tobiashochguertel/InquirerPrompt/commit/c551f199e30bd8b0f68f489349c3838fbf689fbb))

- **fuzzy**: Handle optional multiselect
  ([`e169d22`](https://github.com/tobiashochguertel/InquirerPrompt/commit/e169d22c2c78725f38a3dbe49b888ce235c722d9))

- **fuzzy**: Highlight matched string
  ([`5a40746`](https://github.com/tobiashochguertel/InquirerPrompt/commit/5a40746aa979c560a94ba64aa9e63eaf40eb97bf))

- **fuzzy**: Improve render performance
  ([`840834b`](https://github.com/tobiashochguertel/InquirerPrompt/commit/840834b13aff7404eed0431487719e5ee9fa2161))

- **fuzzy**: Load choices after render if callable
  ([`bf7a17c`](https://github.com/tobiashochguertel/InquirerPrompt/commit/bf7a17cf59d84220b1e51f74984fd6e0f171a4e1))

- **fuzzy**: Set default value to buffer if passed in
  ([`21ea20f`](https://github.com/tobiashochguertel/InquirerPrompt/commit/21ea20f4c0bab49141ce8be9393a7be459d29195))

- **fuzzy**: Setup fuzzy processing function
  ([`8350119`](https://github.com/tobiashochguertel/InquirerPrompt/commit/83501191b9e61c0c04162593d2c94cd5f15df9ff))

- **input**: Added input prompt
  ([`aedc320`](https://github.com/tobiashochguertel/InquirerPrompt/commit/aedc320f66b07170bfab50be96cc9352ae2e8382))

- **input**: Prettier input for multiline
  ([`80b187a`](https://github.com/tobiashochguertel/InquirerPrompt/commit/80b187a757f150877e89f51346eb02e790e78f34))

- **list**: Allow more value type
  ([`1c9a3c9`](https://github.com/tobiashochguertel/InquirerPrompt/commit/1c9a3c95dd1bf72427ed3672b0c3a03c40318f16))

- **list**: Allow separator
  ([`b9327a5`](https://github.com/tobiashochguertel/InquirerPrompt/commit/b9327a54a79e1989e61487a3e1c5afd9a949acee))

- **list**: Change default pointer behavior
  ([`0fa902f`](https://github.com/tobiashochguertel/InquirerPrompt/commit/0fa902f5a8419b4157da2d7bbb68dec73cedb2cd))

- **list**: Init the list prompt
  ([`4355b8f`](https://github.com/tobiashochguertel/InquirerPrompt/commit/4355b8f0db18e0c3dcc557c5ca190354e567f1f3))

- **rawlist**: Display index as input in prompt message
  ([`31aa1f8`](https://github.com/tobiashochguertel/InquirerPrompt/commit/31aa1f81340b1652833a405bc94ab71296a19e16))

- **rawlist**: Handle separator
  ([`073d218`](https://github.com/tobiashochguertel/InquirerPrompt/commit/073d218f3e3e97ba1b3658dcca79442c9bffd7cb))

- **rawlist**: Implemented rawlist
  ([`e55c4f1`](https://github.com/tobiashochguertel/InquirerPrompt/commit/e55c4f19fc2f120e161896960d111cf79b1458dd))

- **rawlist**: Set a different default pointer behavior
  ([`12fefcb`](https://github.com/tobiashochguertel/InquirerPrompt/commit/12fefcb0f35d201e7f1fb065c3ae1b01a635c136))

- **resolver**: Added filepath mapping
  ([`2144a01`](https://github.com/tobiashochguertel/InquirerPrompt/commit/2144a01c94af72f7bbaa99f92dedee17333e121f))

- **resolver**: Added filter
  ([`a9c578e`](https://github.com/tobiashochguertel/InquirerPrompt/commit/a9c578e15f79a270f03d049ae430fc8e8d9c863e))

- **resolver**: Conditional question
  ([`961b464`](https://github.com/tobiashochguertel/InquirerPrompt/commit/961b464debf34ad2b0670f357f8e7fbb67f5f46c))

- **resolver**: Read environment variable for style and keybindings
  ([`9591047`](https://github.com/tobiashochguertel/InquirerPrompt/commit/9591047aa08c353a21742f5a690e60f3416d7751))

- **secret**: Basic secret prompt
  ([`75d8571`](https://github.com/tobiashochguertel/InquirerPrompt/commit/75d8571764d925c4e0b41567eef3951de3dedfe3))

- **utils**: Added color print func
  ([`a6248ad`](https://github.com/tobiashochguertel/InquirerPrompt/commit/a6248adb9b78a6af982df9b95a823a82dd6a856b))

- **utils**: If height is provided, set max_height to 100%
  ([`92d72f4`](https://github.com/tobiashochguertel/InquirerPrompt/commit/92d72f4fb1a676cb3782a4118501b0a5c61cd8dc))

- **utils**: Patched_print
  ([`69f17e4`](https://github.com/tobiashochguertel/InquirerPrompt/commit/69f17e410057dd70183063be6ae1ddcd4f91f98b))

- **utils**: Resolve ENV even if style_override
  ([`dd92452`](https://github.com/tobiashochguertel/InquirerPrompt/commit/dd92452eb839ffaa38592028d7c5a819aa2844b2))

- **utils**: Set default max_height to 50%
  ([`51146de`](https://github.com/tobiashochguertel/InquirerPrompt/commit/51146dec7a27c5450ed7f6f92f0d538d64e83d95))

- **validator**: Added a basic empty validator
  ([`d709c26`](https://github.com/tobiashochguertel/InquirerPrompt/commit/d709c2656840388a20e9ec269b13901aa5a820e9))

- **validator**: Added basic validator class
  ([`057ddc6`](https://github.com/tobiashochguertel/InquirerPrompt/commit/057ddc6f99166d0cb6145a924591108878947d1d))

- **validator**: Added more condition for filepath validator
  ([`c8fff6e`](https://github.com/tobiashochguertel/InquirerPrompt/commit/c8fff6e6761a90ace73576b935987b5980120cb5))

- **validator**: Added NumberValidator
  ([`369a96c`](https://github.com/tobiashochguertel/InquirerPrompt/commit/369a96c920d50154da5d7f40b4fe7abff93f48af))

- **validator**: Added password validator
  ([`dc37fbe`](https://github.com/tobiashochguertel/InquirerPrompt/commit/dc37fbef91cf88d4b9b4941228a1fd8ae19df546))

- **validator**: Export only required validators
  ([`e1d3d3f`](https://github.com/tobiashochguertel/InquirerPrompt/commit/e1d3d3f13c1963755215ab66bf3f991c55d6c585))

### Refactoring

- Abstract _format_choices
  ([`53d9edc`](https://github.com/tobiashochguertel/InquirerPrompt/commit/53d9edcb2a01be47881a1c05ccc9353f984f4fe0))

- Abstract common function between fuzzy and BaseComplexPrompt
  ([`63b2c75`](https://github.com/tobiashochguertel/InquirerPrompt/commit/63b2c7597f1e2d440c696e5b7f080e0ad71e10c9))

- Added base class for simple prompts
  ([`f8391f8`](https://github.com/tobiashochguertel/InquirerPrompt/commit/f8391f8f9a4e8ba3fcad9155222881dff59531ae))

- Added multiselect to rawlist and expand
  ([`b1e4cd8`](https://github.com/tobiashochguertel/InquirerPrompt/commit/b1e4cd858c66ef7645527b17950c2d8e2b9ce9e3))

- Adjust default keybinding, alt-i has weird issues
  ([`4557d9b`](https://github.com/tobiashochguertel/InquirerPrompt/commit/4557d9bc95f3b57fec5076ffedabe13421fa6dc0))

- Adjustment around default exception, style
  ([`353b8fc`](https://github.com/tobiashochguertel/InquirerPrompt/commit/353b8fcb52a25e76939397957f8276fe5bf21ef1))

- Change default fuzzy_info color
  ([`be7dbb5`](https://github.com/tobiashochguertel/InquirerPrompt/commit/be7dbb5477288edc37add02f8f374dba76317cb2))

- Change movement function to private function
  ([`66b2e22`](https://github.com/tobiashochguertel/InquirerPrompt/commit/66b2e22a7d27cce178ced20a62544e77a8702f5a))

- Change param name to match Inquirer.js or PyInquirer
  ([`17dc323`](https://github.com/tobiashochguertel/InquirerPrompt/commit/17dc323e171396bab6b2b469d116c6c2ae59fb80))

- Change style qmark to questionmark
  ([`6d03e84`](https://github.com/tobiashochguertel/InquirerPrompt/commit/6d03e84033cdbcaae51dca6561c37c26dd51aece))

- Choices callable with result as param
  ([`03ddfb6`](https://github.com/tobiashochguertel/InquirerPrompt/commit/03ddfb65ca7623822b92a8620727b6a7a35493ec))

- Enable multiselect for all list type prompt
  ([`ae78aa5`](https://github.com/tobiashochguertel/InquirerPrompt/commit/ae78aa5efa31cb686297e7a78bf9484d993ebb48))

- Format style
  ([`0432d5c`](https://github.com/tobiashochguertel/InquirerPrompt/commit/0432d5c838760e3b4a41f74a60e47c11a16aeb03))

- Hide choice window when loading
  ([`85f2087`](https://github.com/tobiashochguertel/InquirerPrompt/commit/85f208771c0039b58d9e8d3defa442a6ab0855a3))

- Kb registration decorator
  ([`f242051`](https://github.com/tobiashochguertel/InquirerPrompt/commit/f2420514d529ffa008c86273524f0c9a4af4c435))

- List type prompt default callable
  ([`371c928`](https://github.com/tobiashochguertel/InquirerPrompt/commit/371c9289923d7c05ff974d781ecc2497abc4cbf3))

- Move _register_kb up to parent class
  ([`1340a0d`](https://github.com/tobiashochguertel/InquirerPrompt/commit/1340a0d4e036b4f0af2757c484ee35c078b596c2))

- Move common attribute def into base class
  ([`4bddd97`](https://github.com/tobiashochguertel/InquirerPrompt/commit/4bddd97c8e987634487632192ce2c26c4843e623))

- Move common string to enum module
  ([`a803270`](https://github.com/tobiashochguertel/InquirerPrompt/commit/a8032702c906e49b321690f64f7d2380bc887ee2))

- Move filter in to baseclass
  ([`8c71348`](https://github.com/tobiashochguertel/InquirerPrompt/commit/8c713480158d22f8a7c684a8cd748de9f4cca1e3))

- Move filter into baseclass
  ([`e561433`](https://github.com/tobiashochguertel/InquirerPrompt/commit/e56143377d67a5a24c6a2f73dbbe575306c753ee))

- Move handle_enter, instruction to base class and doesn't
  ([`319309f`](https://github.com/tobiashochguertel/InquirerPrompt/commit/319309f94bb5ec40d26020cefe88771d726b948f))

- Move height calculation to util
  ([`01ef398`](https://github.com/tobiashochguertel/InquirerPrompt/commit/01ef39855d787c43eccf0fe211e44d545c24241c))

- Move keybinding resolving logic to base class
  ([`d6e4f34`](https://github.com/tobiashochguertel/InquirerPrompt/commit/d6e4f34f5ff9a48007645a2bbd7e1ab3ec1fa38c))

- Move validate to _handle_enter
  ([`7114c74`](https://github.com/tobiashochguertel/InquirerPrompt/commit/7114c74bf361b01717519ffe722bd236f1a72c34))

- New param session_result
  ([`8ddced0`](https://github.com/tobiashochguertel/InquirerPrompt/commit/8ddced00d23fc5a8f2ef82475e90919581429846))

- Optional style even at the base class
  ([`7c41dac`](https://github.com/tobiashochguertel/InquirerPrompt/commit/7c41daca98ed0e1bf346f20426de2b3181df5aaf))

- Rename option to choice
  ([`6a97979`](https://github.com/tobiashochguertel/InquirerPrompt/commit/6a97979452374df8f143a79bb17d4d922383df6d))

- Rename symbol to qmark
  ([`cdf0e10`](https://github.com/tobiashochguertel/InquirerPrompt/commit/cdf0e10d296906d48db0d98085d6333b1e88d32a))

- Rename util to utils
  ([`fdedd02`](https://github.com/tobiashochguertel/InquirerPrompt/commit/fdedd0236648a2e967edacf2026a58b07aaa2ac9))

- Rename validator to validate
  ([`f3397ff`](https://github.com/tobiashochguertel/InquirerPrompt/commit/f3397ff40f4783cc33a4e041a1bf2ca07877670a))

- Style qmark change to questionmark
  ([`c1171f6`](https://github.com/tobiashochguertel/InquirerPrompt/commit/c1171f6429ac18853233c49c8d36a012827e0f0b))

- Update attribute name and refactor default style processing
  ([`6a06d87`](https://github.com/tobiashochguertel/InquirerPrompt/commit/6a06d87e82316462808e2077322a46f8aad1a85f))

- Update class name
  ([`07e79fd`](https://github.com/tobiashochguertel/InquirerPrompt/commit/07e79fd705786c396a4aa859c665f8f814d38503))

- Update editing_mode param to vi_mode
  ([`d113a23`](https://github.com/tobiashochguertel/InquirerPrompt/commit/d113a23c027bd3cd2117929520ed0ab28fe94d4b))

- Update exception name
  ([`4d366e7`](https://github.com/tobiashochguertel/InquirerPrompt/commit/4d366e75d4c0d72523be0bebc57fea6067d7b157))

- Update filepath and secret to use input as base class
  ([`04e793d`](https://github.com/tobiashochguertel/InquirerPrompt/commit/04e793ddfa418e6e5800caa7aaa4509f0814c9c0))

- Update how to apply keybinding, for customize kb by user
  ([`e2f5aa1`](https://github.com/tobiashochguertel/InquirerPrompt/commit/e2f5aa189c91076ee304959205be6dc2aa2c5774))

- Update import
  ([`d710f37`](https://github.com/tobiashochguertel/InquirerPrompt/commit/d710f376fc519c398e0be1212f090a6a9de683f7))

- Update style processing
  ([`77a92b4`](https://github.com/tobiashochguertel/InquirerPrompt/commit/77a92b42f626c624b8df4888a566355084753dde))

- Update typing
  ([`2b145e4`](https://github.com/tobiashochguertel/InquirerPrompt/commit/2b145e45951d357d9a9ac37dccfc854aca80f19f))

- Use a style class instead of plain dict
  ([`5b8d674`](https://github.com/tobiashochguertel/InquirerPrompt/commit/5b8d6742ca45d520be00dd1d6de263bc2b3c855d))

- **base**: Added common string as param
  ([`0a95a0d`](https://github.com/tobiashochguertel/InquirerPrompt/commit/0a95a0de95f61ba83da7989be1c08a16094f5e52))

- **base**: Adjust type definition
  ([`62fccc3`](https://github.com/tobiashochguertel/InquirerPrompt/commit/62fccc31d77ce1e22c57908a6411fe578718ed78))

- **base**: Base class set lexer class
  ([`74d7bfc`](https://github.com/tobiashochguertel/InquirerPrompt/commit/74d7bfcfeb5e73d5b71b004ee1d62d5997350bed))

- **base**: Check index error before returning value
  ([`3155979`](https://github.com/tobiashochguertel/InquirerPrompt/commit/3155979e0691c797b34c4cc021381f1ae5e95332))

- **base**: Move old code to complex prompt
  ([`4a0556c`](https://github.com/tobiashochguertel/InquirerPrompt/commit/4a0556c86f889344e6e846f9a373d8130bcfc26d))

- **base**: Private function
  ([`e280bed`](https://github.com/tobiashochguertel/InquirerPrompt/commit/e280bed25e66bc9aaf7d68b26286ac7f26185932))

- **checkbox**: Refactor into function for key_bindings
  ([`0f91288`](https://github.com/tobiashochguertel/InquirerPrompt/commit/0f912880c955e1f2154727777ceee0cd69f597a3))

- **checkbox**: Set cursor position
  ([`305b8a1`](https://github.com/tobiashochguertel/InquirerPrompt/commit/305b8a10249514c7b94be24e9f2ddceb0f3a6a81))

- **checkbox**: Update selection logic
  ([`6723656`](https://github.com/tobiashochguertel/InquirerPrompt/commit/67236567d0819c95a199711d64cf3cde95098c60))

- **confirm**: Adjust structure, change to class for easier test
  ([`629caa1`](https://github.com/tobiashochguertel/InquirerPrompt/commit/629caa10b2a0d9b01b11ae547d2ed1861abf3161))

- **confirm**: Stop raising keyboardinterupt, let prompt_toolkit do
  ([`187b6f5`](https://github.com/tobiashochguertel/InquirerPrompt/commit/187b6f5e5362fbd1f200b878c8b6c09f3d87ef34))

- **examples**: Move examples
  ([`84ac923`](https://github.com/tobiashochguertel/InquirerPrompt/commit/84ac923fea6088a1a8072b6a431ef524b65b616a))

- **expand**: Set cursor position
  ([`1ab6c4e`](https://github.com/tobiashochguertel/InquirerPrompt/commit/1ab6c4e5c1a23596e266d340ddc0e8aa91477ac5))

- **filepath**: Use InputPrompt as base class
  ([`32c9157`](https://github.com/tobiashochguertel/InquirerPrompt/commit/32c9157c4b0655c018665eae71b9e0772355d68b))

- **fuzzy**: Cleaup and performance
  ([`505a747`](https://github.com/tobiashochguertel/InquirerPrompt/commit/505a747a81e7cb3f0a6f74b1723fce3c83c6a2ce))

- **fuzzy**: Inherit from newly created class
  ([`0ce123d`](https://github.com/tobiashochguertel/InquirerPrompt/commit/0ce123d4bd77d42209906cd7dfca0d9ac7db26f2))

- **fuzzy**: Leverage prompt toolkit eventloop
  ([`1a9a057`](https://github.com/tobiashochguertel/InquirerPrompt/commit/1a9a0579cfec84a2e4e18358acf6c3c238e215a7))

- **fuzzy**: Private attributes if not needed
  ([`79b37a3`](https://github.com/tobiashochguertel/InquirerPrompt/commit/79b37a3e8b4a2d091d33974717c3d1266e906d89))

- **input**: Clean up condition
  ([`ab9c6f9`](https://github.com/tobiashochguertel/InquirerPrompt/commit/ab9c6f904798f58948ac7b722e4adf8d7e1be303))

- **list**: Abstrct the list class
  ([`43c2a48`](https://github.com/tobiashochguertel/InquirerPrompt/commit/43c2a486be5b02526c600d6f7d0a42481f0abb3e))

- **list**: Remove unused attribute
  ([`ec62b41`](https://github.com/tobiashochguertel/InquirerPrompt/commit/ec62b419907070af3da3d1e04eee081df33cd923))

- **list**: Set cursor position
  ([`853b4da`](https://github.com/tobiashochguertel/InquirerPrompt/commit/853b4da04df29118a1b9d367aa59a1e45a0fa667))

- **resolver**: Rename secret to password
  ([`5f99b7b`](https://github.com/tobiashochguertel/InquirerPrompt/commit/5f99b7b5957b209afeda3bb954a4319dc253e848))

- **separator**: Pyinquirer compatible
  ([`0e68354`](https://github.com/tobiashochguertel/InquirerPrompt/commit/0e68354a84a6d9224608d217fa50055094a31fba))

### Testing

- Choices callable with result as param
  ([`6d6e468`](https://github.com/tobiashochguertel/InquirerPrompt/commit/6d6e468849b36d8757c2cee0b5e26126d4611018))

- Filter and transformer
  ([`181b030`](https://github.com/tobiashochguertel/InquirerPrompt/commit/181b03064f8eca7ff1f79a3591eb1f9a30aa4dad))

- Fix call check
  ([`736b3e8`](https://github.com/tobiashochguertel/InquirerPrompt/commit/736b3e8450dc58c0347fdddfc56c93b06b6038d7))

- Layout adjustment due to validation bar added to float
  ([`86be91f`](https://github.com/tobiashochguertel/InquirerPrompt/commit/86be91f732670610a34434b2042d891cf1730afb))

- List type prompt default callable
  ([`b393f5f`](https://github.com/tobiashochguertel/InquirerPrompt/commit/b393f5f57afbd301618d625c21a34a891e129ebb))

- Multicolumn_complete
  ([`9ee271a`](https://github.com/tobiashochguertel/InquirerPrompt/commit/9ee271ad9ccaf6976079225584db1df571540afd))

- Multiselect enter behavior of ListPrompt
  ([`b0d2f3f`](https://github.com/tobiashochguertel/InquirerPrompt/commit/b0d2f3fb7edb2aacd7c8ca91c6999f70e6b834e6))

- New param session_result
  ([`0a1e70b`](https://github.com/tobiashochguertel/InquirerPrompt/commit/0a1e70bfc5a6e3497b656e672f29c96bbca28cdf))

- Unnamed question
  ([`bc132a4`](https://github.com/tobiashochguertel/InquirerPrompt/commit/bc132a476edb80d81f73bbe859882243ef0a26ce))

- Update color
  ([`029bee5`](https://github.com/tobiashochguertel/InquirerPrompt/commit/029bee508df3ee1af29cfbfd8d4e2c93eb03b930))

- Update due to refactor
  ([`e84851f`](https://github.com/tobiashochguertel/InquirerPrompt/commit/e84851f1030367ad0be74a4f945a963b12d5b944))

- Update editing_mode param to vi_mode
  ([`a39ca67`](https://github.com/tobiashochguertel/InquirerPrompt/commit/a39ca673a3c9340df234744c891fc03a8626a004))

- Update style test
  ([`1f1d173`](https://github.com/tobiashochguertel/InquirerPrompt/commit/1f1d173ee29b84e91355e600e7b39deca868879c))

- Update test due to style update
  ([`d6cd3af`](https://github.com/tobiashochguertel/InquirerPrompt/commit/d6cd3afe484df39a399c6eecfd886b68d419cdb0))

- Update test for multiselect
  ([`98b0a53`](https://github.com/tobiashochguertel/InquirerPrompt/commit/98b0a5380b9d7b29ec6d49c1e161408007d2af30))

- Update test to match the changing default behavior
  ([`173a282`](https://github.com/tobiashochguertel/InquirerPrompt/commit/173a282b1db9cfd550c60e7c19dacb017ad16cee))

- Update test variables
  ([`92e766a`](https://github.com/tobiashochguertel/InquirerPrompt/commit/92e766a46cb38a4fd880d35a2a6efea2bc441584))

- Update tests due to changes to prompt param
  ([`99a0136`](https://github.com/tobiashochguertel/InquirerPrompt/commit/99a013620c2f8c6f1f280373f58478d719ec26e9))

- **checkbox**: After_render
  ([`1bf3ba3`](https://github.com/tobiashochguertel/InquirerPrompt/commit/1bf3ba38f9098b42fae01c379a24cc2bd5c84e2a))

- **checkbox**: Alt-a and alt-r process
  ([`50a8001`](https://github.com/tobiashochguertel/InquirerPrompt/commit/50a80010a231f9109a4172d039354703b6360570))

- **checkbox**: More coverage
  ([`9ec1b8b`](https://github.com/tobiashochguertel/InquirerPrompt/commit/9ec1b8b15c024f38e0ea8cd1a92ae991fc597027))

- **checkbox**: Test checkbox
  ([`046979e`](https://github.com/tobiashochguertel/InquirerPrompt/commit/046979e360c541ac02b7b037c457763adf5aac59))

- **checkbox**: Test validator
  ([`fe3c6e6`](https://github.com/tobiashochguertel/InquirerPrompt/commit/fe3c6e67aa67fc65aa7781b36a71146d7b2b0a6d))

- **checkbox**: Update
  ([`67ab947`](https://github.com/tobiashochguertel/InquirerPrompt/commit/67ab9477dd4d0a762110ff7374af6c70b4cd0591))

- **checkbox**: Update kb check
  ([`bc05e99`](https://github.com/tobiashochguertel/InquirerPrompt/commit/bc05e99aeee267a196e380bd5a00305ac70494ed))

- **checkbox**: Update kb test
  ([`099452c`](https://github.com/tobiashochguertel/InquirerPrompt/commit/099452c6db25b1de7a56ce28f417624f66d2e63d))

- **confirm**: Init test for confirm prompt
  ([`9918af0`](https://github.com/tobiashochguertel/InquirerPrompt/commit/9918af02a87492c1ed232b5ffd68ce1b3727d6f8))

- **confirm**: Kbi raise
  ([`53266c9`](https://github.com/tobiashochguertel/InquirerPrompt/commit/53266c973d4adba8b505079fd37eb66af6898239))

- **confirm**: Update test due to adjustment of parameter name
  ([`b5691d3`](https://github.com/tobiashochguertel/InquirerPrompt/commit/b5691d3f22376e804d3e72327d751e204e62cd43))

- **confirm**: Update test to adjust change of class
  ([`195a918`](https://github.com/tobiashochguertel/InquirerPrompt/commit/195a9180398182c083230b9c89e945b53d0b6c7d))

- **expand**: Full coverage
  ([`77d48bb`](https://github.com/tobiashochguertel/InquirerPrompt/commit/77d48bbb6d581f5f6efa17b876519a45b08c13b6))

- **expand**: Test content_control
  ([`1ed13d4`](https://github.com/tobiashochguertel/InquirerPrompt/commit/1ed13d4dcc7e2a5d501e916ca9f019ab97f22d06))

- **expand**: Test key against expand state
  ([`bbdc853`](https://github.com/tobiashochguertel/InquirerPrompt/commit/bbdc853374d6ba969b8bd10843e338559a1eadf9))

- **filepath**: Only_files
  ([`035dd83`](https://github.com/tobiashochguertel/InquirerPrompt/commit/035dd838ebc36de9c1f29d8af2b506532d9fa755))

- **filepath**: Test callable called
  ([`64ab4ae`](https://github.com/tobiashochguertel/InquirerPrompt/commit/64ab4aed55c43343f9ea10a9c29db415c8348238))

- **filepath**: Test completer
  ([`12f1b78`](https://github.com/tobiashochguertel/InquirerPrompt/commit/12f1b78d2206a6d3bd96edcb8290d0e2af02f748))

- **filepath**: Test get prompt message
  ([`c961a97`](https://github.com/tobiashochguertel/InquirerPrompt/commit/c961a97b0a8eb99f62418dd8fe485a6844b3d1f9))

- **fuzzy**: After_render
  ([`6ddb9b2`](https://github.com/tobiashochguertel/InquirerPrompt/commit/6ddb9b2bb3849f991afad6dbbd406037b7fd1845))

- **fuzzy**: Filter in async
  ([`bd300ec`](https://github.com/tobiashochguertel/InquirerPrompt/commit/bd300ecd9d5daf30ce1b10a307f878920871bf9f))

- **fuzzy**: More coverage
  ([`a55c4aa`](https://github.com/tobiashochguertel/InquirerPrompt/commit/a55c4aa2792067f393f22f8543de3882f7fbb625))

- **fuzzy**: Test fuzzy prompt init, height and filter
  ([`4ddace0`](https://github.com/tobiashochguertel/InquirerPrompt/commit/4ddace03b2ac9761fbc6c7c4ae37394e443c9ad3))

- **fuzzy**: Test fuzzy validator
  ([`e777529`](https://github.com/tobiashochguertel/InquirerPrompt/commit/e777529c5598f84c844a6c7c4d21b1c21279ac84))

- **fuzzy**: Test validation issue
  ([`9defade`](https://github.com/tobiashochguertel/InquirerPrompt/commit/9defade2265ca26a3e5c5c89a93e0927ab77799d))

- **fuzzy**: Tested choice content_control
  ([`d4eff39`](https://github.com/tobiashochguertel/InquirerPrompt/commit/d4eff39c399cad7459dad84549f19e24cdea702e))

- **fuzzy**: Toggle all
  ([`8904000`](https://github.com/tobiashochguertel/InquirerPrompt/commit/89040008bb15aca62e10e2d383b280c444111de7))

- **fuzzy**: Update
  ([`37b4319`](https://github.com/tobiashochguertel/InquirerPrompt/commit/37b43197c07393075159b9a0a6b48e8e3987078e))

- **fuzzy**: Wait_time
  ([`9b748cf`](https://github.com/tobiashochguertel/InquirerPrompt/commit/9b748cfa712816f4cc1a4702e75685bedf2174e5))

- **input**: Filter and transformer
  ([`5556484`](https://github.com/tobiashochguertel/InquirerPrompt/commit/55564842105ada33d7de7f4d35dab9a706002ce1))

- **input**: Fully test input prompt
  ([`ec39860`](https://github.com/tobiashochguertel/InquirerPrompt/commit/ec39860134b78b3dad0da848f7546593c6874125))

- **list**: After_render
  ([`2250ef0`](https://github.com/tobiashochguertel/InquirerPrompt/commit/2250ef0970f590cc4dad10118548df896fe80767))

- **list**: Cover minimum args
  ([`0206051`](https://github.com/tobiashochguertel/InquirerPrompt/commit/0206051a2983123dd7d84ac9412f2c89262619b3))

- **list**: Layout test update
  ([`0bc8299`](https://github.com/tobiashochguertel/InquirerPrompt/commit/0bc82994a745666ba30c3f87b70035eafa11eb3e))

- **list**: Show cursor
  ([`4b5c5f6`](https://github.com/tobiashochguertel/InquirerPrompt/commit/4b5c5f6ca34eb73e139f443212f3cb6dcef1a10f))

- **list**: Unittested list prompt
  ([`df850b0`](https://github.com/tobiashochguertel/InquirerPrompt/commit/df850b0a73959889cf1026d507a6a89c0033220a))

- **list**: Update
  ([`64029da`](https://github.com/tobiashochguertel/InquirerPrompt/commit/64029dae208a03c14b68bc7335e632baf575f5ab))

- **rawlist**: Implemented
  ([`09b882a`](https://github.com/tobiashochguertel/InquirerPrompt/commit/09b882aa101e6cd95aacce3e92d3a825f2b742b1))

- **rawlist**: Limit choices to 9
  ([`c11816a`](https://github.com/tobiashochguertel/InquirerPrompt/commit/c11816aeb391bba78a01bd1eca71f72403d9eb56))

- **rawlist**: Update
  ([`e17ee6b`](https://github.com/tobiashochguertel/InquirerPrompt/commit/e17ee6bd9cb12333d24b9a696994960c22d7e987))

- **rawlist**: Update test to cover new default value behavior
  ([`8eee103`](https://github.com/tobiashochguertel/InquirerPrompt/commit/8eee103b7980c2eaaf77a6dc622644d477311a52))

- **resolver**: Added covreage for filter, transformer and
  ([`7b4a88d`](https://github.com/tobiashochguertel/InquirerPrompt/commit/7b4a88db668a6574eaafe78dd75dd9472f949b67))

- **resolver**: Custom keybindings
  ([`85646d8`](https://github.com/tobiashochguertel/InquirerPrompt/commit/85646d8f597278ed973584a7de226eca7f40f130))

- **resolver**: Env raise kbi
  ([`29bfaa7`](https://github.com/tobiashochguertel/InquirerPrompt/commit/29bfaa7a30a591f049bbc01262186febbcc43cab))

- **resolver**: Env resolve priority
  ([`cde1d98`](https://github.com/tobiashochguertel/InquirerPrompt/commit/cde1d98997f8fb548f6205b920da892a61f44050))

- **resolver**: Fully cover resolver cases
  ([`521cc25`](https://github.com/tobiashochguertel/InquirerPrompt/commit/521cc257958dd81b085802288f7cacbe76b549aa))

- **resolver**: Kbi
  ([`31a4cbd`](https://github.com/tobiashochguertel/InquirerPrompt/commit/31a4cbdb9e9215fb2abf59924ab15694d6b4c062))

- **resolver**: Rename secret to password
  ([`fb53f53`](https://github.com/tobiashochguertel/InquirerPrompt/commit/fb53f53ca602e4a9e400be6f23c73e68b6a33af3))

- **resolver**: Single question dict
  ([`1a2be60`](https://github.com/tobiashochguertel/InquirerPrompt/commit/1a2be60e28e8b30be051da54de05d432b89937fb))

- **resolver**: Test question mapping
  ([`41c343b`](https://github.com/tobiashochguertel/InquirerPrompt/commit/41c343be6d92528f3aa39079fc7f8ea0cbce4dcd))

- **resolver**: Update keybinding test
  ([`345962b`](https://github.com/tobiashochguertel/InquirerPrompt/commit/345962b9ba97cb63feaf83a5523f24d090dbd4e3))

- **resolver**: When condition fix
  ([`1280029`](https://github.com/tobiashochguertel/InquirerPrompt/commit/1280029fcd50b013f4f8773367536a3ccbb898b8))

- **secret**: Complete unittest from secret prompt
  ([`3defc16`](https://github.com/tobiashochguertel/InquirerPrompt/commit/3defc1615910bd66d86c56457d4a42451d8c620f))

- **secret**: Init test
  ([`fca9fb4`](https://github.com/tobiashochguertel/InquirerPrompt/commit/fca9fb491002bffbda748ffbc82eaf21479e1c66))

- **utils**: Calculate height offset
  ([`90549d8`](https://github.com/tobiashochguertel/InquirerPrompt/commit/90549d88c179c00090d6dbf83b1333370713a1ad))

- **utils**: Color_print
  ([`efc126b`](https://github.com/tobiashochguertel/InquirerPrompt/commit/efc126b002a73884a03aeff85f42a447ad380b41))

- **utils**: Format style
  ([`e1f07c0`](https://github.com/tobiashochguertel/InquirerPrompt/commit/e1f07c043b76cbe95e672a3eeb4616ca35480007))

- **utils**: Move test to utils
  ([`2144dcc`](https://github.com/tobiashochguertel/InquirerPrompt/commit/2144dcc3f0bfe3580645e59f454f8566ad92c8b1))

- **utils**: Update height test
  ([`3a8bdd2`](https://github.com/tobiashochguertel/InquirerPrompt/commit/3a8bdd29111cf32a45f63b8f65b9fafa27e260fe))

- **validator**: Init test for validators
  ([`ca730af`](https://github.com/tobiashochguertel/InquirerPrompt/commit/ca730af7d346af2ef1acb0f274f6e676eedb3863))

- **validator**: Numbervalidator
  ([`0270ab3`](https://github.com/tobiashochguertel/InquirerPrompt/commit/0270ab3ea873b31e440922d140516ace4722611b))

- **validator**: Pathvalidator
  ([`a1ea81c`](https://github.com/tobiashochguertel/InquirerPrompt/commit/a1ea81c57575fc103c8ea4ac55d69d12268bb39f))
