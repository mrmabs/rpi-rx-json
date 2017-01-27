Raspberry Pi Direct Conversion RX JSON Remote
======

A simple python web JSON receiver to change the frequency of a direct conversion receiver hooked up the the GPIO pin. Currently the JSON receiver will return either the frequency in hertz (Hz) or "No freq"; this will change to a more appropriate output at version 1.0.

The steps I did to get this working:

1. Installed Raspbian Jesse Lite (the version I used: 2017-01-11)
  * manually configured networking (in my case adding my wifi network to the wpa supplicant conf file, see: [Debian: WPA Supplicant](https://wiki.debian.org/WiFi/HowToUse#wpa_supplicant))
  * Did an update: 
    * `sudo apt-get update`
    * `sudo apt-get upgrade`
  * Installed git: `sudo apt-get install git`

2. Download PiVFO: https://github.com/JennyList/LanguageSpy/tree/master/RaspberryPi/rf/freq_pi
  * I compiled and installed (copied) the freq_pi binary to /usr/local/bin/: `sudo cp freq_pi /usr/local/bin/`

3. Installed the lighttpd web server: `sudo apt-get install lighttpd`
  * Enabled cgi scripting: `sudo lighty-enable-mod cgi`
  * Added `cgi.execute-x-only = "enable"` to the cgi conf file (`/etc/lighttpd/conf-enabled/10-cgi.conf`)

6. So that the JSON receiver can call the binary, you will need to add a line to your sudoers file, for example:
  * `www-data ALL = NOPASSWD: /usr/local/bin/freq_pi`
  * This is basically saying thet the user www-data, which is the webserver user, can execute the binary without needing a password. (This is a potential security issue, but I have tried my best to sanitise the input into Python.)

7. Create a 'cgi-bin' directory under /var/www/html: `sudo mkdir /var/www/html/cgi-bin`
  * Change to the directory `cd /var/www/html/cgi-bin`
  * Download at leas the JSON receiver:
    * `sudo wget https://raw.githubusercontent.com/mrmabs/rpi-rx-json/master/set-rx.py`
  * Also download the HTML generator (if you don't have something to set the frequency for you):
    * `sudo wget https://raw.githubusercontent.com/mrmabs/rpi-rx-json/master/send-json.html`
