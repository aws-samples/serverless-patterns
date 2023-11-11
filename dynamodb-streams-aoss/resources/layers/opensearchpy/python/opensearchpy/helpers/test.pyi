# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
#
# Modifications Copyright OpenSearch Contributors. See
# GitHub history for details.
#
#  Licensed to Elasticsearch B.V. under one or more contributor
#  license agreements. See the NOTICE file distributed with
#  this work for additional information regarding copyright
#  ownership. Elasticsearch B.V. licenses this file to you under
#  the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.

from typing import Any, Tuple
from unittest import TestCase

from ..client import OpenSearch

OPENSEARCH_URL: str

def get_test_client(nowait: bool = ..., **kwargs: Any) -> OpenSearch: ...
def _get_version(version_string: str) -> Tuple[int, ...]: ...

class OpenSearchTestCase(TestCase):
    @staticmethod
    def _get_client() -> OpenSearch: ...
    @classmethod
    def setup_class(cls) -> None: ...
    def teardown_method(self, _: Any) -> None: ...
    def opensearch_version(self) -> Tuple[int, ...]: ...
