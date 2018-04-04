public class Solution {
    public int Sum_Solution(int n) {
        int re=0;
		boolean whatever=false;
		int a=-1;
		whatever=(n!=0)&&(a==(re=Sum_Solution(n-1)));
		return re+n;
    }
}