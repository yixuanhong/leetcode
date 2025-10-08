def product_except_self(nums: list[int]):
    n = len(nums)
    answer = [1] * n

    # Step 1: Left (prefix) product
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    # Step 2: Right (suffix) product
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer

