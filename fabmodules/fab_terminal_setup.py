
'''
We want to use the weaver fab lib to run a basic install, on my laptop, of the terminal settings defined in here.

I have a libary of functions in fedorafab, that I can use to write 
files to the (remote) laptop, and also setup and configure as needed.

Its all here bar the fat lady singing.
'''


BASE_TMPL = '''
!-------------------------------------------------------------------------------
! Xft settings
!-------------------------------------------------------------------------------

Xft.dpi:                    96
Xft.antialias:              false
Xft.rgba:                   rgb
Xft.hinting:                true
Xft.hintstyle:              hintslight

!-------------------------------------------------------------------------------
! URxvt settings
! Colours lifted from Solarized (http://ethanschoonover.com/solarized)
! More info at:
! http://pod.tst.eu/http://cvs.schmorp.de/rxvt-unicode/doc/rxvt.1.pod
!-------------------------------------------------------------------------------

URxvt.depth:                32
URxvt.geometry:             90x30
URxvt.transparent:          false
URxvt.fading:               0
! URxvt.urgentOnBell:         true
! URxvt.visualBell:           true
URxvt.loginShell:           true
URxvt.saveLines:            50
URxvt.internalBorder:       3
URxvt.lineSpace:            0

! Fonts
URxvt.allow_bold:           false
/* URxvt.font:                 -*-terminus-medium-r-normal-*-12-120-72-72-c-60-iso8859-1 */
URxvt*font: -*-terminus-*-*-*-*-32-*-*-*-*-*-*-*
URxvt*boldFont: -*-terminus-*-*-*-*-32-*-*-*-*-*-*-*

! Fix font space
URxvt*letterSpace: -1

! Scrollbar
URxvt.scrollStyle:          rxvt
URxvt.scrollBar:            false

! Perl extensions
URxvt.perl-ext-common:      default,matcher
URxvt.matcher.button:       1
URxvt.urlLauncher:          firefox

! Cursor
URxvt.cursorBlink:          true
URxvt.cursorColor:          #657b83
URxvt.cursorUnderline:      false

! Pointer
URxvt.pointerBlank:         true

!!Source http://github.com/altercation/solarized

*background: #002b36
*foreground: #657b83
!!*fading: 40
*fadeColor: #002b36
*cursorColor: #93a1a1
*pointerColorBackground: #586e75
*pointerColorForeground: #93a1a1

!! black dark/light
*color0: #073642
*color8: #002b36

!! red dark/light
*color1: #dc322f
*color9: #cb4b16

!! green dark/light
*color2: #859900
*color10: #586e75

!! yellow dark/light
*color3: #b58900
*color11: #657b83

!! blue dark/light
*color4: #268bd2
*color12: #839496

!! magenta dark/light
*color5: #d33682
*color13: #6c71c4

!! cyan dark/light
*color6: #2aa198
*color14: #93a1a1

!! white dark/light
*color7: #eee8d5
*color15: #fdf6e3

'''

from fabmodules import fedorafab
from fabmodules.fedorafab import run, sudo

__all__ = ['install_all',]

def install_all():
    setup_xterm()
    install_terminal()
    install_fonts()
    
def setup_xterm():
    """xrdb is of course and X program so needs to display out to a DISPLAY. 
    I fake one, in the same env as the call is made
    I prob need to look at env var in fabric
    """
    remote_path = '/home/pbrian/.Xresources'
    fedorafab.replace_remote_file(remote_path, BASE_TMPL)
    run('export DISPLAY=:0;xrdb {0} > /dev/null;echo $DISPLAY'.format(remote_path))

def install_terminal():
    """
    Using uxrvt
    """
    pkgs = ['rxvt-unicode-256color',
            'xorg-x11-apps']
    for pkg in pkgs:
        sudo("dnf install -y %s " % pkg)
        
def install_fonts():
    """
    I want to install inconsolata or similar
    """
    
    sudo("yum install -y levien-inconsolata-fonts.noarch")
    sudo("yum install -y google-droid-sans-mono-fonts.noarch")
    sudo("fc-cache -fv") # refresh the cache of fonts    
    #edit .emacs?
    #(set-default-font "Inconsolata-12")
    #But I need to make it available
# install python3
# sudo apt-get install python3 python3-pip
# install python from apt ????
# from source, but ??? wheels first...
