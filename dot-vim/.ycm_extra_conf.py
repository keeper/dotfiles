def Settings(**kwargs):
    flags = [
    '-Wall',
    '-Wextra',
    '-Werror',
    # '-Wc++98-compat',
    '-Wno-long-long',
    '-Wno-variadic-macros',
    '-fexceptions',
    '-DNDEBUG',
    '-I',
    '.',
    '-I',
    '.',
    '-I',
    './include',
    '-I',
    '/usr/local/include/highfive',
    '-I',
    '/usr/include/hdf5/serial',
    '-I',
    './extern/googletest/googletest/include',
    '-I',
    './extern/googletest/googlemock/include',
    '-isystem',
    '/usr/lib/gcc/x86_64-linux-gnu/5',

    # std is required
    # clang won't know which language to use compiling headers
    # '-std=c++11',

    # '-x' and 'c++' also required
    # use 'c' for C projects
    # '-x',
    # 'c++',

    # include third party libraries
    #'-isystem',
    #'/usr/include/python2.7',
    ]
    data = kwargs['client_data']
    filetype = data['&filetype']

    if filetype == 'c':
        flags += ['-xc']
    elif filetype == 'c++' or filetype == 'cpp':
        flags += ['-std=c++17']
        flags += ['-x']
        flags += ['c++']
    else:
        flags = []

    # youcompleteme is calling this function to get flags
    # You can also set database for flags. Check: JSONCompilationDatabase.html in
    # clang-3.2-doc package
    return {
            'flags': flags,
            'do_cache': True
            }

