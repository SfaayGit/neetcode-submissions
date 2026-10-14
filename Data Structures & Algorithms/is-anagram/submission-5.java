class Solution {
    public boolean isAnagram(String s, String t) {
          char[] chars1 = s.toCharArray();
        char[] chars2 = t.toCharArray();
        Arrays.sort(chars1);
        Arrays.sort(chars2);
        String sorteds = new String(chars1);
        String sortedt = new String(chars2);
            return (sorteds.equals(sortedt)) ? true : false;
    }
}
