using System;

namespace RandomGenerator;

/// <summary>
/// Deterministic linear congruential generator mirroring the Python implementation.
/// </summary>
public class LcgRandom
{
    private const uint Modulus = 4294967296; // 2**32
    private const uint Multiplier = 1664525;
    private const uint Increment = 1013904223;

    private uint _state;

    public LcgRandom(uint seed)
    {
        _state = seed;
    }

    public int NextInt(int maxExclusive)
    {
        if (maxExclusive <= 0)
        {
            throw new ArgumentOutOfRangeException(nameof(maxExclusive), "Upper bound must be positive.");
        }

        _state = unchecked((Multiplier * _state + Increment) % Modulus);
        return (int)(_state % (uint)maxExclusive);
    }
}
