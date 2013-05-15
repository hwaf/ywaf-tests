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

![hbuild](https://github.com/mana-fwk/ywaf-tests/raw/master/hbuild)

