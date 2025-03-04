# converter cli

I got tired of existing converter tools for waypoint files. This is just the initial basis for a more full-fledged
converter.

# usage

1. install [uv](https://github.com/astral-sh/uv)
2. `uv run main.py --help`

## convert

```console
❯ uv run main.py convert --help
Usage: main.py convert [OPTIONS]

Options:
  -s, --source TEXT        Source file to convert from  \[required]
  -d, --destionation TEXT  destination_file file to convert to  \[required]
  --help                   Show this message and exit.
```

eg.

Provide a `.kml` file, output a `.wpt` file.

```console
uv run main.py convert -s /paragliding/sandcity/sand-city.kml -d /paragliding/sandcity/sand-city.wpt
```

# Currently Supported conversions

Basically covering my only current use case of taking [google earth](https://earth.google.com/) KML files and converint
to `.wpt` waypoint files for importing into [xctrack](https://xctrack.org/). Happy to add more if it would be handy.

- `kml` -->
    - `wpt`
- `wpt` -->
    - `kml`