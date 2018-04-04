import java.util.ArrayList;
public class Solution {
public ArrayList<ArrayList<Integer> > FindContinuousSequence(int sum) {
		ArrayList<ArrayList<Integer>> al = new ArrayList<ArrayList<Integer>>();
		int start = 1;
      	int end = 2;
      	while(end<=sum&&start<=(int)((sum+1)/2)){
            if(getSum(start,end)==sum){
                ArrayList<Integer> temp = new ArrayList<Integer>();
                for(int i = start;i<=end;i++){
                	temp.add(i);
       			}
                al.add(temp);
                start++;
            }
            else if(getSum(start,end)<sum){
                end++;
            }
            else{
                start++;
            }
      	 }
        return al;
	}
	public int getSum(int a,int b){
        int result = 0;
        for(int i = a;i<=b;i++){
            result+=i;
        }
        return result;
    }
}