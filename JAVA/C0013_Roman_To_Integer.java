class Solution {
    public int romanToInt(String s) {
        // read thru the string, when the char is C or X or I, check following charactor
        // Create the roman number dictionary to place data
        int num = 0;
        int l = s.length();
        int last = 1000;
        for (int i = 0; i < l; i++) {
            int v = getValue(s.charAt(i));
            if (v > last) {
                num = num - last * 2; // the reason it need to times 2 is to take back previously added wrong, and also take back from true number, like IV is 4. 
            }
            num = num + v;
            last = v;
            // System.out.println( (String)num + ", last" + (String) v);
        }
        
        return num;
        
    }
    
    private int getValue(char c) {
        switch(c) {
            case 'I': return 1;
            case 'V': return 5;
            case 'X' : return 10;
            case 'L' : return 50;
            case 'C' : return 100;
            case 'D' : return 500;
            case 'M' : return 1000;
            default : return 0;
        }
    }
}
