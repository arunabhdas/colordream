Dream up pleasing color palettes with ML!

## Installation

1. Clone this repo, `git clone https://github.com/skcript/colordream.git`
2. CD into the directory, `cd colordream`
3. Enter the Python shell, `python`
4. Import ColorDream and use!

```
>>> from colordream import ColorDream

# Get an object instance
>>> cd = ColorDream()

# Train the ML
>>> cd.train()
```

## Usage
The ColorDream engine gives you pleasing color choices based on an input you provide. The input is 2 colors and the ML engine returns 3 color matches that works best.

Version 0.1 (current) works only with RGB values passed as an array.

An example,

```
>>> palette = [[228, 87, 46, 1], [41, 51, 92, 1]]
>>> cd.test(palette)
```

## Contribution Guidelines
- Raise an issue on https://github.com/skcript/colordream/issues
- Write appropriate comments and add test cases
- Raise a pull request
- Wait for a merge! 💃🏼
