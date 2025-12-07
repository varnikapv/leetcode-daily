
class Main {
    public static boolean f(int i, int n, String s){
        if(i >= n/2){
            return true;
        }
        while(i <= n/2){
        if (s.charAt(i) != s.charAt(n-1-i)){
            return false;
        }
        i++;
        
        }
         return f(i + 1, n, s);
    }
        
    public static void main(String[] args) {
        String s = "madsam";
        int n = s.length();
        boolean res = f(0, n, s);
        System.out.println(res);
    }
}