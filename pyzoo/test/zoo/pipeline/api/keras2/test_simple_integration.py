#
# Copyright 2018 Analytics Zoo Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import pytest
import shutil

from zoo.pipeline.api.keras2.layers import *
from zoo.pipeline.api.keras.models import *
from test.zoo.pipeline.utils.test_utils import ZooTestCase
import numpy as np

np.random.seed(1337)  # for reproducibility


class TestSimpleIntegration(ZooTestCase):

    def test_sequential(self):
        model = Sequential()
        model.add(Dense(10, kernel_initializer="glorot_uniform", input_shape=(8, )))
        model.add(Dense(12))
        input_shape = model.get_input_shape()
        output_shape = model.get_output_shape()

        np.testing.assert_allclose((8,), input_shape[1:])
        np.testing.assert_allclose((12,), output_shape[1:])


if __name__ == "__main__":
    pytest.main([__file__])
