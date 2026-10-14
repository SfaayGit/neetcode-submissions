class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        //to do list
        //1 - anagram algo (check all sorted strings)
        //2 - get indexes of the same one and store them into an array
        //3 - do for all types of strings.
        HashMap<String, List<String>> map = new HashMap<>();
        for(String s: strs){
          String sorted = s.chars().sorted().collect(StringBuilder::new, StringBuilder::appendCodePoint, StringBuilder::append).toString();
         map.putIfAbsent(sorted, new ArrayList<>());
           map.get(sorted).add(s);
        }
        return new ArrayList<>(map.values());
    }
}
