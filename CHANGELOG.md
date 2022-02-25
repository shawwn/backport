# Changelog

<!--next-version-placeholder-->

## v0.3.1 (2022-02-25)
### Fix
* Don't automatically override the builtin types/typing/dataclasses modules; Don't rely on Python version numbers to influence backport.types behavior ([`610a643`](https://github.com/shawwn/backport/commit/610a6432124e3e88da7cb505f89e812c6e1e135f))

## v0.3.0 (2022-02-08)
### Feature
* Backport from Python 3.10: types, typing, dataclasses, abc.update_abstractmethods as abc_ext.update_abstractmethods, inspect.get_annotations as inspect_ext.get_annotations ([`3a3b505`](https://github.com/shawwn/backport/commit/3a3b505724e7017c03bb8681525539047d9665fe))

## v0.2.0 (2022-02-08)
### Feature
* Add backport.__version__ ([`63b47ad`](https://github.com/shawwn/backport/commit/63b47ada11e209532f07f23618b643ea1f1a6671))
