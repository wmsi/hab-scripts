# rtty-groundstation-startup
These scripts are designed to guide a user through starting up the software required
to use DL-FLDIGI with a software-defined radio, to recieve RTTY telemetry from a High Altitude Balloon.

This involves creating a Virtual Audio Loopback Device, starting up the SDR tool GQRX
and configuring it to output to that Loopback Device, and then starting up DL-FLDIGI
and listening to that device.

## Installation
You will need to have [GQRX](http://gqrx.dk/) and [DL-FLDIGI](https://ukhas.org.uk/projects:dl-fldigi) installed to use this script.

You will also need to configure some variables to your setup:
- Set `DL_FLDIGI_ROOT` to the `src/` directory of your DL-FLDIGI installation.
- Set `GQRX_ROOT` to the root directory of your GQRX installation, or ignore this/leave it blank if you installed GQRX via apt-get.

This has been tested on both the Raspberry Pi and a Lenovo Laptop.

## Usage
To execute the scripts, simply run ./start_all as a normal (non-sudo) user
in a terminal on the Pi desktop, and then follow the prompts.

See also White Mountain Science's [internal guide](https://docs.google.com/document/d/1bzXN15sgmevQ5vlYJJ5ax8ZhUK_JHZSXjYKJSROzY5U/edit#heading=h.l4br9kx5sb2g) or our [script usage guide](https://docs.google.com/document/d/1YyQdTc5vErq8AetqWkQUkAtAH35LsKyGhh1qk3cgxRU/edit?usp=sharing)

To contact us, see [whitemountainscience.org](whitemountainscience.org)
