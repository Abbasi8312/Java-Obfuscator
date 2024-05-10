public class Main {

    public enum Season {
        Winter, Summer, Fall
    }

    public interface mmd {
        public void getName();
        public int getId();
    }

    public static void main(String[] args) {
        int a;
        int num1 = 10;
        int num2 = 5;
        char letter = 'A';
        boolean isTrue = true;
        String name = "John";
        float num3 = 5.67f;
        long bigNumber = 1000000000L;
        byte smallNumber = 127;
        short smallInt = 32767;
        double anotherNum = 42.42;
        double numX = sum(num1, num2);
        System.out.println(numX);
    }

    public static int sum(int a, int b) {
        return a + b;
    }
}