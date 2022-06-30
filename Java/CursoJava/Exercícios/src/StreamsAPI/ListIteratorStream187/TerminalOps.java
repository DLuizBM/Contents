package StreamsAPI.ListIteratorStream187;

import java.util.Arrays;
import java.util.List;
import java.util.function.BinaryOperator;
import java.util.stream.Collectors;

public class TerminalOps {

    public static void main(String[] args) {
        List<Integer> nums = Arrays.asList(1, 2, 3);
        BinaryOperator<Integer> sum = (ac, num) -> ac + num;
        Integer num = nums.stream().reduce(0, sum);
    }
    
}
