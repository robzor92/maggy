#
#   Copyright 2020 Logical Clocks AB
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

"""
Module to encapsulate functionality related to writing to the tensorboard
log dir and programmatically structure the outputs.
"""

print("write 1337")

import tensorflow.compat.v2 as tf
from tensorboard.plugins.hparams import summary_v2 as hp
from tensorboard.plugins.hparams import api_pb2
from tensorboard.plugins.hparams import summary

# __import__("tensorflow").compat.v1.enable_eager_execution()

_tensorboard_dir = None
_writer = None


def _register(trial_dir):
    global _tensorboard_dir
    global _writer
    _tensorboard_dir = trial_dir
    _writer = tf.summary.create_file_writer(_tensorboard_dir)