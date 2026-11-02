"""Zero-width steganographic canary encoding and decoding."""
ZW_0 = "\u200B"  # Zero-width space (bit 0)
ZW_1 = "\u200C"  # Zero-width non-joiner (bit 1)

class CanaryEngine:
    @staticmethod
    def encode_id(identifier: str) -> str:
        bits = "".join(f"{ord(c):08b}" for c in identifier)
        return "".join(ZW_1 if b == "1" else ZW_0 for b in bits)

    @staticmethod
    def decode_canary(text: str) -> str:
        raw_bits = [("1" if c == ZW_1 else "0") for c in text if c in (ZW_0, ZW_1)]
        if not raw_bits or len(raw_bits) % 8 != 0:
            return ""
        chars = []
        for i in range(0, len(raw_bits), 8):
            byte = "".join(raw_bits[i:i+8])
            chars.append(chr(int(byte, 2)))
        return "".join(chars)

    @classmethod
    def inject(cls, text: str, canary_id: str) -> str:
        watermark = cls.encode_id(canary_id)
        return f"{text}{watermark}"

    @classmethod
    def has_canary(cls, text: str, canary_id: str) -> bool:
        return canary_id in cls.decode_canary(text)
