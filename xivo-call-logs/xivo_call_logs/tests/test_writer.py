# -*- coding: utf-8 -*-

# Copyright (C) 2013 Avencall
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

from mock import Mock, patch
from unittest import TestCase

from xivo_call_logs.writer import CallLogsWriter


class TestCallLogsWriter(TestCase):
    def setUp(self):
        self.writer = CallLogsWriter()

    def tearDown(self):
        pass

    @patch('xivo_dao.data_handler.call_log.dao.create_all')
    def test_write(self, mock_call_logs_dao):
        call_logs = [Mock(), Mock()]

        self.writer.write(call_logs)

        mock_call_logs_dao.assert_called_once_with(call_logs)