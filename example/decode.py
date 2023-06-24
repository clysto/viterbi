from viterbi import Viterbi

dot11a_codec = Viterbi(7, [0o133, 0o171])
bits = [0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0]
print(bits)
output1 = dot11a_codec.encode(bits)
print(output1)
output2 = dot11a_codec.decode(output1)
print(output2)


dot11a_codec_rate13 = Viterbi(7, [0o133, 0o171], [1, 1, 0])
bits = [0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1]
print(bits)
output1 = dot11a_codec_rate13.encode(bits)
print(output1)
output2 = dot11a_codec_rate13.decode(output1)
print(output2)
