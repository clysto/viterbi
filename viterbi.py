from viterbicodec import ViterbiCodec, reverse_bits

__all__ = ["Viterbi"]


def list2str(bits):
    return "".join(map(lambda x: "1" if x > 0 else "0", bits))


def str2list(bits):
    return list(map(lambda x: 1 if x == "1" else 0, bits))


class Viterbi(ViterbiCodec):
    def __init__(self, constraint, polynomials, puncpat=[]):
        if constraint <= 0:
            raise Exception("Constraint should be greater than 0.")
        for i in range(len(polynomials)):
            if polynomials[i] <= 0:
                raise Exception("Polynomial should be greater than 0.")
            if polynomials[i] >= (1 << constraint):
                raise Exception(f"Polynomial should be less than {1 << constraint}")
            polynomials[i] = reverse_bits(constraint, polynomials[i])
        self.constraint = constraint
        self.polynomials = polynomials
        if len(puncpat) == 0:
            ViterbiCodec.__init__(self, constraint, polynomials, "")
        else:
            ViterbiCodec.__init__(self, constraint, polynomials, list2str(puncpat))
        self.puncpat = puncpat if len(puncpat) > 0 else [1]
        self.puncpat_ones_len = self.puncpat.count(1)
        self.is_punctured = len(puncpat) > 0

    def encode(self, bits):
        if (
            self.is_punctured
            and len(bits) * len(self.polynomials) % len(self.puncpat) != 0
        ):
            raise Exception(
                "The length of bits divided by the base code rate must be an integer multiple of the length of the puncture pattern."
            )
        bits = list2str(bits)
        output = ViterbiCodec.encode(self, bits)
        return str2list(output)

    def decode(self, bits):
        if self.is_punctured and len(bits) % self.puncpat_ones_len != 0:
            raise Exception(
                "The length of bits must be an integer multiple of the number of ones in the puncture pattern."
            )
        if (
            len(bits)
            / self.puncpat_ones_len
            * len(self.puncpat)
            % len(self.polynomials)
            != 0
        ):
            raise Exception(
                "The length of bits divided by the number of ones in the puncture pattern "
                + "times the length of the puncture pattern must be an integer multiple of the number "
                + "of bits in an input symbol."
            )
        bits = list2str(bits)
        output = ViterbiCodec.decode(self, bits)
        return str2list(output)
