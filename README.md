# MonkeyBusiness

Experimental e-amuse server intended for testing hacks, also usable by players

## Usage

Run [start.bat (Windows)](start.bat) or [start.sh (Linux, MacOS)](start.sh)

[web interface](https://github.com/drmext/BounceTrippy/releases), [score import](utils/db)

## Playable Games
- IIDX 18-20, 29-34 (Online Arena/BPL support)
- DDR A20P, A3, WORLD (OmniMIX/GF, BPL, and Fake PFREE support)
- GD 6-10 DELTA (Battle Mode support)
- DRS
- NOST 3
- SDVX 6-7

**Note**: Playable means settings/scores *should* save and load. Events are not implemented.

## Troubleshooting

- Delete [or fix](make_venv_portable.bat) `/.venv` if the server folder is moved or python is upgraded

- DRS, GD, NOST, and SDVX require mdb xml files copied to the server folder

- When initially creating a DDR profile, complete an entire credit without pfree hacks

- Update the webui
