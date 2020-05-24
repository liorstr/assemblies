from learning.components.data_set.constructors import create_data_set_from_list
from learning.components.errors import DomainSizeMismatch

from learning.components.model import LearningModel
from tests.test_components.learning_component_test_base import LearningComponentTestBase


class TestLearningModel(LearningComponentTestBase):

    def test_run_model_sanity(self):
        model = LearningModel(brain=self.brain, sequence=self.sequence, input_stimuli=self.input_stimuli)
        self.assertIn(model.run_model(0), [0, 1])
        self.assertIn(model.run_model(1), [0, 1])
        self.assertIn(model.run_model(2), [0, 1])
        self.assertIn(model.run_model(3), [0, 1])
        self.assertRaises(DomainSizeMismatch, model.run_model, 4)

    def test_run_model_consistency(self):
        model = LearningModel(brain=self.brain, sequence=self.sequence, input_stimuli=self.input_stimuli)

        result_00 = model.run_model(0)
        result_11 = model.run_model(3)

        result_00_2 = model.run_model(0)
        result_11_2 = model.run_model(3)

        self.assertEqual(result_11, result_11_2)
        self.assertEqual(result_00, result_00_2)

    def test_train_model_sanity(self):
        model = LearningModel(brain=self.brain, sequence=self.sequence, input_stimuli=self.input_stimuli)

        training_set = create_data_set_from_list([0, 1, 0, 1])

        model.train_model(training_set, number_of_sequence_cycles=50)
        test_results = model.test_model(training_set)
        self.assertEqual(1, test_results.accuracy)
        self.assertEqual([], test_results.false_negative)
        self.assertEqual([0, 1, 2, 3], test_results.true_positive)
