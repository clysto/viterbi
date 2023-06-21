# Makefile for viterbi codec.
#
# Created by: Min Xu <mxu@scu.edu> or <xukmin@gmail.com>
# Date: 01/30/2015

CXX = g++

BINS     = viterbi_main viterbi_test $(PYLIB)
SRCS     = viterbi.cpp viterbi_main.cpp viterbi_test.cpp
PYLIB    = viterbicodec$(shell python3-config --extension-suffix)
CPPFLAGS = $(shell pybind11-config --includes) -std=c++11 

all: $(BINS)

clean:
	$(RM) *.o $(BINS)

test: viterbi_test
	./viterbi_test

$(PYLIB): viterbi.cpp viterbi_python.cpp
	$(CXX) $(CPPFLAGS) -undefined dynamic_lookup -shared -fPIC $^ -o $@

viterbi.o: viterbi.cpp viterbi.h
	$(CXX) $(CPPFLAGS) -c $<

viterbi_main.o: viterbi_main.cpp viterbi.h
	$(CXX) $(CPPFLAGS) -c $<

viterbi_main: viterbi_main.o viterbi.o
	$(CXX) $(CPPFLAGS) $^ -o $@

viterbi_test.o: viterbi_test.cpp viterbi.h
	$(CXX) $(CPPFLAGS) -c $<

viterbi_test: viterbi_test.o viterbi.o
	$(CXX) $(CPPFLAGS) $^ -o $@

%.o: %.cpp
	$(CXX) $(CPPFLAGS) -c $<

.PHONY: all clean test

