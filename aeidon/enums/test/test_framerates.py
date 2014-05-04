# -*- coding: utf-8 -*-

# Copyright (C) 2005 Osmo Salomaa
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

import aeidon


class TestModule(aeidon.TestCase):

    def test_attributes(self):
        for framerate in aeidon.framerates:
            assert hasattr(framerate, "label")
            assert hasattr(framerate, "mpsub")
            assert hasattr(framerate, "value")

    def test_items(self):
        assert hasattr(aeidon.framerates, "FPS_23_976")
        assert hasattr(aeidon.framerates, "FPS_24_000")
        assert hasattr(aeidon.framerates, "FPS_25_000")
        assert hasattr(aeidon.framerates, "FPS_29_970")
