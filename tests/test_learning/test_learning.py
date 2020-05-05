from learning.data_set.constructors import create_data_set_from_list
from learning.learning_task import Learning
from tests.test_learning.learning_test_base import LearningTestBase


class TestLearning(LearningTestBase):

    def test_learning_sanity(self):
        learning = Learning(brain=self.brain, domain_size=2)
        data_set = create_data_set_from_list([0, 1, 0, 1])

        learning.sequence = self.sequence
        learning.training_set = data_set

        model = learning.create_model(number_of_sequence_cycles=50)
        test_results = model.test_model(data_set)
        self.assertEqual(1, test_results.accuracy)

    def test_learning_with_two_separated_models_sanity(self):
        learning = Learning(brain=self.brain, domain_size=2)
        learning.sequence = self.sequence

        data_set1 = create_data_set_from_list([0, 1, 0, 1])
        learning.training_set = data_set1
        model1 = learning.create_model(number_of_sequence_cycles=50)

        data_set2 = create_data_set_from_list([1, 0, 1, 0])
        learning.training_set = data_set2
        model2 = learning.create_model(number_of_sequence_cycles=50)

        # Models have been trained with opposite data, so we expect different results
        self.assertNotEqual(model1.run_model(0), model2.run_model(0))
        self.assertNotEqual(model1.run_model(1), model2.run_model(1))
        self.assertNotEqual(model1.run_model(2), model2.run_model(2))
        self.assertNotEqual(model1.run_model(3), model2.run_model(3))