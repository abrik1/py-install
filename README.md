<h1 align="center"><code>py-install</code></h1>
<h3 align="center"><code>install</code> bindings for Python 3</h3>

# what is install?

> ### `install` is a command line utility for GNU based OSes which copies a file with specific permissions

# syntax:-

```python
install(TargetFile, Destination, Permissions)
```

- `TargetFile` is the file which is to be copied
- `Destination` is the target destination(it should be a directory) where `TargetFile` will be copied
- `Permissions` is the specific permissions supported by `os.chmod()`

# todo:-
- [ ] Enable directory support
