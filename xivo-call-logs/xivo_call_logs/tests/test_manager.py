# -*- coding: utf-8 -*-

from mock import Mock
from unittest import TestCase
from xivo_call_logs.manager import CallLogsManager
from xivo_call_logs.cel_fetcher import CELFetcher
from xivo_call_logs.generator import CallLogsGenerator
from xivo_call_logs.writer import CallLogsWriter


class TestCallLogsManager(TestCase):
    def setUp(self):
        self.cel_fetcher = Mock(CELFetcher)
        self.generator = Mock(CallLogsGenerator)
        self.writer = Mock(CallLogsWriter)
        self.manager = CallLogsManager(self.cel_fetcher, self.generator, self.writer)

    def tearDown(self):
        pass

    def test_generate(self):
        cels = self.cel_fetcher.fetch_all.return_value = [Mock(), Mock()]
        call_logs = self.generator.from_cel.return_value = [Mock(), Mock()]

        self.manager.generate()

        self.cel_fetcher.fetch_all.assert_called_once_with()
        self.generator.from_cel.assert_called_once_with(cels)
        self.writer.write.assert_called_once_with(call_logs)