public class Solution {
    public  int StrToInt(String str) {
    if(str==""||str==null) return 0;
    int len = str.length();
    if(len==0){
        return 0;
    }
    long sum = 0;
    int count = 0;
    for (int i = len-1; i>=1 ; i--) {
        char c = str.charAt(i);
        if(isdight(c)==0){
            return 0;
        }
        else if(isdight(c)==1){
            int temp = (int) c;
            temp = temp - 48;
            sum += temp*Math.pow(10, count);
            count++;
        }else if(isdight(c)==2){
            return 0;
        }
    }
    if(str.charAt(0)=='+'){
        return (int)sum;
    }else if(str.charAt(0)=='-'){
        return (int)-sum;
    }else if(isdight(str.charAt(0))==1){
        int n = (int)str.charAt(0);
        sum += (n - 48)*Math.pow(10, len-1);
    }else{
        return 0;
    }
    return (int)sum;
}
public  int isdight(char c){
    int i = (int) c;
    if((i>=65&&i<=90)||(i>=97&&i<=122)){
        return 0;//0代表字母
    }
    else if(i>=48&&i<=57){
        return 1;//1代表数字
    }else{
        return 2;//2代表其他符号
    }
    
}
}