#! usr/bin/env python2.7
#-*- coding: utf-8 -*-
max = int(input('Please input primes range (0~max), max: '))
primes = filter(lambda prime: all(prime % n for n in range(2, prime)), range(2, max))


print primes
