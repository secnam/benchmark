Framework Benchmark
===================

Framework benchmark with simple 'hello world' responders.

Tests were peformed on:
	* Mac Mini (late 2014)
	* Proccessor 2.8 Ghz Intel Core i5

Luxon Test Results:
-------------------

.. code:: bash

    $ python benchmark.py luxon
    Jan 14 21:00:26 root[56719] <ERROR>: Unable to determine application root. Using current working directory '/Users/christiaan/Documents/code/benchmark/luxon' 
                  msec    rps  tcalls  funcs
    luxon         1560  64105      41     37
    total requests: 100000

    Profiling with 100000 requests
             3800023 function calls (3800022 primitive calls) in 2.734 seconds

       Ordered by: internal time
       List reduced from 51 to 20 due to restriction <20>

       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       100000    0.730    0.000    2.492    0.000 application.py:134(__call__)
       100000    0.253    0.000    0.597    0.000 request.py:300(__init__)
       100000    0.148    0.000    0.205    0.000 router.py:117(find)
       100000    0.116    0.000    0.167    0.000 request.py:47(request_id)
       100000    0.111    0.000    0.145    0.000 response.py:67(__init__)
       100000    0.106    0.000    2.686    0.000 benchmark.py:79(request)
       100000    0.103    0.000    0.221    0.000 response.py:109(body)
       100000    0.094    0.000    0.272    0.000 timer.py:62(__enter__)
       100000    0.088    0.000    0.088    0.000 {method 'copy' of 'dict' objects}
       100000    0.086    0.000    0.253    0.000 request.py:91(__init__)
       100000    0.070    0.000    0.070    0.000 threaddict.py:44(__setitem__)
       100000    0.066    0.000    0.105    0.000 logger.py:414(getEffectiveLevel)
       300000    0.065    0.000    0.065    0.000 {method 'strip' of 'str' objects}
       100000    0.064    0.000    0.135    0.000 globals.py:117(__setattr__)
       200000    0.062    0.000    0.062    0.000 {method 'encode' of 'str' objects}
       100000    0.054    0.000    0.159    0.000 logger.py:424(debug_mode)
       100000    0.052    0.000    0.099    0.000 encoding.py:31(if_unicode_to_bytes)
       100000    0.050    0.000    0.062    0.000 timer.py:79(__exit__)
            1    0.048    0.048    2.733    2.733 <timeit-src>:2(inner)
       100000    0.040    0.000    0.040    0.000 logger.py:371(info)

Django Test Results:
--------------------

.. code:: bash

	$ python benchmark.py django
				  msec    rps  tcalls  funcs
	django        8025  12461     191     81
	total requests: 100000

	Profiling with 100000 requests
			 18800023 function calls (18700022 primitive calls) in 13.419 seconds

	   Ordered by: internal time
	   List reduced from 95 to 20 due to restriction <20>

	   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
	   300000    0.840    0.000    1.081    0.000 resolvers.py:30(__init__)
	   100000    0.801    0.000    2.080    0.000 wsgi.py:67(__init__)
	   100000    0.728    0.000   13.004    0.000 wsgi.py:142(__call__)
	200000/100000    0.727    0.000    2.770    0.000 resolvers.py:488(resolve)
	   100000    0.548    0.000    7.021    0.000 base.py:98(_get_response)
	  1100000    0.449    0.000    0.449    0.000 {built-in method builtins.hasattr}
	   100000    0.447    0.000    0.722    0.000 dispatcher.py:228(_live_receivers)
	   500000    0.383    0.000    0.383    0.000 {method 'search' of '_sre.SRE_Pattern' objects}
	   300000    0.365    0.000    0.723    0.000 resolvers.py:146(match)
	   100000    0.342    0.000    1.319    0.000 response.py:36(__init__)
	   700000    0.328    0.000    0.624    0.000 wsgi.py:200(get_bytes_from_wsgi)
	   200000    0.309    0.000    0.535    0.000 response.py:106(_convert_to_charset)
	  1000000    0.307    0.000    0.307    0.000 {method 'encode' of 'str' objects}
	   300000    0.264    0.000    0.946    0.000 utils.py:216(all)
	   200000    0.258    0.000    0.831    0.000 wsgi.py:167(get_script_name)
	   600000    0.254    0.000    0.254    0.000 {built-in method builtins.getattr}
	   200000    0.246    0.000    0.737    0.000 response.py:74(charset)
	   100000    0.239    0.000    2.842    0.000 base.py:62(view)
	  1300000    0.233    0.000    0.233    0.000 {method 'get' of 'dict' objects}
	   100000    0.233    0.000    1.114    0.000 dispatcher.py:177(<listcomp>)

Flask Test Results:
-------------------

.. code:: bash

	$ python benchmark.py flask
				  msec    rps  tcalls  funcs
	flask        10905   9170     253    117
	total requests: 100000

	Profiling with 100000 requests
			 25000023 function calls (25000022 primitive calls) in 18.968 seconds

	   Ordered by: internal time
	   List reduced from 131 to 20 due to restriction <20>

	   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
	  1000000    0.747    0.000    0.899    0.000 local.py:68(__getattr__)
	   600000    0.699    0.000    1.260    0.000 local.py:160(top)
	   100000    0.646    0.000    2.770    0.000 routing.py:1261(bind_to_environ)
	  3100002    0.595    0.000    0.595    0.000 {built-in method builtins.isinstance}
	   100000    0.546    0.000    2.554    0.000 wrappers.py:830(__init__)
	   100000    0.532    0.000    1.186    0.000 routing.py:1443(match)
	   800000    0.515    0.000    0.853    0.000 {built-in method builtins.getattr}
	   100000    0.468    0.000    3.274    0.000 ctx.py:299(push)
	   100000    0.420    0.000    2.599    0.000 ctx.py:336(pop)
	   200000    0.407    0.000    0.779    0.000 datastructures.py:1187(set)
	   100000    0.349    0.000   18.279    0.000 app.py:1952(wsgi_app)
	   100000    0.341    0.000    0.853    0.000 wrappers.py:1187(get_wsgi_headers)
	   100000    0.316    0.000    2.968    0.000 app.py:1690(make_response)
	   600000    0.302    0.000    0.453    0.000 _compat.py:198(to_unicode)
	   300000    0.294    0.000    0.294    0.000 {built-in method builtins.hasattr}
	   100000    0.282    0.000    0.765    0.000 routing.py:1374(__init__)
	   100000    0.281    0.000    4.620    0.000 ctx.py:237(__init__)
	   100000    0.251    0.000    5.096    0.000 app.py:1600(full_dispatch_request)
	   200000    0.249    0.000    3.019    0.000 app.py:1752(create_url_adapter)
	   100000    0.248    0.000    0.510    0.000 app.py:1861(do_teardown_request)

