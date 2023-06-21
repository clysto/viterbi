# Convolutional Encoder and Viterbi Decoder

```py
from viterbi import Viterbi

dot11a_codec = Viterbi(7, [0o133, 0o171])
bits = [0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0]
output = dot11a_codec.encode(bits)
# [0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1]
dot11a_codec.decode(output)
# [0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0]
```
