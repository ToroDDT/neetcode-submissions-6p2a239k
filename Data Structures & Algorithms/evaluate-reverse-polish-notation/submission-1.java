
class Solution {
    public int evalRPN(String[] tokens) {
        // We use Integer so we can perform math directly after popping
        Stack<Integer> stack = new Stack<>();

        for (String v : tokens) {
            switch (v) {
                case "+":
                    // Auto-unboxing: stack.pop() returns Integer, Java treats it as int
                    stack.push(stack.pop() + stack.pop());
                    break;

                case "-":
                    // Order matters: [top-1] - [top]
                    int rightOperandSub = stack.pop();
                    int leftOperandSub = stack.pop();
                    stack.push(leftOperandSub - rightOperandSub);
                    break;

                case "*":
                    stack.push(stack.pop() * stack.pop());
                    break;

                case "/":
                    // Order matters: [top-1] / [top]
                    int rightOperandDiv = stack.pop();
                    int leftOperandDiv = stack.pop();
                    stack.push(leftOperandDiv / rightOperandDiv);
                    break;

                default:
                    // TYPE CONVERSION: Convert the String token to a primitive int
                    // and push it onto the Stack (where it is boxed to an Integer)
                    stack.push(Integer.parseInt(v));
                    break;
            }
        }

        // The final remaining value on the stack is our result
        return stack.pop();
    }
}