from training.lib.training_set_base import TrainingSetBase


class CallableTrainingSet(TrainingSetBase):
    """
    An iterator defining the training set for a brain, based on an appropriate
    Callable. For example, given binary functions such as f(x) =  x (identity)
    and f(x, y) = (x + y) % 2, appropriate Callables for example are
    lambda x: x and lambda x: bin(x)[2:].count('1') % 2 (respectively).
    Importantly, the inputs of the Callable are considered to be integers from
    the interval [0, 2^domain_size-1].
    """
    def __init__(self, function, domain_size, noise_probability=0.) -> None:
        super().__init__(noise_probability=noise_probability)
        self._function = function
        self._domain_size = domain_size
        self._value = -1

    @property
    def domain_size(self):
        return self._domain_size

    @property
    def current_input_value(self):
        return self._value

    def _next(self):
        if self._value == 2 ** self._domain_size - 1:
            raise StopIteration()

        self._value += 1
        return self._function(self._value)
