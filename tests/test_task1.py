import unittest
import pytest
from unittest import TestCase
from Task1 import top_3_popular, sort_courses_by_duration, explore_relationship
from data import *


class TestTop3Popular(TestCase):
    def test_result(self):
        expected = 'Александр: 10 раз(а), Евгений: 5 раз(а), Максим: 4 раз(а)'
        result = top_3_popular(mentors)
        self.assertEqual(result, expected)

    def test_len(self):
        expected = 3
        result = len(top_3_popular(random_names).split(', '))
        self.assertEqual(result, expected)

    def test_wrong_data(self):
        with self.assertRaises(Exception):
            expected = 'Егор'
            result = top_3_popular(random_names_2)
            self.assertIn(expected, result)


class TestSortCoursesByDuration(TestCase):
    def test_list(self):
        expected = [
            'Fullstack-разработчик на Python - 12 месяцев',
            'Python-разработчик с нуля - 14 месяцев',
            'Java-разработчик с нуля - 20 месяцев',
            'Frontend-разработчик с нуля - 20 месяцев'
        ]
        result = sort_courses_by_duration(courses, durations)
        self.assertListEqual(result, expected)


class TestExploreRelationship(TestCase):
    def test_in(self):
        expected = 'Связи нет'
        result = explore_relationship(courses, mentors, durations)
        self.assertIn(expected, result)

    # Функция плохо обрабатывает курсы с одинаковой длительностью
    @unittest.expectedFailure
    def test_in_2(self):
        expected = 'Связь есть'
        result = explore_relationship(courses, mentors, durations_test)
        self.assertIn(expected, result)


@pytest.mark.parametrize(
    "dur,courses_list,expected", [
        (durations, courses, 'FuPyJaFr'),
        (durations_test, courses, 'PyFrJaFu'),
        (durations_test_2, courses, 'PyJaFuFr'),
        (durations_test_3, courses, 'FrFuJaPy')
    ]
)
def test_duration_sort(dur, courses_list, expected):
    res = ''.join([x[:2] for x in sort_courses_by_duration(courses_list, dur)])
    assert res == expected
