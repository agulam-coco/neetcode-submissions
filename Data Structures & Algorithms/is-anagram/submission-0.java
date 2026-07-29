class Solution {
    public boolean isAnagram(String s, String t) {

        //first check lengths are different
        if(s.length()!= t.length()){
            return false;
        }

        //hash each value in the hash map
        HashMap<Character,Integer> newHash = new HashMap<>();

        for(char letter : s.toCharArray()){
            newHash.put(letter, newHash.getOrDefault(letter, 0) + 1);
        }

        //t
        for(char letter : t.toCharArray()){
            if(!newHash.containsKey(letter)){
                return false;
            }
            else{
                newHash.put(letter, newHash.get(letter)-1);
            }
        }

        //check everything is 0
        for(int value: newHash.values()){
         if(value != 0){
            return false;
         }
        }
        return true;

    }
}
