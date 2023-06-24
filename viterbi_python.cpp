#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "viterbi.h"

PYBIND11_MODULE(viterbicodec, m) {
  pybind11::class_<ViterbiCodec>(m, "ViterbiCodec")
      .def(pybind11::init<int, const std::vector<int>&, const std::string&>())
      .def("encode", &ViterbiCodec::Encode)
      .def("decode", &ViterbiCodec::Decode);

  m.def("reverse_bits", &ReverseBits);
}