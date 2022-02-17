# Copyright 1999-2021 Alibaba Group Holding Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

try:
    from pyarrow.fs import S3FileSystem as _ArrowS3FileSystem
    from .arrow import S3FileSystem

    del _ArrowS3FileSystem
except ImportError:  # pragma: no cover
    try:
        # pyarrow < 2.0.0
        from pyarrow import S3FileSystem
    except ImportError:
        S3FileSystem = None

from .core import register_filesystem


if S3FileSystem is not None:  # pragma: no branch
    register_filesystem("s3", S3FileSystem)
