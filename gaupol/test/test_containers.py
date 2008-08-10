# Copyright (C) 2008 Osmo Salomaa
#
# This file is part of Gaupol.
#
# Gaupol is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# Gaupol is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# Gaupol. If not, see <http://www.gnu.org/licenses/>.

import gaupol


class TestSubRip(gaupol.TestCase):

    def test_attributes(self):

        container = gaupol.containers.new("subrip")
        assert hasattr(container, "x1")
        assert hasattr(container, "y1")
        assert hasattr(container, "x2")
        assert hasattr(container, "y2")


class TestSubStationAlpha(gaupol.TestCase):

    def test_attributes(self):

        container = gaupol.containers.new("ssa")
        assert hasattr(container, "marked")
        assert hasattr(container, "layer")
        assert hasattr(container, "style")
        assert hasattr(container, "name")
        assert hasattr(container, "margin_l")
        assert hasattr(container, "margin_r")
        assert hasattr(container, "margin_v")
        assert hasattr(container, "effect")


class TestModule(gaupol.TestCase):

    def test_new__value_error(self):

        self.raises(ValueError, gaupol.containers.new, "xxx")