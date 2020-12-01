import utils


def test_storage():
    data = utils.storage.load('test1.json')
    assert len(data) == 0

    data['test'] = 123
    utils.storage.save('test.json', data)

    data = utils.storage.load('test.json')
    assert data['test'] == 123

    utils.storage.save('test.json', None)
