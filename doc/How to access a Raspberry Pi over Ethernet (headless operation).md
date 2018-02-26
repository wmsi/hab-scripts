How to access a Raspberry Pi over Ethernet (headless operation)

# First Steps

1. Make sure you have configured the Raspberry Pi network interfaces correctly.

This involves confirming the configuration in /etc/network/interfaces (run sudo nano /etc/network/interfaces) contains only these lines with reference to eth0 (remove any that reference eth0 elsewhere):

	auto eth0

	allow-hotplug eth0

	iface eth0 inet dhcp # this line is optional

2. **Determine the hostname of your Raspberry Pi. **The easiest way is simply to look at the terminal prompt (ex. pi@<HOSTNAME>), or execute this command: cat /etc/hostname

	**From now on, this hostname will be referred to as**** <HOSTNAME>**

3. Plug an ethernet cable into the Pi’s port

4. Plug the other end into your computer. This may require a Ethernet->USB or Ethernet->Thunderbolt adapter if your computer doesn’t have a dedicated Ethernet plug.

# Mac

1. If something about a new network interface pops up, click on its button to go to Network settings

2. Otherwise, open up the Network settings by clicking on the Apple icon in the upper left, and going to **System Preferences->Network**

3. Find the interface that is the one you’re using with the ethernet cable. It may help to unplug and replug the cable and dongle and see which one’s "**Status**" goes to “**Cable Unplugged**.” You’ll likely be able to see easily.

<table>
  <tr>
    <td></td>
  </tr>
  <tr>
    <td>The interface with the cable unplugged</td>
  </tr>
</table>


    1. Make sure that this network interface is set to "**Using DHCP**" under “**Configure IPV4**”

    2. You should see it turn yellow with the message "**Self-Assigned IP**" once it’s all set

<table>
  <tr>
    <td></td>
  </tr>
  <tr>
    <td>The interface with the cable and Pi connected</td>
  </tr>
</table>


**NOTE: The above won’t be necessary on subsequent times; just unplug and replug the cable to jog things if need be.**

4. Open up a terminal through the application search.

	i.e. press **Command+Spacebar **and start typing "**Terminal**" then open the application

5. Once you’ve opened the terminal, execute **ssh pi@<HOSTNAME>.local**

**Enter your password** when prompted (saying **yes** to any "Add unknown host" prompt) , and you should be logged in!

# Windows

You will need to install an SSH client called **PUTTY**. Go to [https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) and download the installer under "**MSI (‘Windows Installer’)**"

Note: looking online, there are several ways people say to do this, but this method most often works for the author on Windows 10.

1. Right click on your **Wifi/Network icon **in the lower right hand corner and select "**Open Network and Sharing Center**"

2. Click "**Change Adapter Settings**" on the left

3. Find your wireless network interface (ex. "**Wi-Fi**"), right click on it, then select “**Properties**”

4. In the tabs that show up, select the "**Sharing**" tab. 

5. Check the "**Allow other network users to connect through this...**" box and select your *ethernet interface* in the “**Home networking connection**” dropdown (ex. “**Ethernet 1**”)

    1. You can determine the ethernet interface by plugging/unplugging the cable to see which one either appears/disappears OR says "**Network cable unplugged**" vs. “**Identifying...**”

    2. **If it is already selected**, deselect it, close the dialog, and **repeat** as if it wasn’t selected in the first place.

    3. *This will also share your computer’s internet connection with the Pi (if you’re connected to wifi)*

<table>
  <tr>
    <td></td>
  </tr>
  <tr>
    <td>Configuring the "Wi-Fi" interface</td>
  </tr>
</table>


<table>
  <tr>
    <td></td>
  </tr>
  <tr>
    <td>Appearance of network interfaces when correctly configured</td>
  </tr>
</table>


6. Click Save and close all the dialogs/windows.

**NOTE: The above ****_probably _****won’t be necessary on subsequent times; just unplug and replug the cable to jog things if need be. **

**However, if ****you want to get internet from your ethernet adapter****, you’ll have to reverse this process to disable it**

7. Open **PUTTY.**

8. Type in **pi@<HOSTNAME.mshome.net** as the address (NOTE the different suffix!)

    4. If **.mshome.net** doesn’t work, you can try **.local**. This can depend on the particulars of your setup.

9. Hit enter, enter your password, and you should be logged in!

# Linux (Ubuntu)

1. Click on your **Wifi/Network icon** in the top right corner, and go to "**Edit Connections**"

2. Select "**Wired Connection 1**" (or “Wired Connection X”, whichever one you’re using for the ethernet connection) and then hit “**Edit**”

3. Go the "**IPV4 Settings**" tab and set “**Method**” to either “**Automatic (DHCP)**” or “**Shared to other computers**” (*both work, and also share your computer’s internet connection (if you’re connected to wifi), with the Pi*).

<table>
  <tr>
    <td></td>
  </tr>
  <tr>
    <td>The configuration windows, with the connection set up correctly</td>
  </tr>
</table>


**NOTE: The above won’t be necessary on subsequent times; just unplug and replug the cable to jog things if need be.**

4. Open up a terminal through either the application search (dash) or by hitting **Ctrl+Alt+T**.

5. Once you’ve opened the terminal, execute **ssh pi@<HOSTNAME>.local**

**Enter your password** when prompted (saying **yes** to any "Add unknown host" prompt) , and you should be logged in!

# SSH Troubleshooting

* *Occasionally you might get a very urgent error about "host authentication has changed." This just happens because your computer expects the Pi to be coming from a certain IP, but that IP has changed, so it fears foul play. *

	

To solve this issue, **simply read through the output and run the command they tell you to **run to remove your computer’s memory of the Pi’s IP address so it doesn’t throw the error.

