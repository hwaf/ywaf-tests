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

Here is an example of such a ``hscript`` file:

 https://github.com/mana-fwk/ywaf-tests/blob/master/app/hscript.yml
 

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
    # or, possible:
    # use: [], # implicitly imports from pkg uses...
  }
}
```

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
  # list of tags to activate
  tag: [i686, x86_64, enable_graphics],

  # -- escape hatch --
  # entry point to load personal waf-rules and functions
  # this is the equivalent of CMT's fragments, docs and patterns
  #
  # what the key of this dict is meant to represent isn't clear yet:
  #  - should this be the name of a waf-function ? (but attached to what Context?)
  #  - or the name of the (synthesized) python module under which the content
  #    of the imported file would be published ?
  #  - or require that it is just the name for a loadable waf-feature ?
  export_tools: {
    build_reflex_dict: "some/file.py",
    build_rootcint_dict: "some/other/file.py",
  },

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
