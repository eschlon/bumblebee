import pytest

from bumblebee import Transformer

testObj = {
    'name': {
        'first': 'Terry',
        'last': 'Gilliam'
    },
    'nationality': 'British',
    'birthDate': '11-22-1940',
    'films': [
        {
            'title': 'Time Bandits',
            'year': 1981
        },
        {
            'title': 'Brazil',
            'year': 1985
        }
    ],
    'occupations': [
        'actor',
        'animator',
        'comedian',
        'director',
        'producer',
        'screenwriter'
    ]
}

scenarios = {
    "simpleString": (
        """
        nat:
          type: string
          !src: $.nationality
        """,
        testObj,
        {'nat': 'British'}
    ),
    "simpleObj": (
        """
        fullName:
          type: object
          !src: $.name
          properties:
            first: {'type': 'string'}
            last: {'type': 'string'}
        """,
        testObj,
        {'fullName': {'first': 'Terry', 'last': 'Gilliam'}}
    ),
    'simpleArray': (
        """
        jobs:
          type: array
          !src: $.occupations
          items: {'type': 'string'}
        """,
        testObj,
        {'jobs': ['actor', 'animator', 'comedian', 'director', 'producer', 'screenwriter']}
    ),
    'simpleSlice': (
        """
        jobs:
          type: array
          !src: $.occupations.[:2]
          items: {'type': 'string'}
        """,
        testObj,
        {'jobs': ['actor', 'animator']}
    ),
    'simpleSelect': (
        """
        job:
          type: string
          !src: $.occupations.[0]
        """,
        testObj,
        {'job': 'actor'}
    ),
    'simpleUnwind': (
        """
        titles:
          type: array
          !src: $.films.[*].title
          items: {'type': 'string'}
        """,
        testObj,
        {'titles': ['Time Bandits', 'Brazil']}
    ),
    'simpleFn': (
        """
        fullName:
          type: string
          !src: $.name
          !fnc: lambda name: ' '.join(name.values())
        """,
        testObj,
        {'fullName': 'Terry Gilliam'}
    )
}


class TestTransformer(object):

    @pytest.mark.parametrize('manifest,record,result', list(scenarios.values()), ids=list(scenarios.keys()))
    def test_transform(self, manifest, record, result):
        t = Transformer(manifest)
        assert t(record) == result




