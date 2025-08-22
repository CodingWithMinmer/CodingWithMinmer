class Solution:
    def add_string_decimals_415(self, num1: str, num2: str) -> str:
        nums1 = num1.split(".")
        nums2 = num2.split(".")
        decimals1 = nums1[1] if len(nums1) > 1 else ""
        decimals2 = nums2[1] if len(nums2) > 1 else ""

        max_len = max(len(decimals1), len(decimals2))
        decimals1 = decimals1.ljust(max_len, "0")
        decimals2 = decimals2.ljust(max_len, "0")

        carry = [0]
        result = []

        def add_strings_415(num1: str, num2: str, carry: list) -> str:
            n1 = len(num1) - 1
            n2 = len(num2) - 1
            result = []
            while n1 >= 0 or n2 >= 0:
                sum = 0
                if n1 >= 0:
                    sum += int(num1[n1])
                    n1 -= 1
                if n2 >= 0:
                    sum += int(num2[n2])
                    n2 -= 1
                sum += carry[0]

                result.append(str(sum % 10))
                carry[0] = sum // 10

            return "".join(result)

        result.append(add_strings_415(decimals1, decimals2, carry))

        if decimals1 or decimals2:
            result.append(".")

        result.append(add_strings_415(nums1[0], nums2[0], carry))
        if carry[0]:
            print(carry)
            result.append(str(carry[0]))
        return "".join(result)[::-1]


if __name__ == "__main__":
    solution = Solution()
    # Only Whole Numbers
    assert solution.add_string_decimals_415("11", "123") == "134"
    assert solution.add_string_decimals_415("456", "77") == "533"
    assert solution.add_string_decimals_415("0", "0") == "0"
    assert (
        solution.add_string_decimals_415("0", "2983435243982343") == "2983435243982343"
    )
    assert (
        solution.add_string_decimals_415("99999999", "2983435243982343")
        == "2983435343982342"
    )
    assert solution.add_string_decimals_415("99999999", "99999999999") == "100099999998"

    # Both Decimals With And Without Carry
    assert solution.add_string_decimals_415("123.53", "11.2") == "134.73"
    assert (
        solution.add_string_decimals_415("687345.3434321", "389457248.24374657243")
        == "390144593.58717867243"
    )
    assert solution.add_string_decimals_415(".56", ".12") == ".68"
    assert solution.add_string_decimals_415(".5995495049556", ".12") == ".7195495049556"
    assert (
        solution.add_string_decimals_415(".9479823748932", ".716400040030")
        == "1.6643824149232"
    )
    assert (
        solution.add_string_decimals_415(".00009479823748932", ".000000716400040030")
        == ".000095514637529350"
    )
    assert (
        solution.add_string_decimals_415(
            ".00009479823748932", ".00000071640004003000000"
        )
        == ".00009551463752935000000"
    )
    assert solution.add_string_decimals_415("110.12", "9.") == "119.12"
    assert (
        solution.add_string_decimals_415("111111110.0013430430433434454001", "9.")
        == "111111119.0013430430433434454001"
    )
    assert (
        solution.add_string_decimals_415(
            "111111110.0013430430433434454001", "993483400013438854."
        )
        == "993483400124549964.0013430430433434454001"
    )
    assert solution.add_string_decimals_415("910.99999", "999.9999") == "1910.99989"
    assert (
        solution.add_string_decimals_415("999999.99999", "999999.9999")
        == "1999999.99989"
    )
    assert solution.add_string_decimals_415("123.525", "11.2") == "134.725"
    assert (
        solution.add_string_decimals_415("1234540458475845.", "8348736.")
        == "1234540466824581"
    )

    # # One Decimal, One Whole Number
    assert solution.add_string_decimals_415("110.75", "9") == "119.75"
    assert solution.add_string_decimals_415("110.75", "9999999") == "10000109.75"
    assert (
        solution.add_string_decimals_415("150423434.00000000000", "9999999.")
        == "160423433.00000000000"
    )
    assert (
        solution.add_string_decimals_415("150423434.0000009184837483", "9999999.")
        == "160423433.0000009184837483"
    )
    assert (
        solution.add_string_decimals_415("110.9010479382798527", "9999999.")
        == "10000109.9010479382798527"
    )
