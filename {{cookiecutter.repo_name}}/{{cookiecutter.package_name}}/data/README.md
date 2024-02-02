# Sample Package Data

This directory contains sample additional data you may want to include with your package.
This is a place where non-code related additional information (such as data files, molecular structures,  etc.) can 
go that you want to ship alongside your code.

Please note that it is not recommended to place large files in your git directory. If your project requires files larger
than a few megabytes in size it is recommended to host these files elsewhere. This is especially true for binary files
as the `git` structure is unable to correctly take updates to these files and will store a complete copy of every version
in your `git` history which can quickly add up. As a note most `git` hosting services like GitHub have a 1 GB per repository
cap.

## Including package data

Modify your package's `pyproject.toml` file.
Update the [tool.setuptools.package_data](https://setuptools.pypa.io/en/latest/userguide/datafiles.html#package-data)
and point it at the correct files.
Paths are relative to `package_dir`.

Package data can be accessed at run time with `importlib.resources` or the `importlib_resources` back port.
See https://setuptools.pypa.io/en/latest/userguide/datafiles.html#accessing-data-files-at-runtime
for suggestions.

If modules within your package will access internal data files using
[the recommended approach](https://setuptools.pypa.io/en/latest/userguide/datafiles.html#accessing-data-files-at-runtime),
you may need to include `importlib_resources` in your package dependencies.
In `pyproject.toml`, include the following in your `[project]` table.
```
dependencies = [
    "importlib-resources;python_version<'3.10'",
]
```

## Manifest

* `look_and_say.dat`: first entries of the "Look and Say" integer series, sequence [A005150](https://oeis.org/A005150)
