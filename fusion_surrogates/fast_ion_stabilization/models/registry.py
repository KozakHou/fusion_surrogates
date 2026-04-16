# Copyright 2026 DeepMind Technologies Limited.
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

"""Registry of paths for fast ion stabilization models."""

import importlib.resources
import pathlib

import immutabledict

DEFAULT_MODELS = immutabledict.immutabledict({
    'H': 'fast_ion_H_v1',
    'He3': 'fast_ion_He3_v1',
})

MODELS = immutabledict.immutabledict({
    'fast_ion_H_v1': f'{pathlib.Path(__file__).parent}/fast_ion_H_v1.fistab',
    'fast_ion_He3_v1': (
        f'{pathlib.Path(__file__).parent}/fast_ion_He3_v1.fistab'
    ),
})


def get_model_resource(model_name: str) -> importlib.resources.abc.Traversable:
  """Returns the packaged resource for a registered fast-ion model."""
  model_resource = MODELS.get(model_name)
  if model_resource is None:
    raise ValueError(f'Model {model_name} not found in registry.')
  return importlib.resources.files(__package__).joinpath(
      pathlib.Path(model_resource).name
  )
