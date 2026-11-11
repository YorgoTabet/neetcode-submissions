class Solution {
    public boolean isValid(String s) {
        if(s.length() <= 1) return false;
        Map<Character, Character> closing = new HashMap<>(Map.of(
            ')', '(',
            '}', '{',
            ']', '['
            ));

        Deque<Character> stack = new ArrayDeque<>();

        for(Character c: s.toCharArray()) {
            if(closing.containsKey(c)){
                if(stack.size() < 1) return false;
                Character pair = stack.pop();
                if(closing.get(c) != pair) return false;
            }else {
                stack.push(c);
            }
        }

        return stack.size() == 0;
    }
}
