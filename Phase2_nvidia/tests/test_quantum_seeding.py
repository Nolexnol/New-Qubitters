from Phase2_nvidia.quantum_seeding import remove_symmetric_duplicates

def test_remove_symmetric_duplicates():
    samples = [
        ([1, -1, 1], 2.0),
        ([-1, 1, -1], 2.0),
        ([1, 1, -1], 1.0)
    ]

    filtered = remove_symmetric_duplicates(samples)

    # One of the symmetric pair should be removed
    assert len(filtered) == 2
