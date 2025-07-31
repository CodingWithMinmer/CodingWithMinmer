class LC125_ValidPalindrome {
    boolean isPalindrome_125(String s) {
        int left = 0, right = s.length() - 1;
        while (left < right) {
            while (!Character.isLetterOrDigit(s.charAt(left)) && left < right)
                left++;
            while (!Character.isLetterOrDigit(s.charAt(right)) && left < right)
                right--;
    
            if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right)))
                return false;
    
            left++;
            right--;
        }
        return true;
    }

    // VARIANT: What if you could only consider a limited set of characters as a part of a potential palindrome?
    boolean isPalindrome_variant_125(String s, List<Character> include) {
        HashSet<Character> included_set = new Hashset<>(include);
        int left = 0;
        int right = s.length() - 1;
        while (left < right) {
            while (!included_set.contains(s.charAt(left)) && left < right) {
                left++;
            }
            while (!included_set.contains(s.charAt(right)) && left < right) {
                right--;
            }

            if (s.charAt(left) != s.charAt(right))
                return false;

            left++;
            right--;
        }

        return true;
    }
}