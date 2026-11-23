# Two Lines of Morning Light — entry notes

## Final couplet (94 characters including the line break, no trailing newline)

```
Light arrives through the blinds in stripes —
the cat wears them, and for a moment is a tiger.
```

## Why this one wins

The judge's brief asks for one image of light arriving, with the second line
*opening* the image rather than restating it. Here the image is striped light
coming through the blinds; the second line turns those stripes into a tiger's,
worn by the cat — a small, silent transformation. Nothing is named outright:
no dawn, no gold, no waking, no feeling stated. The em-dash break suspends the
first line, and the "stripes / tiger" echo gives the couplet its sound. What is
left unsaid — the brief daily magic of it, and why it lasts only "for a
moment" — leaves the poem larger than its two lines.

## Runners-up

- "Under the door, a blade of light; / the cat steps over it into morning."
- "Morning light, thin as a letter slipped under the door — / we read it with our bare feet."
- "A shaft of light leans in the stairwell — / dust climbs it, going somewhere bright."
- "It enters under the door, one bright thread; / by noon the whole room is sewn with light."

The runners-up each work a single image well (a blade, a letter, a shaft, a
thread), but the winner's second line changes what the first line *means*
instead of extending it, which is exactly the turn the brief rewards.

## Program

`main.py` (Python standard library only) embeds the couplet as a constant and
writes it as UTF-8 bytes to `entry.txt` in the output directory —
`MAKEFUN_OUTPUT_DIR` if set, else `/output` — creating the directory first and
writing nowhere else. No clock, no randomness: two runs are byte-identical.

## Verification

Tested under simulated server conditions: read-only working directory, empty
environment (`env -i`, no `MAKEFUN_OUTPUT_DIR`), writable stand-in at the
output path. Exit 0, `entry.txt` produced only in the output directory,
exactly two lines, 94 characters including the line break, byte-identical
across two runs.
