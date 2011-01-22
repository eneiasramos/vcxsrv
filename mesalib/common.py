#######################################################################
# Common SCons code

import os
import os.path
import re
import subprocess
import sys
import platform as _platform

import SCons.Script.SConscript


#######################################################################
# Defaults

_platform_map = {
	'linux2': 'linux',
	'win32': 'windows',
}

host_platform = sys.platform
host_platform = _platform_map.get(host_platform, host_platform)

# Search sys.argv[] for a "platform=foo" argument since we don't have
# an 'env' variable at this point.
if 'platform' in SCons.Script.ARGUMENTS:
    target_platform = SCons.Script.ARGUMENTS['platform']
else:
    target_platform = host_platform

cross_compiling = target_platform != host_platform

_machine_map = {
	'x86': 'x86',
	'i386': 'x86',
	'i486': 'x86',
	'i586': 'x86',
	'i686': 'x86',
	'ppc' : 'ppc',
	'x86_64': 'x86_64',
}


# find host_machine value
if 'PROCESSOR_ARCHITECTURE' in os.environ:
	host_machine = os.environ['PROCESSOR_ARCHITECTURE']
else:
	host_machine = _platform.machine()
host_machine = _machine_map.get(host_machine, 'generic')

default_machine = host_machine
default_toolchain = 'default'

if target_platform == 'windows' and cross_compiling:
    default_machine = 'x86'
    default_toolchain = 'crossmingw'


# find default_llvm value
if 'LLVM' in os.environ:
    default_llvm = 'yes'
else:
    default_llvm = 'no'
    try:
        if target_platform != 'windows' and \
           subprocess.call(['llvm-config', '--version'], stdout=subprocess.PIPE) == 0:
            default_llvm = 'yes'
    except:
        pass


#######################################################################
# Common options

def AddOptions(opts):
	try:
		from SCons.Variables.BoolVariable import BoolVariable as BoolOption
	except ImportError:
		from SCons.Options.BoolOption import BoolOption
	try:
		from SCons.Variables.EnumVariable import EnumVariable as EnumOption
	except ImportError:
		from SCons.Options.EnumOption import EnumOption
	opts.Add(EnumOption('build', 'build type', 'debug',
	                  allowed_values=('debug', 'checked', 'profile', 'release')))
	opts.Add(BoolOption('quiet', 'quiet command lines', 'yes'))
	opts.Add(EnumOption('machine', 'use machine-specific assembly code', default_machine,
											 allowed_values=('generic', 'ppc', 'x86', 'x86_64')))
	opts.Add(EnumOption('platform', 'target platform', host_platform,
											 allowed_values=('linux', 'cell', 'windows', 'winddk', 'wince', 'darwin', 'embedded', 'cygwin', 'sunos5', 'freebsd8')))
	opts.Add('toolchain', 'compiler toolchain', default_toolchain)
	opts.Add(BoolOption('gles', 'EXPERIMENTAL: enable OpenGL ES support', 'no'))
	opts.Add(BoolOption('llvm', 'use LLVM', default_llvm))
	opts.Add(BoolOption('debug', 'DEPRECATED: debug build', 'yes'))
	opts.Add(BoolOption('profile', 'DEPRECATED: profile build', 'no'))
	opts.Add(EnumOption('MSVS_VERSION', 'MS Visual C++ version', None, allowed_values=('7.1', '8.0', '9.0')))
