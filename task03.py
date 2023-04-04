def test_filter():
    f = Filter([lambda x: x % 2 == 0, lambda x: x > 0, lambda x: isinstance(x, int)])
    assert f.apply(range(100)) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]

def test_make_filter():
    f = make_filter(name='polly', type='bird')
    assert f.apply(sample_data) == [{
         "is_dead": True,
         "kind": "parrot",
         "type": "bird",
         "name": "polly"
     }]

    f = make_filter(name='Bill', type='person')
    assert f.apply(sample_data) == [{
         "name": "Bill",
         "last_name": "Gilbert",
         "occupation": "was here",
         "type": "person",
     }]

    f = make_filter(type='person')
    assert f.apply(sample_data) == [{
         "name": "Bill",
         "last_name": "Gilbert",
         "occupation": "was here",
         "type": "person",
     }]

    f = make_filter(name='polly', type='person')
    assert f.apply(sample_data) == []

test_filter()
test_make_filter()