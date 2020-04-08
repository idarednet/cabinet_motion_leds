# You may amend and distribute as you like, but don't remove this header!
# All rights reserved.
# This is an Open Source project provided under the
# GNU General Public License (GPL) as published by the 
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#
# The GNU General Public License can be viewed at http://www.opensource.org/licenses/gpl-license.php
# If you unfamiliar with this license or have questions about it, here is an http://www.gnu.org/licenses/gpl-faq.html
# The code for this project may be used and redistributed by any means PROVIDING it is 
# not sold for profit without the author's written consent, and providing that this notice 
# and the author's name and all copyright notices remain intact.
# 
# All code and executables are provided "as is" with no warranty either express or implied. 
# The author accepts no liability for any damage or loss of business that this product may cause.
#
# AUTHOR : IDAREDNET
# DATE   : APRIL 8 2020
# LIB    : ADAFRUIT-CIRCUITPYTHON-BUNDLE-5.X (neopixel.mpy)
# HW     : TRINKET M0, STRIP OF 100 RGB 5050 LEDS, EXTERNAL 5VDC P/S, Grove PIR Motion Sensor

import time
import board
import digitalio
import neopixel

PIXEL_PIN = board.D4  # PIN DIN IS CONNECTED TO
NUM_PIXELS = 100      # NUMBER OF LEDS IN STRIP
ORDER = neopixel.RGB  # ORDER OF COLORS
PIR = digitalio.DigitalInOut(board.D3)      # PIN PIR IS CONNECTED TO
PIR.direction = digitalio.Direction.INPUT   # PIR IS A DIGITAL INPUT
ACTIVATED = False     # CODE LOGIC FOR FADING LEDS IN AND OUT
OFFSET = 0            # OFFSET WHEN FADING OUT TO FADING IN

pixels = neopixel.NeoPixel(PIXEL_PIN, NUM_PIXELS, auto_write=False, pixel_order=ORDER)

def FadeIn(color, fade_delay, offset):
    """ FadeIn(color, fade_delay, offset)
    Upon detection of movement from a PIR,
    slowly increases the brightness of a specified color
    of a determined length 5050 led strip

    Parameters
    ----------
    color : list
        list of three items that are unsigned integers
        that represent the desired color
        ie. [255,255,255] for white
    fade_delay : float
        represents the desired speed of fade
    offset : int
        unsigned integer that is set during FadeOut.
        if PIR detects movement while fading out, the
        offset is passed to FadeIn so that the transition
        from FadeOut to FadeIn is wicked smooth
    """
    for o in range(offset,255,3):
        red = (o / 256.0) * color[0]
        green = (o / 256.0) * color[1]
        blue = (o / 256.0) * color[2]
        pixels.fill((int(red),int(green),int(blue)))
        pixels.show()
        time.sleep(fade_delay)
    ACTIVATED = True
    return ACTIVATED

def FadeOut(color, fade_delay):
    """ FadeIn(color, fade_delay, offset)
    Upon no detection of movement, Slowly decreases
    the brightness of a specified color of a determined
    length 5050 led strip

    Parameters
    ----------
    color : list
        list of three items that are unsigned integers
        that represent the desired color
        ie. [255,255,255] for white
    fade_delay : float
        represents the desired speed of fade
    """
    for o in range(255,0,-3):
        red = (o / 256.0) * color[0]
        green = (o / 256.0) * color[1]
        blue = (o / 256.0) * color[2]
        pixels.fill((int(red),int(green),int(blue)))
        pixels.show()
        time.sleep(fade_delay)
        if PIR.value:
            ACTIVATED = True
            return ACTIVATED, o
    ACTIVATED = False
    return ACTIVATED, o
    
while True:
    if not ACTIVATED:
        pixels.fill((0,0,0))
        pixels.show()
    if PIR.value:
        if not ACTIVATED or (ACTIVATED and OFFSET != 0):
            ACTIVATED = FadeIn([0,0,255], 0, offset)
        time.sleep(30)
    elif ACTIVATED:
        ACTIVATED, OFFSET = FadeOut([0,0,255], 0)
    else:
        time.sleep(1)
