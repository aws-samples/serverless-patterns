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

import sys
from typing import Tuple

from .client import OpenSearch as OpenSearch
from .connection import AsyncHttpConnection as AsyncHttpConnection
from .connection import Connection as Connection
from .connection import RequestsHttpConnection as RequestsHttpConnection
from .connection import Urllib3HttpConnection as Urllib3HttpConnection
from .connection import connections as connections
from .connection_pool import ConnectionPool as ConnectionPool
from .connection_pool import ConnectionSelector as ConnectionSelector
from .connection_pool import RoundRobinSelector as RoundRobinSelector
from .exceptions import AuthenticationException as AuthenticationException
from .exceptions import AuthorizationException as AuthorizationException
from .exceptions import ConflictError as ConflictError
from .exceptions import ConnectionError as ConnectionError
from .exceptions import ConnectionTimeout as ConnectionTimeout
from .exceptions import IllegalOperation as IllegalOperation
from .exceptions import ImproperlyConfigured as ImproperlyConfigured
from .exceptions import NotFoundError as NotFoundError
from .exceptions import OpenSearchDeprecationWarning as OpenSearchDeprecationWarning
from .exceptions import OpenSearchDslException as OpenSearchDslException
from .exceptions import OpenSearchException as OpenSearchException
from .exceptions import OpenSearchWarning as OpenSearchWarning
from .exceptions import RequestError as RequestError
from .exceptions import SerializationError as SerializationError
from .exceptions import SSLError as SSLError
from .exceptions import TransportError as TransportError
from .exceptions import UnknownDslObject as UnknownDslObject
from .exceptions import ValidationException as ValidationException
from .helpers.aggs import A as A
from .helpers.analysis import Analyzer, CharFilter, Normalizer, TokenFilter, Tokenizer
from .helpers.document import Document as Document
from .helpers.document import InnerDoc as InnerDoc
from .helpers.document import MetaField as MetaField
from .helpers.faceted_search import DateHistogramFacet as DateHistogramFacet
from .helpers.faceted_search import Facet as Facet
from .helpers.faceted_search import FacetedResponse as FacetedResponse
from .helpers.faceted_search import FacetedSearch as FacetedSearch
from .helpers.faceted_search import HistogramFacet as HistogramFacet
from .helpers.faceted_search import NestedFacet as NestedFacet
from .helpers.faceted_search import RangeFacet as RangeFacet
from .helpers.faceted_search import TermsFacet as TermsFacet
from .helpers.field import Binary as Binary
from .helpers.field import Boolean as Boolean
from .helpers.field import Byte as Byte
from .helpers.field import Completion as Completion
from .helpers.field import CustomField as CustomField
from .helpers.field import Date as Date
from .helpers.field import DateRange as DateRange
from .helpers.field import DenseVector as DenseVector
from .helpers.field import Double as Double
from .helpers.field import DoubleRange as DoubleRange
from .helpers.field import Field as Field
from .helpers.field import Float as Float
from .helpers.field import FloatRange as FloatRange
from .helpers.field import GeoPoint as GeoPoint
from .helpers.field import GeoShape as GeoShape
from .helpers.field import HalfFloat as HalfFloat
from .helpers.field import Integer as Integer
from .helpers.field import IntegerRange as IntegerRange
from .helpers.field import Ip as Ip
from .helpers.field import IpRange as IpRange
from .helpers.field import Join as Join
from .helpers.field import Keyword as Keyword
from .helpers.field import Long as Long
from .helpers.field import LongRange as LongRange
from .helpers.field import Murmur3 as Murmur3
from .helpers.field import Nested as Nested
from .helpers.field import Object as Object
from .helpers.field import Percolator as Percolator
from .helpers.field import RangeField as RangeField
from .helpers.field import RankFeature as RankFeature
from .helpers.field import RankFeatures as RankFeatures
from .helpers.field import ScaledFloat as ScaledFloat
from .helpers.field import SearchAsYouType as SearchAsYouType
from .helpers.field import Short as Short
from .helpers.field import SparseVector as SparseVector
from .helpers.field import Text as Text
from .helpers.field import TokenCount as TokenCount
from .helpers.field import construct_field as construct_field
from .helpers.function import SF as SF
from .helpers.index import Index as Index
from .helpers.index import IndexTemplate as IndexTemplate
from .helpers.mapping import Mapping as Mapping
from .helpers.query import Q as Q
from .helpers.search import MultiSearch as MultiSearch
from .helpers.search import Search as Search
from .helpers.update_by_query import UpdateByQuery as UpdateByQuery
from .helpers.utils import AttrDict as AttrDict
from .helpers.utils import AttrList as AttrList
from .helpers.utils import DslBase as DslBase
from .helpers.wrappers import Range as Range
from .serializer import JSONSerializer as JSONSerializer
from .transport import Transport as Transport

try:
    if sys.version_info < (3, 6):
        raise ImportError

    from ._async.client import AsyncOpenSearch as AsyncOpenSearch
    from ._async.http_aiohttp import AIOHttpConnection as AIOHttpConnection
    from ._async.http_aiohttp import AsyncConnection as AsyncConnection
    from ._async.transport import AsyncTransport as AsyncTransport
    from .helpers import AWSV4SignerAsyncAuth as AWSV4SignerAsyncAuth
    from .helpers import AWSV4SignerAuth as AWSV4SignerAuth
except (ImportError, SyntaxError):
    pass

VERSION: Tuple[int, int, int]
__version__: Tuple[int, int, int]
__versionstr__: str
