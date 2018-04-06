"""Collection of hyper parameters."""


import tensorflow as tf
import numpy as np

from s_labels import num_classes


# Constants describing the training process.
tf.flags.DEFINE_integer('batch_size', 1,
                        """(Maximum) Number of samples within a batch.""")

NUM_EPOCHS_PER_DECAY = 9.0          # Number of epochs after which learning rate decays.
LEARNING_RATE_DECAY_FACTOR = 0.50   # Learning rate decay factor.
INITIAL_LEARNING_RATE = 0.001       # Initial learning rate.
NUM_HIDDEN_LSTM = 128               # Number of hidden units per LSTM cell.
NUM_LAYERS_LSTM = 4                 # Number of BDLSTM layers.


# Logging & Output
tf.flags.DEFINE_integer('max_steps', 1000000,
                        """Number of batches to run.""")
tf.flags.DEFINE_integer('log_frequency', 101,
                        """How often (every x steps) to log results to the console.""")

# Miscellaneous & Data set
tf.flags.DEFINE_integer('sampling_rate', 16000,
                        """The sampling rate of the audio files (2 * 8kHz).""")
tf.flags.DEFINE_boolean('log_device_placement', False,
                        """Whether to log device placement.""")
tf.flags.DEFINE_string('train_dir', '/tmp/s_train',
                       """Directory where to write event logs and checkpoints.""")
tf.flags.DEFINE_integer('num_examples_train', 4620,
                        """Number of examples in the training set.""")
tf.flags.DEFINE_integer('num_examples_test', 1680,
                        """Number of examples in the testing/evaluation set.""")
NUM_CLASSES = num_classes()
TF_FLOAT = tf.float32   # ctc_xxxx functions don't support float64. See #13
NP_FLOAT = np.float32   # ctc_xxxx functions don't support float64. See #13


# Export names.
FLAGS = tf.flags.FLAGS