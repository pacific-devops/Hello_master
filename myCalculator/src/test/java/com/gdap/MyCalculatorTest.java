import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class MyCalculatorTest {

    @Test
    public void testAdd() {
        MyCalculator calc = new MyCalculator();
        assertEquals(5, calc.add(2, 3));
    }

    @Test
    public void testSubtract() {
        MyCalculator calc = new MyCalculator();
        assertEquals(1, calc.subtract(3, 2));
    }

    @Test
    public void testMultiply() {
        MyCalculator calc = new MyCalculator();
        assertEquals(6, calc.multiply(2, 3));
    }

    @Test
    public void testDivide() {
        MyCalculator calc = new MyCalculator();
        assertEquals(2.0, calc.divide(6, 3));
    }

    @Test
    public void testDivideByZero() {
        MyCalculator calc = new MyCalculator();
        assertThrows(ArithmeticException.class, () -> calc.divide(1, 0));
    }
}
