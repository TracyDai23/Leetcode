//my draft: wrong code.
class Solution {
    public boolean isValid(String s) {
        if (s.length() == 0) return true;
        List<Integer> chk = new ArrayList<Integer>(){{
                        add(0);
                        add(0);
                        add(0);
                          }};
       for(int i = 0; i<s.length(); i++) {
           switch(s.charAt(i)) {
               case '(':
                   chk[0] +=1;
                   break;
               case ")":
                   if (chk[0]>0) {
                       chk[0]-=1;
                       break;
                   } else {
                       return false;
                   }
               case "[":
                   chk[1] +=1;
                   break;
               case "]":
                   if (chk[1]>0) {
                       chk[1]-=1;
                       break;
                   } else {
                       return false;
                   }
               case "{":
                   chk[2] +=1;
                   break;
               case "}":
                   if (chk[2]>0) {
                       chk[2]-=1;
                       break;
                   } else {
                       return false;
                   }   
           }
       }
        int sum = 0;
        for (int value : chk) {
            sum += value;
        }
        if (sum == 0) {
            return true;
        } else {
            return false;
        }
        
    }
}
