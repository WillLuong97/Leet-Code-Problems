import unittest
import insertIntervals

class TestInterInsertion(unittest.TestCase):
    def test_insert_interval(self):
        intervals = [[1,3],[6,9]]
        newInterval = [2, 5]
        result = [1,5,6,9]
        programmed_result = insertIntervals.insertIntervals(intervals, newInterval)
        self.assertEquals(programmed_result, result)
