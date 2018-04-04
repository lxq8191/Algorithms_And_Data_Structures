import java.util.Stack;

public class Solution {
    Stack<Integer> stack1 = new Stack<Integer>();
    Stack<Integer> stack2 = new Stack<Integer>();
    
    public void push(int node) {
        stack1.push(new Integer(node));
    }
    
    public int pop() {
    	if(stack2.isEmpty()){//当栈2为空时，才将栈1中的元素压入栈2中，若栈2不空，则直接将栈2的最上面一个元素出栈  
            while(!stack1.isEmpty()){  
                stack2.push(stack1.pop());  
            }  
        }  
        return stack2.pop().intValue(); 
    }
}