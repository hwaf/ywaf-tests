# -*- python -*-
# @purpose the main entry point for driving the build and installation steps
# @author Sebastien Binet <binet@cern.ch>

# imports ---------------------------------------------------------------------
import os

# globals ---------------------------------------------------------------------
top = '.'
out = '__build__'
PREFIX = 'install_area'
VERSION = '0.0.1' # FIXME: should take it from somewhere else
APPNAME = os.path.basename(os.getcwd())

# imports ---------------------------------------------------------------------

# waf imports --
import waflib.Logs
import waflib.Utils
import waflib.Options
import waflib.Context
import waflib.Logs as msg

# functions -------------------------------------------------------------------

def options(ctx):
    ctx.recurse('app')
    ctx.recurse('control/pkg-a')
    ctx.recurse('control/pkg-b')
    return

def configure(ctx):
    ctx.recurse('app')
    ctx.recurse('control/pkg-a')
    ctx.recurse('control/pkg-b')
    return

def build(ctx):
    ctx.recurse('app')
    ctx.recurse('control/pkg-a')
    ctx.recurse('control/pkg-b')
    return
