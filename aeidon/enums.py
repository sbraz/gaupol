# -*- coding: utf-8 -*-

# Copyright (C) 2016 Osmo Salomaa
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Miscellanous enumerations."""

import aeidon
import os
import sys

from aeidon.i18n import _

__all__ = [
    "align_methods",
    "documents",
    "formats",
    "framerates",
    "modes",
    "newlines",
    "players",
    "registers",
]


class AlignMethodNumber(aeidon.EnumerationItem):
    label = _("Subtitle number")

class AlignMethodPosition(aeidon.EnumerationItem):
    label = _("Subtitle position")

align_methods = aeidon.Enumeration()
align_methods.NUMBER = AlignMethodNumber()
align_methods.POSITION = AlignMethodPosition()


class DocumentMain(aeidon.EnumerationItem): pass
class DocumentTranslation(aeidon.EnumerationItem): pass

documents = aeidon.Enumeration()
documents.MAIN = DocumentMain()
documents.TRAN = DocumentTranslation()


class Framerate23976(aeidon.EnumerationItem):
    label = _("23.976 fps")
    value = 24 / 1.001

class Framerate24000(aeidon.EnumerationItem):
    label = _("24.000 fps")
    value = 24.0

class Framerate25000(aeidon.EnumerationItem):
    label = _("25.000 fps")
    value = 25.0

class Framerate29970(aeidon.EnumerationItem):
    label = _("29.970 fps")
    value = 30 / 1.001

framerates = aeidon.Enumeration()
framerates.FPS_23_976 = Framerate23976()
framerates.FPS_24_000 = Framerate24000()
framerates.FPS_25_000 = Framerate25000()
framerates.FPS_29_970 = Framerate29970()


class ModeTime(aeidon.EnumerationItem): pass
class ModeFrame(aeidon.EnumerationItem): pass
class ModeSeconds(aeidon.EnumerationItem): pass

modes = aeidon.Enumeration()
modes.TIME = ModeTime()
modes.FRAME = ModeFrame()
modes.SECONDS = ModeSeconds()


class NewlinesMac(aeidon.EnumerationItem):
    label = _("Mac (classic)")
    value = "\r"

class NewlinesUnix(aeidon.EnumerationItem):
    label = "Unix"
    value = "\n"

class NewlinesWindows(aeidon.EnumerationItem):
    label = "Windows"
    value = "\r\n"

newlines = aeidon.Enumeration()
newlines.MAC = NewlinesMac()
newlines.UNIX = NewlinesUnix()
newlines.WINDOWS = NewlinesWindows()


def _get_mplayer_executable():
    if sys.platform == "win32":
        directory = os.environ.get("PROGRAMFILES", "C:\\Program Files")
        path = os.path.join(directory, "MPlayer", "mplayer.exe")
        return aeidon.util.shell_quote(path)
    return "mplayer"

def _get_mpv_executable():
    if sys.platform == "win32":
        directory = os.environ.get("PROGRAMFILES", "C:\\Program Files")
        path = os.path.join(directory, "MPV", "mpv.exe")
        return aeidon.util.shell_quote(path)
    return "mpv"

def _get_vlc_executable():
    if sys.platform == "win32":
        directory = os.environ.get("PROGRAMFILES", "C:\\Program Files")
        path = os.path.join(directory, "VideoLAN", "VLC", "vlc.exe")
        return aeidon.util.shell_quote(path)
    return "vlc"

class PlayerMPlayer(aeidon.EnumerationItem):
    command = " ".join((_get_mplayer_executable(),
                        "-quiet",
                        "-identify",
                        "-osdlevel 2",
                        "-ss $SECONDS",
                        "-slang",
                        "-noautosub",
                        "-sub $SUBFILE",
                        "$VIDEOFILE",))

    if sys.platform != "win32":
        # Required for mplayer to work if gaupol was started
        # as a background process (&) from a terminal window.
        # http://www.mplayerhq.hu/DOCS/HTML/en/faq.html#idp11051520
        command = "{} < /dev/null".format(command)

    command_utf_8 = " ".join((_get_mplayer_executable(),
                              "-quiet",
                              "-osdlevel 2",
                              "-ss $SECONDS",
                              "-slang",
                              "-noautosub",
                              "-sub $SUBFILE",
                              "-utf8",
                              "$VIDEOFILE",))

    if sys.platform != "win32":
        # Required for mplayer to work if gaupol was started
        # as a background process (&) from a terminal window.
        # http://www.mplayerhq.hu/DOCS/HTML/en/faq.html#idp11051520
        command_utf_8 = "{} < /dev/null".format(command_utf_8)

    label = "MPlayer"

class PlayerMPV(aeidon.EnumerationItem):
    command = " ".join((_get_mpv_executable(),
                        "--quiet",
                        "--osd-level=2",
                        "--hr-seek=yes",
                        "--start=$SECONDS",
                        "--sub-file=$SUBFILE",
                        "$VIDEOFILE",))

    command_utf_8 = " ".join((_get_mpv_executable(),
                              "--quiet",
                              "--osd-level=2",
                              "--hr-seek=yes",
                              "--start=$SECONDS",
                              "--sub-file=$SUBFILE",
                              "--sub-codepage=utf-8:utf-8-broken",
                              "$VIDEOFILE",))

    label = "mpv"

class PlayerVLC(aeidon.EnumerationItem):
    command = " ".join((_get_vlc_executable(),
                        "$VIDEOFILE",
                        ":start-time=$SECONDS",
                        ":sub-file=$SUBFILE",))

    command_utf_8 = " ".join((_get_vlc_executable(),
                              "$VIDEOFILE",
                              ":start-time=$SECONDS",
                              ":sub-file=$SUBFILE",
                              ":subsdec-encoding=UTF-8",))

    label = "VLC"

players = aeidon.Enumeration()
players.MPLAYER = PlayerMPlayer()
players.MPV = PlayerMPV()
players.VLC = PlayerVLC()


class RegisterDo(aeidon.EnumerationItem):
    shift = 1
    signal = "action-done"

class RegisterUndo(aeidon.EnumerationItem):
    shift = -1
    signal = "action-undone"

class RegisterRedo(aeidon.EnumerationItem):
    shift = 1
    signal = "action-redone"

registers = aeidon.Enumeration()
registers.DO = RegisterDo()
registers.UNDO = RegisterUndo()
registers.REDO = RegisterRedo()


class FormatAdvSubStationAlpha(aeidon.EnumerationItem):
    container = "ssa"
    extension = ".ass"
    has_header = True
    identifier = r"^ScriptType:\s*[vV]4.00\+\s*$"
    label = "Advanced Sub Station Alpha"
    mime_type = "text/x-ssa"
    mode = modes.TIME

class FormatLRC(aeidon.EnumerationItem):
    container = None
    extension = ".lrc"
    has_header = True
    identifier = r"^\[-?\d\d:\d\d\.\d\d\]"
    label = "LRC"
    mime_type = "text/plain"
    mode = modes.TIME

class FormatMicroDVD(aeidon.EnumerationItem):
    container = None
    extension = ".sub"
    has_header = True
    identifier = r"^\{-?\d+\}\{-?\d+\}"
    label = "MicroDVD"
    mime_type = "text/x-microdvd"
    mode = modes.FRAME

class FormatMPL2(aeidon.EnumerationItem):
    container = None
    extension = ".txt"
    has_header = False
    identifier = r"^\[-?\d+\]\[-?\d+\]"
    label = "MPL2"
    mime_type = "text/plain"
    mode = modes.TIME

class FormatSubRip(aeidon.EnumerationItem):
    container = "subrip"
    extension = ".srt"
    has_header = False
    identifier = (r"^-?\d\d:\d\d:\d\d,\d\d\d -->"
                  r" -?\d\d:\d\d:\d\d,\d\d\d"
                  r"(  X1:\d+ X2:\d+ Y1:\d+ Y2:\d+)?\s*$")

    label = "SubRip"
    mime_type = "application/x-subrip"
    mode = modes.TIME

class FormatSubStationAlpha(aeidon.EnumerationItem):
    container = "ssa"
    extension = ".ssa"
    has_header = True
    identifier = r"^ScriptType:\s*[vV]4.00\s*$"
    label = "Sub Station Alpha"
    mime_type = "text/x-ssa"
    mode = modes.TIME

class FormatSubViewer2(aeidon.EnumerationItem):
    container = None
    extension = ".sub"
    has_header = True
    identifier = (r"^-?\d\d:\d\d:\d\d\.\d\d"
                  r",-?\d\d:\d\d:\d\d\.\d\d\s*$")

    label = "SubViewer 2.0"
    mime_type = "text/x-subviewer"
    mode = modes.TIME

class FormatTMPlayer(aeidon.EnumerationItem):
    container = None
    extension = ".txt"
    has_header = False
    identifier = r"^-?\d?\d:\d\d:\d\d:"
    label = "TMPlayer"
    mime_type = "text/plain"
    mode = modes.TIME

class FormatWebVTT(aeidon.EnumerationItem):
    container = "webvtt"
    extension = ".vtt"
    has_header = True
    identifier = r"^\s*[wW][eE][bB][vV][tT][tT]\b"
    label = "WebVTT"
    mime_type = "text/vtt"
    mode = modes.TIME

formats = aeidon.Enumeration()
formats.ASS = FormatAdvSubStationAlpha()
formats.LRC = FormatLRC()
formats.MICRODVD = FormatMicroDVD()
formats.MPL2 = FormatMPL2()
formats.SUBRIP = FormatSubRip()
formats.SSA = FormatSubStationAlpha()
formats.SUBVIEWER2 = FormatSubViewer2()
formats.TMPLAYER = FormatTMPlayer()
formats.WEBVTT = FormatWebVTT()
