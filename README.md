ywaf-tests
==========

A simple example on how ``hwaf`` could be modified to use ``yaml`` to
describe builds.

## Example

```sh
$ hwaf init work
$ cd work
$ hwaf setup
$ hwaf pkg co git://github.com/hwaf/ywaf-tests tests
$ hwaf setup -cmtpkgdir=src/tests
$ hwaf configure
hello from my [/tmp/work/src/tests/app/my-script.py] options
+++++++++>>>> hello from <waflib.Options.OptionsContext object at 0x7fd70d568e90>
Setting top to                           : /tmp/work 
Setting out to                           : /tmp/work/__build__ 
Manifest file                            : /tmp/work/.hwaf/local.conf 
Manifest file processing                 : ok 
Checking for 'g++' (c++ compiler)        : g++ 
Checking for 'gcc' (c compiler)          : gcc 
================================================================================
project                                  : work-0.0.1 
prefix                                   : install-area 
pkg dir                                  : src/tests 
variant                                  : x86_64-archlinux-gcc48-opt 
arch                                     : x86_64 
OS                                       : archlinux 
compiler                                 : gcc48 
build-type                               : opt 
projects deps                            : None 
install-area                             : install-area 
njobs-max                                : 2 
================================================================================
hello from my [/tmp/work/src/tests/app/my-script.py] configure
hello from my [/tmp/work/src/tests/app/waftools/my-script.py] configure
hello from my [/tmp/work/src/tests/app/waftools/my-other-script.py] configure
Checking for program python              : /usr/bin/python 
+++++++++++++++++ '/tmp/work/src/tests/ext'
'configure' finished successfully (0.122s)

$ hwaf
hello from my [/tmp/work/src/tests/app/my-script.py] options
+++++++++>>>> hello from <waflib.Options.OptionsContext object at 0x7f764ea30490>
Waf: Entering directory `/tmp/work/__build__'
hello from my [/tmp/work/src/tests/app/my-script.py] build
hello from my [/tmp/work/src/tests/app/waftools/my-script.py] build
hello from my [/tmp/work/src/tests/app/waftools/my-other-script.py] build
[ 1/10] cxx: src/tests/control/pkg-a/src/liba.cxx -> __build__/src/tests/control/pkg-a/src/liba.cxx.1.o
[ 2/10] cxx: src/tests/control/pkg-b/src/libb.cxx -> __build__/src/tests/control/pkg-b/src/libb.cxx.1.o
[ 3/10] cxx: src/tests/app/src/app.cxx -> __build__/src/tests/app/src/app.cxx.1.o
[ 4/10] cxx: src/tests/control/pkg-c/src/libc.cxx -> __build__/src/tests/control/pkg-c/src/libc.cxx.1.o
[ 5/10] cxx: src/tests/control/pkg-d/src/libd.cxx -> __build__/src/tests/control/pkg-d/src/libd.cxx.1.o
[ 6/10] cxxshlib: __build__/src/tests/control/pkg-a/src/liba.cxx.1.o -> __build__/src/tests/control/pkg-a/libaa.so
[ 7/10] cxxshlib: __build__/src/tests/control/pkg-b/src/libb.cxx.1.o -> __build__/src/tests/control/pkg-b/libbb.so
[ 8/10] cxxshlib: __build__/src/tests/control/pkg-c/src/libc.cxx.1.o -> __build__/src/tests/control/pkg-c/libmylinklib.so
[ 9/10] cxxprogram: __build__/src/tests/app/src/app.cxx.1.o -> __build__/src/tests/app/my-app
[10/10] cxxshlib: __build__/src/tests/control/pkg-d/src/libd.cxx.1.o -> __build__/src/tests/control/pkg-d/libmycomplib.so
Waf: Leaving directory `/tmp/work/__build__'
'build' finished successfully (0.588s)
hello from my [/tmp/work/src/tests/app/my-script.py] options
+++++++++>>>> hello from <waflib.Options.OptionsContext object at 0x7f8f614f4490>
Waf: Entering directory `/tmp/work/__build__'
hello from my [/tmp/work/src/tests/app/my-script.py] build
hello from my [/tmp/work/src/tests/app/waftools/my-script.py] build
hello from my [/tmp/work/src/tests/app/waftools/my-other-script.py] build
+ install install-area/share/hwaf/__hwaf_module__work.py (from __build__/__hwaf_module__work.py)
+ install /tmp/work/install-area/lib/libaa.so (from __build__/src/tests/control/pkg-a/libaa.so)
+ install /tmp/work/install-area/lib/libbb.so (from __build__/src/tests/control/pkg-b/libbb.so)
+ install install-area/project.info (from __build__/project.info)
+ install /tmp/work/install-area/lib/libmylinklib.so (from __build__/src/tests/control/pkg-c/libmylinklib.so)
+ install /tmp/work/install-area/bin/my-app (from __build__/src/tests/app/my-app)
+ install /tmp/work/install-area/lib/libmycomplib.so (from __build__/src/tests/control/pkg-d/libmycomplib.so)
Waf: Leaving directory `/tmp/work/__build__'
'install' finished successfully (0.033s)

$ hwaf run my-app
hello from my [/home/binet/tmp/yy/ttt/work/src/tests/app/my-script.py] options
+++++++++>>>> hello from <waflib.Options.OptionsContext object at 0x7ff9e45214d0>
hello from my [/home/binet/tmp/yy/ttt/work/src/tests/app/my-script.py] build
hello from my [/home/binet/tmp/yy/ttt/work/src/tests/app/waftools/my-script.py] build
hello from my [/home/binet/tmp/yy/ttt/work/src/tests/app/waftools/my-other-script.py] build
=== app ===
liba: hello from liba
libb: hello from libb
'run' finished successfully (0.081s)
```

