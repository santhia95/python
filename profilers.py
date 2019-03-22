# Python includes a profiler called cProfile. It not only gives the total running time, but also times each function separately, and tells you how many times each function was called, making it easy to determine where you should make optimizations.

# You can call it from within your code, or from the interpreter, like this:

# import cProfile
# cProfile.run('foo()')
# Even more usefully, you can invoke the cProfile when running a script:

# python -m cProfile myscript.py
# To make it even easier, I made a little batch file called 'profile.bat':

# python -m cProfile %1
# So all I have to do is run:

# profile euler048.py
# And I get this:

# 1007 function calls in 0.061 CPU seconds

# Ordered by: standard name
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.061    0.061 <string>:1(<module>)
#  1000    0.051    0.000    0.051    0.000 euler048.py:2(<lambda>)
#     1    0.005    0.005    0.061    0.061 euler048.py:2(<module>)
#     1    0.000    0.000    0.061    0.061 {execfile}
#     1    0.002    0.002    0.053    0.053 {map}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler objects}
#     1    0.000    0.000    0.000    0.000 {range}
#     1    0.003    0.003    0.003    0.003 {sum}