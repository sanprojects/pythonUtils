## Install
```shell
pip3 install --upgrade https://github.com/sanprojects/pythonUtils/archive/main.zip
```

## Usage   
```python
import utils
utils.http.enableLogger()
utils.http.enableCache()
```

```
history = utils.storage.load('history.json')
history[123] = 'test'
utils.storage.save('history.json', history)
```