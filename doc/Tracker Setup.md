# Tracker Setup

#### Starting From Scratch

##### 	Hardware

* [Pi in the Sky kit](https://store.uputronics.com/index.php?route=product/product&path=62&product_id=52)

* [How to connect board ](http://www.pi-in-the-sky.com/index.php?id=board-connections)

* [Stacking multiple boards](http://www.pi-in-the-sky.com/index.php?id=stacking-guide)

    * The order of the boards may affect their functionality.  A known-working stacking order is: Pi > PITS Board > APRS Board > LoRa Board. (i.e. Add the APRS board between the two boards stacking the tutorial)

##### 	Software

**[PITS** ](http://www.pi-in-the-sky.com/index.php?id=sd-card-image-from-scratch)**[tracke**r](http://www.pi-in-the-sky.com/index.php?id=sd-card-image-from-scratch)**[ Installation Guid**e](http://www.pi-in-the-sky.com/index.php?id=sd-card-image-from-scratch)

* **NOTE (1/3/2018):** Now that Raspbian has migrated over to version Stretch (instead of Jessie), it’s harder to find the Jessie image. So, **here’s the ****[direct download lin**k](https://downloads.raspberrypi.org/raspbian_lite/images/raspbian_lite-2017-07-05/2017-07-05-raspbian-jessie-lite.zip)** and the folder on Raspbian’s servers where you can find all the ****[lite** ](https://downloads.raspberrypi.org/raspbian_lite/images/)**and ****[normal** ](https://downloads.raspberrypi.org/raspbian/images/)**images**

* It’s good to **double-check the install process **for PITS at [https://github.com/PiInTheSky/pits](https://github.com/PiInTheSky/pits) (though we’ve tried to cover the differences below)

* It may be a good idea to run [rpi-update](https://github.com/Hexxeh/rpi-update) to **update the Pi’s firmware**. Note, however, that this is third party software (not by the RPi foundation), and has been known to wreck Raspbian installations, so **do this early on in the process.**

    * This can often **solve camera issues**

* Make sure to install ssdv or it will not send images over LoRa/RTTY! (There is no logging of errors due to missing packages.)

* To use a USB camera, make sure to install fswebcam via apt-get.

* To log telemetry data in the metadata of images (stored on the pi), make sure to install exiv2 via apt-get.

#### Configuration

You will edit **/boot/pisky.txt**; see [http://www.pi-in-the-sky.com/index.php?id=configuration](http://www.pi-in-the-sky.com/index.php?id=configuration) for key points in this configuration. 

Below are transmission-format-specific configuration details.

##### Configuring RTTY

* Make sure to set payload to a unique value (from LoRa)

* RTTY is enabled by default, but you can disable by setting 

Disable_RTTY=Y

##### 	Configuring APRS

* To enable APRS, you *must have* the following lines; their values can, however, be changed:

APRS_Callsign= CHANGEME # Change this...

APRS_ID=11 # 11 is for balloons.

APRS_Period=1 # MUST be an int!

APRS_Offset=10 # A good default; must be > 0

APRS_Random=5 # > 0; 5 seconds is enough randomness…

* [Main PITS docs](http://www.pi-in-the-sky.com/index.php?id=aprs-configuration)

##### 	Configuring LoRa

* To enable LoRa, you *must have* the following lines; their values can, however, be changed

* **NOTE:** the number provided in each setting allows you to have two configurations, the _0 configuration and the _1 one. This is because the LoRa chip has two slots, so you can configure two simultaneous LoRa transmitters with different settings.

			LORA_Frequency_0= 434.450 # A good default; can be changed

LORA_Payload_0= CHANGEME # Whatever you want, but **must be unique** (not the same as other channel or RTTY)

LORA_Mode_0= 0 # see note

**AND/OR**

LORA_Frequency_1= 434.450 # different from above

LORA_Payload_1= CHANGEME # see above

LORA_Mode_1= 0 # you’d likely be using something different here

* **NOTE** on LORA_Mode: Generally, this set to 0 (infrequent transmissions) for just telemetry and 1 (continuous transmissions) for SSDV images, but other advanced modes exist. If you’re interested in exploring them, check out the modes [here](https://github.com/PiInTheSky/pits/blob/master/tracker/lora.c#L55)

* [Main PITS docs](http://www.pi-in-the-sky.com/index.php?id=making-a-lora-tracker)

##### Configuring Camera

* PITS Guide: [https://github.com/PiInTheSky/pits#usb-camera](https://github.com/PiInTheSky/pits#usb-camera) 

* Modes (the value of the "camera" configuration parameter):

<table>
  <tr>
    <td>Config setting</td>
    <td>Function</td>
    <td>Use</td>
  </tr>
  <tr>
    <td>G/g </td>
    <td>gphoto2</td>
    <td>USB Camera (Canon connected via USB, etc...you must ensure your model is compatible with gphoto2 online.)</td>
  </tr>
  <tr>
    <td>U/F/u/f</td>
    <td>fswebcam</td>
    <td>USB Webcam</td>
  </tr>
  <tr>
    <td>N/n</td>
    <td>No camera</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Y/y/1/TC/c</td>
    <td>CSI camera</td>
    <td>RPi (CSI) camera</td>
  </tr>
</table>


    * Camera can be **enabled ONLY over LORA** by enabling camera (via camera=Y OR camera=U) and setting image_packets=0

#### Displaying telemetry overlay on images

* Make sure to install imagemagick via using: 

sudo apt-get install imagemagick

* Create the script referenced by the tracker program by **downloading our script from ****[her**e](https://github.com/wmsi/hab-scripts/blob/master/hab/image-processing/process_image)** and putting it in ****~/pits/tracker ****(****_run these commands):_**

cd ~/pits/tracker

wget [https://github.com/wmsi/hab-scripts/blob/master/hab/image-processing/process_image](https://github.com/wmsi/hab-scripts/blob/master/hab/image-processing/process_image)

		chmod +x process_image # make sure it can be executed

* **Alternatively, you can manually edit it from the original sample:**

		cd ~/pits/tracker

		cp process_image.sample process_image

		chmod +x process_image # make sure to set executable!

You’ll want to modify some things (since you haven’t used our file):

    * Make sure the font used to add the text is available on this system by setting the -font parameter on the convert call at the end of the file (choose one from this list:)

		convert -list font

    * You’ll likely want to make the font smaller by changing the -pointsize parameter on the convert call (we like size 18)

    * You may want to remove the odd rectangles by removing the -fill lines drawing them (we’re not sure why this rectangle is here)

    * Normally, metadata is only added to the files **sent** over RTTY/LORA via SSDV, but if you want to store the files on the tracker, add these lines to the end of the script to copy them from the temp image (ssdv.jpg) to the original folder:

# normally the original images are unchanged,

# but we decided to overwrite them with the converted (and add a backup)

prefix=$(basename $(dirname $2)) # last directory

mkdir -p images/ORIGINAL/$prefix/

mv $2 images/ORIGINAL/$prefix/$(basename $2)

cp ssdv.jpg $2

