from viterbicodec import ViterbiCodec, reverse_bits

all = ["Viterbi"]


def list2str(bits):
    return "".join(map(lambda x: "1" if x > 0 else "0", bits))


def str2list(bits):
    return list(map(lambda x: 1 if x == "1" else 0, bits))


class Viterbi(ViterbiCodec):
    def __init__(self, constraint, polynomials):
        for i in range(len(polynomials)):
            polynomials[i] = reverse_bits(constraint, polynomials[i])
        self.constraint = constraint
        self.polynomials = polynomials
        ViterbiCodec.__init__(self, constraint, polynomials)

    def encode(self, bits):
        bits = list2str(bits)
        output = ViterbiCodec.encode(self, bits)[: -2 * (self.constraint - 1)]
        return str2list(output)

    def decode(self, bits):
        bits = list2str(bits)
        bits += "0" * (2 * (self.constraint - 1))
        output = ViterbiCodec.decode(self, bits)
        return str2list(output)


if __name__ == "__main__":
    bits = [1] * 100
    codec = Viterbi(7, [0o133, 0o171])
    a = codec.encode(bits)
    print(a)
    b = codec.decode(a)
    print(b)
