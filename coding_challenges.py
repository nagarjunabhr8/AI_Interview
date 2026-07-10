"""
Coding Challenges for Programming Knowledge Assessment
Real coding problems with multiple difficulty levels
Time allocation: 5-15 minutes based on complexity
"""

from typing import List, Dict, Any
import random


class CodingChallenge:
    """Represents a single coding challenge."""

    def __init__(self, challenge_id: str, title: str, description: str, difficulty: str,
                 language: str, time_limit_minutes: int, starter_code: str = "",
                 test_cases: List[Dict] = None, solution: str = ""):
        self.id = challenge_id
        self.title = title
        self.description = description
        self.difficulty = difficulty  # Easy, Medium, Hard
        self.language = language
        self.time_limit_minutes = time_limit_minutes
        self.starter_code = starter_code
        self.test_cases = test_cases or []
        self.solution = solution

    def to_dict(self) -> Dict:
        """Convert to dictionary for API response."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'difficulty': self.difficulty,
            'language': self.language,
            'time_limit_minutes': self.time_limit_minutes,
            'starter_code': self.starter_code,
            'test_cases_count': len(self.test_cases),
            'test_cases': [
                {'input': tc.get('input'), 'expected_output': tc.get('expected_output')}
                for tc in self.test_cases[:3]  # Show first 3 test cases only
            ]
        }


class CodingChallengeBank:
    """Repository of coding challenges by language."""

    def __init__(self):
        self.challenges = {
            'java': self._build_java_challenges(),
            'python': self._build_python_challenges(),
            'javascript': self._build_javascript_challenges(),
            'typescript': self._build_typescript_challenges(),
            'cpp': self._build_cpp_challenges(),
        }

    def _build_java_challenges(self) -> List[CodingChallenge]:
        """Build Java coding challenges."""
        return [
            # EASY - 5 minutes
            CodingChallenge(
                'java_easy_001',
                'Two Sum',
                'Given an array of integers nums and an integer target, return the indices of the two numbers that add up to target.\nYou may assume each input has exactly one solution, and you cannot use the same element twice.',
                'Easy',
                'java',
                5,
                starter_code='''public class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Your code here
        return new int[]{};
    }
}''',
                test_cases=[
                    {'input': 'nums = [2,7,11,15], target = 9', 'expected_output': '[0,1]'},
                    {'input': 'nums = [3,2,4], target = 6', 'expected_output': '[1,2]'},
                    {'input': 'nums = [3,3], target = 6', 'expected_output': '[0,1]'},
                ],
                solution='''public class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                return new int[]{map.get(complement), i};
            }
            map.put(nums[i], i);
        }
        return new int[]{};
    }
}'''
            ),

            CodingChallenge(
                'java_easy_002',
                'Reverse String',
                'Write a function that reverses a string. The input string is given as an array of characters s.\nYou must do this by modifying the input array in-place with O(1) extra memory.',
                'Easy',
                'java',
                5,
                starter_code='''public class Solution {
    public void reverseString(char[] s) {
        // Your code here
    }
}''',
                test_cases=[
                    {'input': 's = ["h","e","l","l","o"]', 'expected_output': '["o","l","l","e","h"]'},
                    {'input': 's = ["H","a","n","n","a","h"]', 'expected_output': '["h","a","n","n","a","H"]'},
                ],
                solution='''public class Solution {
    public void reverseString(char[] s) {
        int left = 0, right = s.length - 1;
        while (left < right) {
            char temp = s[left];
            s[left] = s[right];
            s[right] = temp;
            left++;
            right--;
        }
    }
}'''
            ),

            # MEDIUM - 10 minutes
            CodingChallenge(
                'java_medium_001',
                'Longest Substring Without Repeating Characters',
                'Given a string s, find the length of the longest substring without repeating characters.',
                'Medium',
                'java',
                10,
                starter_code='''public class Solution {
    public int lengthOfLongestSubstring(String s) {
        // Your code here
        return 0;
    }
}''',
                test_cases=[
                    {'input': 's = "abcabcbb"', 'expected_output': '3'},
                    {'input': 's = "bbbbb"', 'expected_output': '1'},
                    {'input': 's = "pwwkew"', 'expected_output': '3'},
                ],
                solution='''public class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> map = new HashMap<>();
        int maxLen = 0, start = 0;
        for (int i = 0; i < s.length(); i++) {
            if (map.containsKey(s.charAt(i))) {
                start = Math.max(start, map.get(s.charAt(i)) + 1);
            }
            map.put(s.charAt(i), i);
            maxLen = Math.max(maxLen, i - start + 1);
        }
        return maxLen;
    }
}'''
            ),

            CodingChallenge(
                'java_medium_002',
                'Binary Tree Level Order Traversal',
                'Given the root of a binary tree, return the level order traversal of its nodes\' values (i.e., from left to right, level by level).',
                'Medium',
                'java',
                10,
                starter_code='''public class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        // Your code here
        return new ArrayList<>();
    }
}''',
                test_cases=[
                    {'input': 'root = [3,9,20,null,null,15,7]', 'expected_output': '[[3],[9,20],[15,7]]'},
                    {'input': 'root = [1]', 'expected_output': '[[1]]'},
                ],
                solution='''public class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) return result;

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()) {
            int size = queue.size();
            List<Integer> level = new ArrayList<>();
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                level.add(node.val);
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
            result.add(level);
        }
        return result;
    }
}'''
            ),

            # HARD - 15 minutes
            CodingChallenge(
                'java_hard_001',
                'Median of Two Sorted Arrays',
                'Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.\nThe overall run time complexity should be O(log (m+n)).',
                'Hard',
                'java',
                15,
                starter_code='''public class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        // Your code here - must achieve O(log(m+n))
        return 0.0;
    }
}''',
                test_cases=[
                    {'input': 'nums1 = [1,3], nums2 = [2]', 'expected_output': '2.0'},
                    {'input': 'nums1 = [1,2], nums2 = [3,4]', 'expected_output': '2.5'},
                ],
                solution='''public class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        if (nums1.length > nums2.length) {
            return findMedianSortedArrays(nums2, nums1);
        }

        int m = nums1.length, n = nums2.length;
        int low = 0, high = m;

        while (low <= high) {
            int cut1 = (low + high) / 2;
            int cut2 = (m + n + 1) / 2 - cut1;

            int left1 = cut1 == 0 ? Integer.MIN_VALUE : nums1[cut1 - 1];
            int left2 = cut2 == 0 ? Integer.MIN_VALUE : nums2[cut2 - 1];
            int right1 = cut1 == m ? Integer.MAX_VALUE : nums1[cut1];
            int right2 = cut2 == n ? Integer.MAX_VALUE : nums2[cut2];

            if (left1 <= right2 && left2 <= right1) {
                if ((m + n) % 2 == 0) {
                    return (Math.max(left1, left2) + Math.min(right1, right2)) / 2.0;
                } else {
                    return Math.max(left1, left2);
                }
            } else if (left1 > right2) {
                high = cut1 - 1;
            } else {
                low = cut1 + 1;
            }
        }
        return -1.0;
    }
}'''
            ),
        ]

    def _build_python_challenges(self) -> List[CodingChallenge]:
        """Build Python coding challenges."""
        return [
            # EASY - 5 minutes
            CodingChallenge(
                'python_easy_001',
                'Palindrome Number',
                'Given an integer x, return True if x is a palindrome, and False otherwise.\nDo this without converting to string.',
                'Easy',
                'python',
                5,
                starter_code='''def isPalindrome(x: int) -> bool:
    # Your code here
    pass''',
                test_cases=[
                    {'input': 'x = 121', 'expected_output': 'True'},
                    {'input': 'x = -121', 'expected_output': 'False'},
                    {'input': 'x = 10', 'expected_output': 'False'},
                ],
                solution='''def isPalindrome(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reversed_num = 0
    while x > reversed_num:
        reversed_num = reversed_num * 10 + x % 10
        x //= 10

    return x == reversed_num or x == reversed_num // 10'''
            ),

            # MEDIUM - 10 minutes
            CodingChallenge(
                'python_medium_001',
                'Word Ladder',
                'Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord.\nYou can only add one letter at a time.',
                'Medium',
                'python',
                10,
                starter_code='''def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    # Your code here
    pass''',
                test_cases=[
                    {'input': 'beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]', 'expected_output': '5'},
                    {'input': 'beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]', 'expected_output': '0'},
                ],
                solution='''def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0

    queue = deque([(beginWord, 1)])

    while queue:
        word, level = queue.popleft()
        if word == endWord:
            return level

        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                nextWord = word[:i] + c + word[i+1:]
                if nextWord in wordSet:
                    wordSet.remove(nextWord)
                    queue.append((nextWord, level + 1))

    return 0'''
            ),
        ]

    def _build_javascript_challenges(self) -> List[CodingChallenge]:
        """Build JavaScript coding challenges."""
        return [
            CodingChallenge(
                'js_easy_001',
                'Remove Duplicates from Sorted Array',
                'Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place.\nReturn the number of unique elements.',
                'Easy',
                'javascript',
                5,
                starter_code='''var removeDuplicates = function(nums) {
    // Your code here
    return 0;
};''',
                test_cases=[
                    {'input': 'nums = [1,1,2]', 'expected_output': '2, nums = [1,2,_]'},
                    {'input': 'nums = [0,0,1,1,1,2,2,3,3,4]', 'expected_output': '5'},
                ],
                solution='''var removeDuplicates = function(nums) {
    if (nums.length === 0) return 0;
    let k = 1;
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] !== nums[i - 1]) {
            nums[k] = nums[i];
            k++;
        }
    }
    return k;
};'''
            ),
        ]

    def _build_typescript_challenges(self) -> List[CodingChallenge]:
        """Build TypeScript coding challenges."""
        return [
            CodingChallenge(
                'ts_easy_001',
                'Merge Sorted Array',
                'You are given two integer arrays nums1 and nums2, sorted in non-decreasing order.\nMerge nums2 into nums1 as one sorted array.',
                'Easy',
                'typescript',
                5,
                starter_code='''function merge(nums1: number[], m: number, nums2: number[], n: number): void {
    // Your code here
}''',
                test_cases=[
                    {'input': 'nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3', 'expected_output': '[1,2,2,3,5,6]'},
                ],
                solution='''function merge(nums1: number[], m: number, nums2: number[], n: number): void {
    let p1 = m - 1, p2 = n - 1, p = m + n - 1;
    while (p1 >= 0 && p2 >= 0) {
        if (nums1[p1] > nums2[p2]) {
            nums1[p] = nums1[p1];
            p1--;
        } else {
            nums1[p] = nums2[p2];
            p2--;
        }
        p--;
    }
    while (p2 >= 0) {
        nums1[p] = nums2[p2];
        p2--;
        p--;
    }
}'''
            ),
        ]

    def _build_cpp_challenges(self) -> List[CodingChallenge]:
        """Build C++ coding challenges."""
        return [
            CodingChallenge(
                'cpp_easy_001',
                'Valid Parentheses',
                'Given a string s containing just the characters \'(\', \')\', \'{\', \'}\', \'[\' and \']\',\ndetermine if the input string is valid.',
                'Easy',
                'cpp',
                5,
                starter_code='''class Solution {
public:
    bool isValid(string s) {
        // Your code here
        return false;
    }
};''',
                test_cases=[
                    {'input': 's = "()"', 'expected_output': 'true'},
                    {'input': 's = "()[]{}"', 'expected_output': 'true'},
                    {'input': 's = "(]"', 'expected_output': 'false'},
                ],
                solution='''class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        for (char c : s) {
            if (c == '(' || c == '[' || c == '{') {
                st.push(c);
            } else {
                if (st.empty()) return false;
                char top = st.top();
                st.pop();
                if ((c == ')' && top != '(') ||
                    (c == ']' && top != '[') ||
                    (c == '}' && top != '{')) {
                    return false;
                }
            }
        }
        return st.empty();
    }
};'''
            ),
        ]

    def get_challenges_by_language(self, language: str, difficulty: str = None) -> List[CodingChallenge]:
        """Get challenges for a specific language, optionally filtered by difficulty."""
        if language.lower() not in self.challenges:
            return []

        challenges = self.challenges[language.lower()]

        if difficulty:
            challenges = [c for c in challenges if c.difficulty == difficulty]

        return challenges

    def get_random_challenge(self, language: str, difficulty: str = None) -> CodingChallenge:
        """Get a random challenge for a language and optional difficulty."""
        challenges = self.get_challenges_by_language(language, difficulty)
        if not challenges:
            return None
        return random.choice(challenges)

    def get_challenge_by_id(self, challenge_id: str) -> CodingChallenge:
        """Get a specific challenge by ID."""
        for language_challenges in self.challenges.values():
            for challenge in language_challenges:
                if challenge.id == challenge_id:
                    return challenge
        return None

    def get_statistics(self) -> Dict[str, Dict]:
        """Get statistics about available challenges."""
        stats = {}
        for lang, challenges in self.challenges.items():
            easy = len([c for c in challenges if c.difficulty == 'Easy'])
            medium = len([c for c in challenges if c.difficulty == 'Medium'])
            hard = len([c for c in challenges if c.difficulty == 'Hard'])

            stats[lang] = {
                'total': len(challenges),
                'easy': easy,
                'medium': medium,
                'hard': hard,
                'total_questions': easy + medium + hard
            }
        return stats