## YAML-based syntax

Here is an example of such a ``hscript`` file:

 https://github.com/hwaf/ywaf-tests/blob/master/app/hscript.yml
 

A typical ``Athena`` ``component-library`` package would look like:

```yaml
## -*- yaml -*-
package: {
  name: "Control/AthenaServices",
  authors: [ 
    "me <me@cern.ch>", 
    "you <you@cern.ch>",
  ],
  
  deps: {
    public: [
     "Control/AthenaBaseComps",
     "Control/StoreGate",
     
     "Event/EventInfo",
    ],
  },
}

build: {
  AthenaServices: {
    features: "athena_component_library",
    source: ["src/*.cxx"],
    use: ["AthenaBaseComps", "StoreGateLib", "EventInfo"],
    # or, possibly:
    # use: ["@{auto-imports-from-pkg-uses}"],
    # or, possibly:
    # use: [], # implicitly imports from pkg uses...
  }
}
```

## hscript.yml specss

Here is the complete syntax:

```yaml
## -*- yaml -*-

## describe a full project
## not needed for a simple package.
# project: {
#   name: "AtlasCore",
#   deps: {
#     public: [
#       "Gaudi",
#       "DetCommon",
#     ],
#   },
# }

package: {
  name: "control/pkg-app",
  authors: ["my", "myself", "irene"],

  deps: {
    public: [
     "control/pkg-a",
     "control/pkg-b",
    ],

    private: [
     "Control/AthenaBaseComps",
    ],

    # specify runtime dependencies
    # e.g: python modules for scripts installed by this package
    #      binaries used by scripts installed by this package
    runtime: [
     "External/AtlasPyFwdBwdPorts", # for py-yaml
     "Tools/PyUtils",               # for setup-workarea
    ],
  },
}

options: {
  tools: ["compiler_c", "compiler_cxx", "python"],

  # escape hatch: 
  #  this will load the python module and
  #  execute the function 'options'
  hwaf-call: [
    "my-script.py",
    "waftools/my-script.py",
    "waftools/my-other-script.py",
  ],
}

configure: {
  tools: ["compiler_c", "compiler_cxx", "python"],
  env: {
    MY_VAR: "/some/path",
    PATH: "${MY_VAR}/bin:${PATH}",
    # or special syntax ?
    # _@_append_PATH:  "${MY_VAR}/bin",
    # PATH_@_append:  "${MY_VAR}/bin",
    my_macro: {
      default: "some-default-value",
      i686:    "some-value-for-32b",
      x86_64:  "some-value-for-64b",
    },
    my_other_macro: "some-value",
    
    ## tentative syntax... 
    ## what should be the (proper) algorithm to pattern-match ?
    CXXFLAGS: {
      unix&i686: ["-m32",],
      unix&x86_64: ["-m64",],
    },
  },

  # list of tags definitions
  declare-tags: [
      {x86_64-linux-gcc-opt: [x86_64, linux, 64b, gcc, opt]},
      {x86_64: [64b]},
  ],

  # list of tags to activate
  apply-tags: [x86_64-linux-gcc-opt],

  # escape hatch:
  #  this will load the python module and,
  #  execute the function 'configure'
  hwaf-call: [
    "my-script.py",
    "waftools/my-script.py",
    "waftools/my-other-script.py",
  ],

}

build: {

  my-app: {
    features: "cxx cxxprogram",
    source: "src/app.cxx",
    use: ["my-lib-aa", "my-lib-bb"],
  },

  my-lib-aa: {
    features: "cxx cxxshlib",
    source: "src/liba.cxx",
  },
  
  my-lib-bb: {
    features: "cxx cxxshlib",
    source: "src/libb.cxx",
  },
  
  my-py-script: {
    features: "python",
    source: "scripts/my-py-script.py",
  },
  
  # escape hatch: 
  #  this will load the python module and,
  #  execute the function 'build'
  hwaf-call: [
    "my-script.py",
    "waftools/my-script.py",
    "waftools/my-other-script.py",
  ],
}
## EOF ##
```
