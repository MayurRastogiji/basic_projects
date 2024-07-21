// There are two errors in this code 
// first in line 16 op is not taking values
// second in line 59 (some issue related to parse int)

import java.util.Scanner;

public class calculator {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        calculator_arg obj = new calculator_arg();
        System.out.println("Our calculator works on integers, in future we will make it compatible with doubles value, if your answer is in double than it may vary \nSo only solve problem whoes answer as well as intermediate answer is in integer.\n\t\tThank you.");
        if (args.length == 0) {
            String op = "";
            int n1, n2;
            while (!op.equals("exit")) {
                System.out.println("Enter operation you wanna perform. \nFor Terminate this code enter exit");
                op = sc.next();
                if (op.equals("exit")) {
                    System.out.println("Thank You for using my calculator \nSee you soon.");
                    System.exit(0);
                }
                else{
                System.out.println("Enter your First operand:");
                n1 = sc.nextInt();
                System.out.println("Enter your Second operand:");
                n2 = sc.nextInt();
                // System.out.println(op);
                op = op.toLowerCase();
                switch (op) {
                    case "+", "add", "addition":
                        int result = obj.add(n1, n2);
                        System.out.println(result);
                        break;
                    case "-", "sub", "subtraction":
                        result = obj.sub(n1, n2);
                        System.out.println(result);
                        break;
                    case "*", "multiply", "multiplication":
                        result = obj.mul(n1, n2);
                        System.out.println(result);
                        break;
                    case "/", "divide", "division":
                        result = obj.div(n1, n2);
                        System.out.println(result);
                        break;
                    case "%", "modulo", "modulus":
                        result = obj.remainder(n1, n2);
                        System.out.println(result);
                        break;
                    case "^", "power", "exponential":
                        result = obj.pow(n1, n2);
                        System.out.println(result);
                        break;
                    default:
                        System.out.println("Invald operation");
                        break;
                }
            }
            }

        } else {
            int[] array;
            // String arg = args[0];
            // System.out.println(arg);
            array = new int[50];
            int j = 0;
            for (int i = 0; i < args.length; i++) {
                if (!args[i].equals("+") && !args[i].equals("-") && !args[i].equals("*") && !args[i].equals("/")
                    && !args[i].equals("%") && !args[i].equals("^")) {
                    array[j++] = Integer.parseInt(args[i]);
                } else {
                    int n1, n2;
                    if (j >= 1) {
                        n1 = array[--j];
                    } else {
                        System.out.println("Syntax Error operands not given.");
                        break;
                    }
                    if (j >= 1) {
                        n2 = array[--j];
                    } else {
                        System.out.println("Syntax Error operands not given.");
                        break;
                    }
            int result;
                    switch (args[i]) {
                        case "+":
                            result = obj.add(n1, n2);
                            array[j++] = result;
                            break;
                        case "-":
                            result = obj.sub(n1, n2);
                            array[j++] = result;
                            break;
                        case "*":
                            result = obj.mul(n1, n2);
                            array[j++] = result;
                            break;
                        case "/":
                            result = obj.div(n1, n2);
                            array[j++] = result;
                            break;
                        case "%":
                            result = obj.remainder(n1, n2);
                            array[j++] = result;
                            break;
                        case "^":
                            result = obj.pow(n1, n2);
                            array[j++] = result;
                            break;
                        default:
                            System.out.println("Invalid operation");
                            break;
                    }
                    
            
            // for (int i = 0; i < args.length; i++) {
            //     // System.out.println(args[i]);
            //     if (!args[i].equals("+") && !args[i].equals("-") && !args[i].equals("*") && !args[i].equals("/")
            //             && !args[i].equals("%") && !args[i].equals("^")) {
            //         array[j++] = Integer.parseInt(args[i]);

            //     } else {
            //         j = array.length;
            //         if (j == 0) {
            //             System.out.println("Syntax Error operands not given.");
            //         } else {
            //             int n1, n2;
            //             if (array[j] == 1111111) {
            //                 n1 = array[j - 1];
            //             } else {
            //                 n1 = array[j];
            //             }
            //             if (array[j - 1] == 1111111) {
            //                 n2 = array[j - 2];
            //             } else {
            //                 n2 = array[j - 1];
            //             }
                        
            //             switch (args[i]) {

            //                 case "+":
            //                     int result = obj.add(n1, n2);
            //                     array[j - 1] = result;
            //                     array[j] = 1111111;
            //                     break;
            //                 case "-":
            //                     result = obj.sub(n1, n2);
            //                     array[j - 1] = result;
            //                     array[j] = 1111111;
            //                     break;
            //                 case "*":
            //                     result = obj.mul(n1, n2);
            //                     array[j - 1] = result;
            //                     array[j] = 1111111;
            //                     break;
            //                 case "/":
            //                     result = obj.div(n1, n2);
            //                     array[j - 1] = result;
            //                     array[j] = 1111111;
            //                     break;
            //                 case "%":
            //                     result = obj.remainder(n1, n2);
            //                     array[j - 1] = result;
            //                     array[j] = 1111111;
            //                     break;
            //                 case "^":
            //                     result = obj.pow(n1, n2);
            //                     array[j - 1] = result;
            //                     array[j] = 1111111;
            //                     break;
            //                 default:
            //                     System.out.println("Invald operation");
            //                     break;

            //             }
                        System.out.printf("Intermediate Output %d and %d\n\n ", array[j], array[j-1]);
                        // System.out.printf("Output is : %d", result);
                    }
                }
            
            System.out.printf("Output of your given expression is %d", array[0]);
        }

        sc.close();
    }
}

class calculator_arg {
    public int add(int n1, int n2) {
        System.out.printf("Addition of %d and %d is: %d\n", n2, n1, n2+n1);
        return n1 + n2;
    }

    public int sub(int n1, int n2) {
        System.out.printf("Subtraction of %d and %d is: %d\n", n2, n1, n2 - n1);
        return n2 - n1;
    }

    public int mul(int n1, int n2) {
        System.out.printf("Multiplication of %d and %d is: %d\n", n2, n1, n2 * n1);
        return n1 * n2;
    }

    public int div(int n1, int n2) {
        System.out.printf("Division of %d and %d is: %d\n", n1, n2, n1 / n2);
        return n1 / n2;
    }

    public int remainder(int n1, int n2) {
        System.out.printf("Remainder of %d and %d is: %d\n", n2, n1, n2 % n1);
        return n2 % n1;
    }

    public int pow(int n1, int n2) {
        System.out.printf(" %d Power %d is: %d\n", n2, n1, n2 ^ n1);
        int a = 1;
        for (int i = 0; i < n2; i++) {
            a *= n1;
        }
        return a;
    }
}
