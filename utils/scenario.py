def apply_scenario(ndvi, temp, trees, roofs, water):
    """
    Estimate environmental improvements based on interventions.
    """

    new_ndvi = ndvi + trees * 0.0015
    new_ndvi = min(new_ndvi, 0.8)

    cooling = (
        trees * 0.02
        + roofs * 0.015
        + water * 0.01
    )

    new_temp = max(temp - cooling, 20)

    return new_ndvi, new_temp