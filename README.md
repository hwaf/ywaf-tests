ywaf-tests
==========

A simple example on how ``hwaf`` could be modified to use ``yaml`` to
describe builds.

## Example

```sh
$ ./h-waf configure
Setting top to                           : /tmp/ywaf-tests 
Setting out to                           : /tmp/ywaf-tests/build 
Checking for 'gcc' (c compiler)          : /usr/bin/gcc 
loading [compiler_cxx]...
Checking for 'g++' (c++ compiler)        : /usr/bin/g++ 
loading [python]...
Checking for program python              : /usr/bin/python 
$ ./h-waf build install
$ cd build; export LD_LIBRARY_PATH=`pwd`:$LD_LIBRARY_PATH
$ ./build/my-app
=== app ===                                                                     
liba: hello from liba
libb: hello from libb

```

## YAML-based syntax

Here is an example of such a ``hbuild`` file:

```yaml
## -*- yaml -*-

package: {
  name: "my-package",
  authors: ["my", "myself", "irene"],
}

options: {
  tools: ["compiler_cxx", "python"],
}

configure: {
  tools: ["compiler_cxx", "python"],
}

build: {
  my-app: {
    features: "cxx cxxprogram",
    source: "src/app/src/app.cxx",
    use: ["aa", "bb"],
  },

  aa: {
    features: "cxx cxxshlib",
    source: "src/liba/src/liba.cxx",
    includes: "src/liba/include",
    export_includes: "src/liba/include",
  },

  bb: {
    features: "cxx cxxshlib",
    source: "src/libb/src/libb.cxx",
    includes: "src/libb/include",
    export_includes: "src/libb/include",
  },
}
## EOF ##
```

