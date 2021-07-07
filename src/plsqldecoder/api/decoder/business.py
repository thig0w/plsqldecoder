# -*- coding: utf-8 -*-
"""Business logic for /decoder API endpoints."""


def decode(hashed="28734699435745114553445143494439451343314421345532093267"):
    sp_hash = [hashed[i : i + 4] for i in range(0, len(hashed), 4)]
    key = sp_hash.pop(0)

    decoded = ""
    for i in range(0, len(sp_hash)):
        val = int(sp_hash[i]) - 1000
        mask = int(key) + (10 * (i + 1))

        decoded = decoded + chr((val ^ mask) >> 4)

    return decoded


if __name__ == "__main__":
    print(decode())
