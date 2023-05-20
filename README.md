<h1 align="center"><code>py-install</code></h1>
<h3 align="center"><code>install</code> bindings for Python 3</h3>

# what is install?

> ### `install` is a command line utility for GNU based OSes which copies a file with specific permissions. It is useful to make package managers.

# syntax:-

```python
install(TargetFile, Destination, Permissions)
```

- `TargetFile` is the file which is to be copied
- `Destination` is the target destination(it should be a directory) where `TargetFile` will be copied
- `Permissions` is the specific permissions supported by `os.chmod()`

> __Note__:- There are only specific permissions supported:- [exec_all, write_all, read_all, rwe_all, read_user, write_user, exec_user]
> 

<h4> Permission explanations:- </h4>
<ul type="square">
  <li><code>exec_all</code>: permission allows every user to execute</li>
  <li><code>exec_user</code>: permission allows current user to execute</li>
  <li><code>read_all</code>: permission allows every user to read a file</li>
  <li><code>read_user</code>: permission allows current user to read a file</li>
  <li><code>write_all</code>: permission allows every user to edit a file</li>
  <li><code>write_user</code>: permission allows every user to execute</li>
  <li><code>rwe_all</code>: permission allows current user to perform read,write and execute</li>
  <li><code>rwe_user</code>: permission allows current user to perform read,write and execute</li>
</ul>

# todo:-
- [ ] Enable directory support
