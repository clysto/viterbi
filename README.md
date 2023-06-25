# Convolutional Encoder and Viterbi Decoder

![License](https://img.shields.io/github/license/clysto/viterbi)
![Version](https://img.shields.io/github/tag/clysto/viterbi)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/viterbi)
![PyPI - Downloads](https://img.shields.io/pypi/dm/viterbi)

> This project is a fork of <https://github.com/xukmin/viterbi> that introduces Python support, enabling effortless utilization of the Viterbi module within the Python environment.

## Install

```sh
pip install viterbi
```

## Usage

The following is a convolutional encoder with a constraint length of 7. The diagram indicates the binary values and polynomial form, indicating the left-most bit is the most-significant-bit (MSB). The generating polynomials are 1011011 and 1111001 can be alternatively expressed in octal as 133 and 171, respectively.

![convolutional encoder](https://raw.githubusercontent.com/clysto/viterbi/master/docs/convolutional%20encoder.svg)

Expressed in code as:

```python
from viterbi import Viterbi
dot11a_codec = Viterbi(7, [0o133, 0o171])
```

You can use the viterbi decoder like this:

```python
from viterbi import Viterbi

dot11a_codec = Viterbi(7, [0o133, 0o171])
bits = [0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0]
output = dot11a_codec.encode(bits)
# [0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1]
dot11a_codec.decode(output)
# [0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0]
```

## Puncturing

This library also allows you to puncture the original encoded data by specifying a puncture pattern or decode data that has already been punctured.

```python
from viterbi import Viterbi

# Puncture Pattern: [1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1]
dot11a_codec = Viterbi(7, [0o133, 0o171], [1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1])
```

## Using in C++

You can find the way to use the Viterbi decoder in C++ in the [README](https://github.com/xukmin/viterbi) of the original project.
