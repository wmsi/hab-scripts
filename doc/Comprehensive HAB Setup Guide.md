#### [Past WMSI Guide](https://docs.google.com/document/d/1ZFpF97Y5OiolW6akIYZ9gOIMfNHRjPRHA_6MLmYhKA4/edit)

#### [Dave Akerman’s Complete Guide](http://www.daveakerman.com/?p=1732)

**NOTE!!! -- Look at our****[ Berlin Guide** ](https://docs.google.com/document/d/1Qs4iHLOsIDn_k9iYtV5Rj-4AxdC1OQxgeXO8yhGX0yo/edit#)**for latest work on an A-Z instruction set.**

## Overview Checklist

**See ****[this lucid char**t](https://www.lucidchart.com/documents/edit/68dc35cf-8dc5-4b39-81c2-32f3b6c5494b#)** for a broad overview (GREAT STARTING PLACE!)**

See [this lucid chart ](https://www.lucidchart.com/documents/edit/31c9fb77-cfe0-4ccf-baf6-2958ac448bfc)for an overview of the radio systems

1. Install and setup tracker software on Balloon Pi 

    1. With required RTTY board

    2. With optional LORA board

    3. With optional APRS board

    4. With optional USB / RPi Camera

2. Install and setup gateway software on ground station Pi

    5. Optionally with LORA board

3. Setup tracker RTTY telemetry receptions and decode.  Follow PITS’ guide.

    6. [for SDR] Setup GQRX or similar software-defined radio interface

    7. Setup Dl-fldigi for receiving RTTY telemetry

    8. Setup Dl-fldigi to work with HabHub for telemetry publishing.  See below for more details; see [habitat.habhub.org/genpayload](http://habitat.habhub.org/genpayload) for details.

## [Tracker Setup](https://drive.google.com/open?id=1-A6Nc35wiFbwoCmUa0WW8bS8rhBATjLagRJKLktG1_Q)

## [Ground Station Setup](https://drive.google.com/open?id=1bzXN15sgmevQ5vlYJJ5ax8ZhUK_JHZSXjYKJSROzY5U)

### In Progress / Known Issues

* **APRS Won’t Send Packets**** if ****tracker**** is manually launched.  **This issue arose when the raspbian installation prior to May 26th 2017 was bricked due to an update.  A backup SD card was then used for a quick replacement; the replacement installation of raspbian and the configurations for tracker don’t send APRS packets if launched manually.  This issue may relate to how tracker is installed and/or is launched on boot.

    * **Workaround (1/3/2017): **Though the issue still exists when running the** ***tracker *script manually, **APRS will work if you run the ****_startup_**** script manually**.

    * **Possible solution:** The old Pi *did* send APRS packets if the tracker was manually launched...look at how the old script/tracker application was started on the old Pi.

* **Documentation**

    * **Testing checklist**

    * **Flight planning**

    * **Mission Rule****s**

